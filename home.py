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


# Lista para armazenar as ligas
ligas = []

# Obtém os elementos das ligas
elementos_ligas = driver.find_elements(By.CSS_SELECTOR, "#my-leagues-list .leftMenu__href")

# Itera sobre os elementos das ligas
for elemento in elementos_ligas:
    item = elemento.get_attribute("href")
    
    # Extrai o nome do campeonato
    nomepart = item.split("/")
    nomecamp = nomepart[5].strip()

    # Verifica se o campeonato está na lista desejada
    if nomecamp in ["brasileirao-betano", "serie-b", "laliga", "ligue-1", "campeonato-ingles", "serie-a", "bundesliga", "torneo-betano", "liga-portugal", ""]:
        ligas.append(item)

# Obtém os elementos dos jogos do dia
jogos_dia = driver.find_elements(By.CSS_SELECTOR, "#live-table .eventRowLink")

# Lista para armazenar os jogos do dia que pertencem às ligas selecionadas
jogos_filtrados = []

# Itera sobre os elementos dos jogos do dia
for elemento in jogos_dia:
    item = elemento.get_attribute("href")
    
    # Verifica se o jogo pertence a uma das ligas selecionadas
    for liga in ligas:
        if liga in item:  # Verifica se a URL da liga está contida na URL do jogo
            jogos_filtrados.append(item)
            break  # Sai do loop interno se encontrar uma correspondência

driver.quit()
# Exibe as listas
print("Ligas selecionadas:", ligas)
print("Jogos do dia filtrados:", jogos_filtrados)