from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import RecolherEstatisticas
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas

import time

url=""
tipoPartida=""
def Obter_Estatisticas(url, tipoPartida):
    driver = webdriver.Chrome()
    bot = RecolherEstatisticas(driver)
    keyboard = ActionChains(driver)


    driver.maximize_window()
    driver.get(url)
    
    bot.cliqueCSS("#onetrust-accept-btn-handler")    
    keyboard.send_keys(Keys.DOWN).perform()  
    bot.cliqueCSS("#detail > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")

    partida = Partidas()
    casa = Estatisticas()
    fora = Estatisticas()
    
    partida = bot.recolher_Partida(driver,tipoPartida)
    casa = bot.recolher_Estatisticas(driver,tipoPartida)
    fora = bot.recolher_Partida(driver,tipoPartida)

    
    rows = driver.find_elements(By.CLASS_NAME, "wcl-row_OFViZ")

    contador =0
    for row in rows:        
        contador +=1
        texto = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[2]/strong").text 
       
        if texto == "Posse de bola":
            casa.Posse_de_bola= bot.atributo_Casa(driver,contador)
            fora.Posse_de_bola = bot.atributo_Fora(driver,contador)
        
       
    driver.quit()



Obter_Estatisticas("https://www.flashscore.com.br/jogo/4fUKLQW0/#/resumo-de-jogo/resumo-de-jogo", "Confronto_Direto")