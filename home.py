import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))  # Adiciona a raiz do projeto ao PATH

from enviarEmail.enviarErro import EmailBackLog
from enviarEmail.EnviarPalpites import EmailPalpites
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from metodos import AutomacaoHomePage
from Obter_ultimos_Jogos import Ultimos_Jogos
from ObterJogosEspecificos import Obter_Times_Especificos
from datetime import datetime
from resetarBanco import resetarBanco
import os


#resetarBanco()
driver = webdriver.Chrome()
url="https://www.flashscore.com.br/"
driver.get(url)
desc=""
try:
    bot = AutomacaoHomePage(driver)
    driver.maximize_window()
    desc="O erro aconteceu logo no começo da page especificamente na hora de adicionar as ligas alternativas"
    
    bot.clique("/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[1]") #cookies
    #principal liga dos paises:
    bot.alemanha()
    bot.argentina()            
    bot.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/span") # botão more (para mostrar todos os paises)
    bot.portugal()
    bot.holanda()
        


    ligas = []
    desc="O erro aconteceu ao buscar ligas, talvez tenha mudado o CSS da Home"
    elementos_ligas = driver.find_elements(By.CSS_SELECTOR, "#my-leagues-list .leftMenu__href")

    for elemento in elementos_ligas:
        item = elemento.get_attribute("href")
            
        nomepart = item.split("/")
        nomecamp = nomepart[5].strip()

        if nomecamp in ["brasileirao-betano", "serie-b", "laliga", "ligue-1", "campeonato-ingles", "serie-a", "bundesliga", "torneo-betano", "liga-portugal","paulista", "eredivisie", "copa-libertadores","liga-dos-campeoes" ]:
            ligas.append(item)



    
    desc="erro ao Buscar Jogos do dia "
    
    jogos_dia = driver.find_elements(By.CSS_SELECTOR, "#live-table > section > div > div:nth-child(1) .eventRowLink")

    items = []

    for element in jogos_dia:
        item = element.get_attribute("href")
        items.append(item)


        
    driver.quit()

    desc="erro ao Buscar Jogos especificos  "
    jogos_Especificos=Obter_Times_Especificos()
    for item in jogos_Especificos:
        items.append(item)

    dia=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    if items==[]:
        desc=f"Nem um jogo encontrado no dia {dia}, pode ser q realmente  não tenha mas é sempre bom verificar "
        bot.BackLogs(url,3,desc)
        
    for item in items:
        Ultimos_Jogos(item)
        
    try:
        EmailBackLog()        
    except:
        print("")
    try:
        EmailPalpites()
    except:    
        print("")

        
    os.system("shutdown /s /t 1")

    
except:
    bot.BackLogs(url,3,desc)
