from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import automacaoUltimosJogos
from models.partidas import Partidas
from Obter_Estatisticas import Obter_Estatisticas
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options




def Ultimos_Jogos(url:str):
    desc=''
    try:
        
        chrome_options = Options()
    
        # --- Configurações de Performance/GPU ---
        chrome_options.add_argument("--disable-gpu")  # Soluciona o erro da GPU não suportada
        chrome_options.add_argument("--disable-software-rasterizer")  # Usa CPU para renderização
        chrome_options.add_argument("--disable-dev-shm-usage")  # Problemas de memória em containers/VMs
        chrome_options.add_argument("--no-sandbox")  # Estabilidade em alguns sistemas

        # --- Stealth Mode (evitar detecção como bot) ---
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])  # Remove logs + avisos
        chrome_options.add_experimental_option("useAutomationExtension", False)

        # --- UX/Navegação ---
        chrome_options.add_argument("--start-maximized")  # Maximiza a janela
        chrome_options.add_argument("--disable-infobars")  # Remove barra de "Chrome está sendo controlado"
        chrome_options.add_argument("--disable-extensions")  # Desativa extensões
        
        driver = webdriver.Chrome(options=chrome_options)

        bot = automacaoUltimosJogos(driver)

        driver.get(url)
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
        bot.pressionar_tecla(Keys.DOWN)
        partida = bot.recolher_Info_Partida(driver,"PartidaAnalise")                                 #detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a

        if partida.Campeonato == "COPA DO MUNDO":
            return 

        partida.Url_Partida=url

        if partida.Campeonato=="AMISTOSO INTERCLUBES" or partida.Campeonato=='COPA AMÉRICA FEMININA':
            driver.quit()
            return


        adiado = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__status > span").text
        if adiado == "ADIADO":
            driver.quit()
            return
        

            
        desc='Falha ao recolher Urls de Partidas anteriores'
                                #detail > div.detailOver > div > a:nth-child(3) > button
        confrontoDireto = [] 
        casacasa = [] 
        forafora = [] 

        # Listas para armazenar dados


        bot.pressionar_tecla(Keys.DOWN)
        bot.pressionar_tecla(Keys.DOWN)

       
        btnH2H = bot.cliqueCSS("#detail > div.detailOver > div > a:nth-child(3) > button")   
        
           
        bot.pressionar_tecla(Keys.DOWN)
        bot.pressionar_tecla(Keys.DOWN)      
        btnConfrontoDireto = bot.cliqueCSS("#detail > div.tabContent__h2h > div > div.filterOver.filterOver--indent > div > a:nth-child(1) > button")         
        confrontoDireto = bot.recolherUltimasPartidas(driver,True )
        
        
        bot.pressionar_tecla(Keys.HOME)
        bot.pressionar_tecla(Keys.DOWN)
        bot.pressionar_tecla(Keys.DOWN)
        btnCasaCasaPartidas = bot.cliqueCSS("#detail > div.tabContent__h2h > div > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")         
        casacasa = bot.recolherUltimasPartidas(driver,False )
        
        bot.pressionar_tecla(Keys.HOME)
        bot.pressionar_tecla(Keys.DOWN)
        bot.pressionar_tecla(Keys.DOWN)
        btnForaForaPartidas = bot.cliqueCSS("#detail > div.tabContent__h2h > div > div.filterOver.filterOver--indent > div > a:nth-child(3) > button")    
        forafora = bot.recolherUltimasPartidas(driver,False )




        desc="Falha ao chamar metodo Obter_Estatisticas"            
        with ThreadPoolExecutor(max_workers=1) as executor:
            
            bot.aguardar_se_memoria_alta()
            executor.map(lambda url: Obter_Estatisticas(url, "liga"), confrontoDireto)
            
            bot.aguardar_se_memoria_alta()
            executor.map(lambda url: Obter_Estatisticas(url, "liga"), casacasa)
            
            bot.aguardar_se_memoria_alta()
            executor.map(lambda url: Obter_Estatisticas(url, "liga"), forafora)



            
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
    
    
    finally:
            try:
                driver.quit()
            except:
                None
    



#Ultimos_Jogos("https://www.flashscore.com.br/jogo/futebol/dr-congo-phn9mm8H/jamaica-CWmDb3zj/?mid=nHRhJvF8")