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
    
    
    bot.cliqueCSS("#detail > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")   # esse clique é pra impedir que ele leia antes q a page carregue 

    partida = Partidas()
    casa = Estatisticas()
    fora = Estatisticas()
    
    partida = bot.recolher_Partida(driver,tipoPartida,True)
    casa = bot.recolher_Partida(driver,tipoPartida,False)
    fora = bot.recolher_Partida(driver,tipoPartida,False)

    rows = driver.find_elements(By.CLASS_NAME, "wcl-row_OFViZ")

    contador =0
    for row in rows:        
        contador +=1
        
        casa =bot.Partida(driver,contador,casa,True)
        fora =bot.Partida(driver,contador,fora,False)
            
        #agora ta vindo completinho todos as informações das partidas analisadas
            
            
            
    driver.quit()



Obter_Estatisticas("https://www.flashscore.com.br/jogo/4fUKLQW0/#/resumo-de-jogo/resumo-de-jogo", "Confronto_Direto")