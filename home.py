from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from metodos import AutomacaoHomePage

driver = webdriver.Chrome()

driver.get("https://www.flashscore.com.br/")

bot = AutomacaoHomePage(driver)

driver.maximize_window()
bot.clique("/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[1]") #cookies

bot.alemanha()# adição das ligas
bot.argentina()            
bot.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/span") # botão more
bot.portugal()
bot.holanda()
bot.times()


ligas = []

elementos_ligas = driver.find_elements(By.CSS_SELECTOR, "#my-leagues-list .leftMenu__href")

for elemento in elementos_ligas:
    item = elemento.get_attribute("href")
        
    nomepart = item.split("/")
    nomecamp = nomepart[5].strip()

    if nomecamp in ["brasileirao-betano", "serie-b", "laliga", "ligue-1", "campeonato-ingles", "serie-a", "bundesliga", "torneo-betano", "liga-portugal" ]:
        ligas.append(item)

jogos_dia = driver.find_elements(By.CSS_SELECTOR, "#live-table .eventRowLink")

jogos_filtrados = []

for elemento in jogos_dia:
    item = elemento.get_attribute("href")
    
    for liga in ligas:
        if liga in item:  
            jogos_filtrados.append(item)
            break 
        
print("Ligas selecionadas:", ligas)
print("Jogos do dia filtrados:", jogos_filtrados)

driver.quit()

