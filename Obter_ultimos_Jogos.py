from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import automacaoUltimosJogos
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from models.EstatisticaTimes import EstatisticasTimes
from Obter_Estatisticas import Obter_Estatisticas
from EnviarEstatisticas import gerarEstatiscasMedias
from EnviarEstatisticas import mandarPartidaAnalise
from concurrent.futures import ThreadPoolExecutor

import time


url=""
def Ultimos_Jogos(url):
    desc=''
    try:
        driver = webdriver.Chrome()
        
        bot = automacaoUltimosJogos(driver)

        driver.get(url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)       
        cokie = WebDriverWait(driver, 15)
        cokie.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler"))).click()   


        try:
            partidaAoVivo = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__status > div > span").text
            if partidaAoVivo!="":
                driver.quit()            
                print("Partida está ao vivo Não analisamos partida ao vivo URL: ", url)
                return
        except:
            print("")

        desc='Falha ao reconhecer dados da classe Partida'
        
        partida = Partidas()

        partida.NomeTimeCasa = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow").text
        partida.NomeTimeFora = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow").text
        nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.detail__breadcrumbs > nav > ol > li:nth-child(3) > a").text
        nomepart = nome.split(" - ")
        partida.Campeonato = nomepart[0].strip()
        partida.PartidaAnalise = True
        diajogo =str(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__startTime > div").text)
        partida.data = datetime.strptime(diajogo, "%d.%m.%Y %H:%M")
        partida.TipoPartida = "PartidaAnalise"

        if partida.Campeonato=="AMISTOSO INTERCLUBES":
            driver.quit()
            return


        adiado = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__status > span").text
        if adiado == "ADIADO":
            driver.quit()
            return
        
        
        try:
            if nomepart[1].strip() in ["PLAYOFFS", "QUALIFICAÇÃO"]:
                brasileiro = False
                if "Bra" in partida.NomeTimeCasa or "Bra" in partida.NomeTimeFora:
                    brasileiro = True
                if not brasileiro: # não analisamos jogos mata a mata
                    driver.quit()
                    return
        except:
            print("")
            
        desc='Falha ao recolher Urls de Partidas anteriores'
                                ##detail > div.detailOver > div > a:nth-child(3) > button
        driver.find_element(By.CSS_SELECTOR, "#detail > div.detailOver > div > a:nth-child(3) > button").click()
        # Listas para armazenar dados
        items = [] 
        confrontoDireto = [] 
        casacasa = [] 
        forafora = [] 
        keyboard = ActionChains(driver)
        contador = 0    #contador é pq são até os 5 ultimos jogos
        count = 3      
        jogofora=0 #para verificar se ja passou a seunda ou terceira coluna
        bot.pressionar_tecla(Keys.DOWN)
        try:
            botaocasa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(6) > div > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")))
            botaofora = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(6) > div > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")))
        except:
            try:
                botaocasa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(7) > div > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")))
                botaofora = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(7) > div > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")))
            except:
                botaocasa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(8) > div > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")))
                botaofora = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div:nth-child(8) > div > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")))

        confronto = driver.find_elements(By.CLASS_NAME, "rows") 
        #essa variavel é para evitar excessões como passar por jogos q o bot n leu pq os times nunca se enfretaram ent melhor tirar
        leu_tudo=0
        for confr in confronto:
            if contador==5 and count ==3 and confrontoDireto== []:
                break
            
            if contador==5 and count ==3:
                count = 1
                keyboard.send_keys(Keys.PAGE_UP).perform()
                keyboard.send_keys(Keys.PAGE_UP).perform()
                botaocasa.click()
                contador = 0
            if contador==5 and count==1:
                keyboard.send_keys(Keys.PAGE_UP).perform()
                botaofora.click()
                jogofora=1 
                contador = 0
                leu_tudo=1
            while contador!= 5:
                contador+=1
                #count é em qual coluna do flashscore está localizado (3 é sobre confronto diretos) 
                # os confrontos diretos variam entre quem é o mandante 
                Url_Jogo= bot.reconhecerUltimosJogos(count,contador)
                if Url_Jogo=='' and contador==1:
                    contador=5
                    break
                items.append(Url_Jogo) 
                if count == 3:                  
                    confrontoDireto.append(Url_Jogo)
                elif count == 1 and jogofora==0:
                    casacasa.append(Url_Jogo)
                elif count == 1 and jogofora==1:
                    forafora.append(Url_Jogo)
        driver.quit()
        
        
        if leu_tudo==1:      
            desc="Erro ao enviar Partida Analise"
            mandarPartidaAnalise(partida)
            desc="Falha ao chamar metodo Obter_Estatisticas"
            
            with ThreadPoolExecutor(max_workers=3) as executor:  # 3 threads
            # Enfileira TODAS as URLs de uma vez
                executor.map(lambda url: Obter_Estatisticas(url, "Confronto Direto"), confrontoDireto)
                executor.map(lambda url: Obter_Estatisticas(url, "Casa"), casacasa)
                executor.map(lambda url: Obter_Estatisticas(url, "Fora"), forafora)

            gerarEstatiscasMedias(partida.NomeTimeCasa,partida.NomeTimeFora)
        else:
            desc='Erro ao ler Partidas anteriores, provalvelmente uma variação nova ou pode ser que esses times nunca tenham jogados Juntos'
            raise
            
    except:
        try:
            driver.quit()
        except:
            print("")
        print("ihhhhhhhhhhhhhhhh Deu pau")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("MADEIRAAAAA !!!!!!!!")
        bot.BackLogs(url,2,desc)
        return




# Ultimos_Jogos("https://www.flashscore.com.br/jogo/futebol/ppxuQFlT/#/resumo-de-jogo")