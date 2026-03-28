from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import automacaoUltimosJogos
from models.Partidas import Partidas
from Obter_Estatisticas import Obter_Estatisticas
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options




def Obter_Partidas_Liga(url:str):
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
        
        
        notMostrarMaisbtn = 0
        while notMostrarMaisbtn==0:
            try:
                bot.pressionar_tecla(Keys.END)                
                btnMostrarMaisJogos = bot.cliqueCSS("#tournamentPage > div:nth-child(2) > section > div.wcl-footer_yI6S3 > button")   
            except:
                notMostrarMaisbtn=1

        matches = driver.find_elements("css selector", "div[data-event-row='true']")

        urls = []

        for match in matches:
            url = match.find_element("css selector", "a.eventRowLink").get_attribute("href")
            urls.append(url)      
        


        driver.quit()

        desc="Falha ao chamar metodo Obter_Estatisticas"            
        with ThreadPoolExecutor(max_workers=3) as executor:
            
            bot.aguardar_se_memoria_alta()
            executor.map(lambda url: Obter_Estatisticas(url, "Teste"), urls)
            



            
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
    



Obter_Partidas_Liga("https://www.flashscore.com.br/futebol/brasil/brasileirao-betano-2025/resultados/")
Obter_Partidas_Liga("https://www.flashscore.com.br/futebol/brasil/brasileirao-betano-2024/resultados/")