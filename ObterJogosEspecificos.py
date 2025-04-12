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
from metodos import AutomacaoHomePage

import time


url=""      # bom esse metodo aqui vai ser referente 
def Obter_Times_Especificos():
    driver = webdriver.Chrome()
    
    bot = AutomacaoHomePage(driver)


    driver.get("https://www.flashscore.com.br/favoritos/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    cookie_button.click()
    driver.find_element(By.CSS_SELECTOR,"#my-teams-list > div.leftMenu__buttonBlock > div").click()

    bot.times()
    driver.refresh()
    try:
        driver.find_element(By.CSS_SELECTOR,"#radix-\:r9\: > div > header > div > button > svg").click()
        driver.find_element(By.CSS_SELECTOR,"#live-table > div > div > div:nth-child(1) > div").click()
    except:
        print("\n")
    

    dia = driver.find_element(By.CSS_SELECTOR, "#live-table > div > div > div:nth-child(1) > div").text 
    diaDeHoje = dia.split(" - ")
    lista_URl=[]
    if diaDeHoje[0]=="Hoje":##g_1_Qwr9Q7QN
        campeonato_do_dia = driver.find_elements(By.CSS_SELECTOR, "#live-table > div > div > div:nth-child(2)")
        
        for jogo in campeonato_do_dia:
            jogos = jogo.find_elements(By.CLASS_NAME, "eventRowLink")
            
            for partidas in jogos:
                url = partidas.get_attribute("href")
                lista_URl.append(url)
    
    driver.quit()
    return  lista_URl

# Obter_Times_Especificos()