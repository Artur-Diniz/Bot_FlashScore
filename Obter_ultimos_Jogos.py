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
from EnviarEstatisticas import mandarDados
import time


url=""
def Ultimos_Jogos(url):
    driver = webdriver.Chrome()
    
    bot = automacaoUltimosJogos(driver)

    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    cookie_button.click()


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



    # Verifica se o jogo foi adiado
    adiado = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__status > span").text
    if adiado == "ADIADO":
        driver.quit()
        exit()

    if nomepart[1].strip() in ["PLAYOFFS", "QUALIFICAÇÃO"]:
        brasileiro = False
        if "Bra" in partida.NomeTimeCasa or "Bra" in partida.NomeTimeFora:
            brasileiro = True
        if not brasileiro: # não analisamos jogos mata a mata
            driver.quit()
            exit()

    # try:
    # Clica no botão para abrir os ultimos jogos
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
     
    botaocasa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div.h2hSection > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")))
    botaofora = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div.h2hSection > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")))
    confronto = driver.find_elements(By.CLASS_NAME, "rows") 
    #essa variavel é para evitar excessões como passar por jogos q o bot n leu pq os times nunca se emfretaram ent melhor tirar
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
         
            if Url_Jogo=='':
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
        
        
        casa = [ Estatisticas()]
        AdversarioCasa = [ Estatisticas()]
        fora = [ Estatisticas()]
        AdversarioFora = [ Estatisticas()]

        confronto_timeA = [ Estatisticas()]
        confronto_timeB = [ Estatisticas()]

        for urls in confrontoDireto:       

            timeA = Estatisticas()
            TimeB = Estatisticas()
            Partida = Partidas()
            Partida, timeA, timeB = Obter_Estatisticas(urls,"Confronto Direto")

            if(timeA.NomeTimeCasa == partida.NomeTimeCasa):
                confronto_timeA.append(timeA)
                confronto_timeB.append(timeB)
            if(timeA.NomeTimeCasa == partida.NomeTimeFora):
                confronto_timeA.append(TimeB)
                confronto_timeB.append(timeA)       
            mandarDados(timeA,timeB,Partida)

        for urls in casacasa:       

            timeA = Estatisticas()
            TimeB = Estatisticas()
            Partida = Partidas()
            Partida, timeA, timeB = Obter_Estatisticas(urls,"Casa")

            casa.append(timeA)
            AdversarioCasa.append(timeB)      
            mandarDados(timeA,timeB,Partida)


        for urls in forafora:       

            timeA = Estatisticas()
            TimeB = Estatisticas()
            Partida = Partidas()
            Partida, timeA, timeB = Obter_Estatisticas(urls,"Fora")

            fora.append(timeA)
            AdversarioFora.append(timeB)     
            mandarDados(timeA,timeB,Partida) 





#Ultimos_Jogos("https://www.flashscore.com.br/jogo/futebol/xzDxPU6K/#/resumo-de-jogo")
