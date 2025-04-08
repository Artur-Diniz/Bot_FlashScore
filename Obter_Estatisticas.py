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
    casa.CasaOuFora='Casa'
    fora.CasaOuFora='Fora'
    casa.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(1)").text)
    fora.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(3)").text)
    
    casa.GolSofrido=fora.Gol
    fora.GolSofrido=casa.Gol
  
    rows = driver.find_elements(By.CLASS_NAME, "wcl-row_OFViZ")
    for row in rows:
      
        sessao = 0
        linha = 0

        try:
        # Tenta achar a sessão do row baseado no pai
            secoes = driver.find_element(By.ID, "detail").find_elements(By.XPATH, "./div")
            for idx_sessao, sec in enumerate(secoes, start=1):
                if row in sec.find_elements(By.CLASS_NAME, "wcl-row_OFViZ"):
                    sessao = idx_sessao
                    linhas = sec.find_elements(By.CLASS_NAME, "wcl-row_OFViZ")
                    for idx_linha, linha_elem in enumerate(linhas, start=1):
                        if linha_elem == row:
                            linha = idx_linha
                            break
                    break
        except Exception as e:
            print(f"Erro ao identificar sessão e linha: {e}")

        print(f"Linha está na sessão {sessao}, linha {linha}")
        bot.pressionar_tecla(Keys.DOWN)

        if sessao==8 and linha==2:             
             bot.cliqueCSS("#detail > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")        
        
        texto=""
        if linha==2:
            try:
                texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({sessao}) > div:nth-child(2) > div.wcl-category_ITphf > div.wcl-category_7qsgP > Strong").text                                 
            except:
                print("obteção de estatisticas concluidas")
                
            if texto=="Gols esperados (xG)":
                continue
        
        bot.pressionar_tecla(Keys.DOWN)                                          
        try:                                                
            texto = driver.find_element
            (By.CSS_SELECTOR, f"#detail > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > Strong").text                              
        except:                                         #/html/body/div[4]/div[1]/div/div/main/div[6]/div[1]/div[8]/div[2]
            print("")
            
        try:
            casa =bot.Partida(driver,linha,casa,True,sessao)
            fora =bot.Partida(driver,linha,fora,False,sessao)
        except:
            print("")
        

    driver.quit()

    return partida,casa,fora 
            
            


partida,casa ,fora =Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/IBeZ9vBb/#/resumo-de-jogo/estatisticas-de-jogo/0", "Confronto_Direto")

