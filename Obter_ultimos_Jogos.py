from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

import time


url=""
def Ultimos_Jogos(url):
    driver = webdriver.Chrome()

    driver.get(url)

    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    cookie_button.click()

    # Classe para representar uma partida
    class Partidas:
        def __init__(self):
            self.NomeTimeCasa = ""
            self.NomeTimeFora = ""
            self.data = datetime.now()
            self.Campeonato = ""
            self.PartidaAnalise = False
            self.TipoPartida = ""

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
        # Clica no botão para abrir estatísticas
        driver.find_element(By.CSS_SELECTOR, "#detail > div.detailOver > div > a:nth-child(3) > button").click()

        # Listas para armazenar dados
        items = []  # Lista que armazena as URLs
        confrontoDireto = []
        casacasa = []
        forafora = []

        actions = ActionChains(driver)

        contador = 0
        count = 3      
        jogofora=0
         
        botaocasa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div.h2hSection > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")))
        botaofora = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail > div.h2hSection > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")))

        confronto = driver.find_elements(By.CLASS_NAME, "rows") #
        original_window = driver.current_window_handle

        for confr in confronto:
            
            if contador==5 and count ==3:
                count = 1                               
                actions.send_keys(Keys.PAGE_UP).perform()
                actions.send_keys(Keys.PAGE_UP).perform()
                botaocasa.click()
                contador = 0
            if contador==5 and count==1:
                actions.send_keys(Keys.PAGE_UP).perform()
                botaofora.click()
                jogofora=1
                contador = 0
            
            while contador!= 5:
                contador+=1
                
                driver.find_element(By.CSS_SELECTOR, f"#detail > div.h2hSection > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({contador})").click()
                                                        
                # driver.find_element(By.CLASS_NAME, "h2h__row ").click()
                
                wait.until(lambda driver: len(driver.window_handles) > 1)
                for window in driver.window_handles:
                    if window != original_window:
                        driver.switch_to.window(window)
                        break
                current_url = driver.current_url
                items.append(current_url)  # Armazena a URL na lista `items`
                
                if count == 3:                  
                    confrontoDireto.append(current_url)
                elif count == 1 and jogofora==0:
                    casacasa.append(current_url)
                elif count == 1 and jogofora==1:
                    forafora.append(current_url)
                    
                driver.close()
                driver.switch_to.window(original_window)

          

        # Imprime as URLs coletadas
        print("URLs coletadas:")
        for url in items:
            print(url)

        driver.quit()
    except Exception as e:
        print("Ocorreu um erro:", e)
        driver.quit()
        
        
Ultimos_Jogos("https://www.flashscore.com.br/jogo/pOrgJQRj/#/resumo-de-jogo")