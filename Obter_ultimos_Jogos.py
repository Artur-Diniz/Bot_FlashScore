from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import automacaoUltimosJogos
from models.Partidas import Partidas
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

    # Coleta os dados da partida
    partida.NomeTimeCasa = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[4]/div[2]/div[3]/div[2]/a").text
    partida.NomeTimeFora = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[4]/div[4]/div[3]/div[1]/a").text
    nome = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[3]/div/span[3]/a").text
    nomepart = nome.split(" - ")
    partida.Campeonato = nomepart[0].strip()
    partida.PartidaAnalise = True
    diajogo =str(driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]").text)
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

    try:
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
        
        for confr in confronto:
            
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
            
            while contador!= 5:
                contador+=1
                
                #count é em qual coluna do flashscore está localizado (3 é sobre confronto diretos) 
                # os confrontos diretos variam entre quem é o mandante 
                Url_Jogo= bot.reconhecerUltimosJogos(count,contador)
             
                items.append(Url_Jogo) 
                
                if count == 3:                  
                    confrontoDireto.append(Url_Jogo)
                elif count == 1 and jogofora==0:
                    casacasa.append(Url_Jogo)
                elif count == 1 and jogofora==1:
                    forafora.append(Url_Jogo)

        print("URLs coletadas:")
        for url in items:
            print(url)

        driver.quit()
    except Exception as e:
        print("Ocorreu um erro:", e)
        driver.quit()
        
        
Ultimos_Jogos("https://www.flashscore.com.br/jogo/pOrgJQRj/#/resumo-de-jogo")