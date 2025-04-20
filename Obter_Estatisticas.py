from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metodos import RecolherEstatisticas
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from API.EnviarEstatisticas import mandarDados
from time import sleep
from selenium.webdriver.chrome.options import Options

import random

import time

url=""
tipoPartida=""
def  Obter_Estatisticas(url:str, tipoPartida:str):
    sleep(random.uniform(3.0, 5.5)) 
    desc=""    
    try:
        chrome_options = Options()
        
        chrome_options.add_argument('--no-sandbox')  # Mais estável em alguns sistemas
        chrome_options.add_argument('--disable-dev-shm-usage')  # Evita problemas de memória
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Disfarça automação
        chrome_options.add_argument('--start-maximized')  # Já inicia maximizado
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # Remove avisos
        
        driver = webdriver.Chrome(options=chrome_options)
        bot = RecolherEstatisticas(driver)
        keyboard = ActionChains(driver)
        wait = WebDriverWait(driver, 3)
        cokie = WebDriverWait(driver, 15)
        driver.get(url)
        
        cokie.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler"))).click()
        bot.pressionar_tecla(Keys.PAGE_DOWN)

        desc="falhou ao pressionar botão de estatisticas, pode ser que seja um jogo sem estatisticas, ou pode ser um jogo com mais uma variação"    
        btnEstatisticaPassou=0

        
        try:             ##detail > div:nth-child(6) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button 
            btnEstatistica=driver.find_element(By.CSS_SELECTOR, "#detail > div:nth-child(7) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button").text
            bot.cliqueCSS("#detail > div:nth-child(7) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")      
            
            if  btnEstatistica=="ESTATÍSTICAS" or btnEstatistica=="Estatísticas":
                btnEstatisticaPassou=1
            else:
                    driver.quit() 
                    raise
        except:
            try:
                btnEstatistica=driver.find_element(By.CSS_SELECTOR, "#detail > div:nth-child(6) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button ").text
                bot.cliqueCSS("#detail > div:nth-child(6) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button ")
                if  btnEstatistica=="ESTATÍSTICAS" or btnEstatistica=="Estatísticas":
                    btnEstatisticaPassou=1
                else:
                    driver.quit() 
                    raise
            except:
                btnEstatistica=driver.find_element(By.CSS_SELECTOR, "#detail > div:nth-child(6) > div.filterOver.filterOver--indent > div > a.selected > button").text      
                bot.cliqueCSS("#detail > div:nth-child(6) > div.filterOver.filterOver--indent > div > a.selected > button")
                if  btnEstatistica=="ESTATÍSTICAS" or btnEstatistica=="Estatísticas":
                    btnEstatisticaPassou=1
                else:
                    driver.quit() 
                    raise
                



        if btnEstatisticaPassou==0:
            driver.quit()       
            raise 
            
        
        desc="falha ao dados da classe partida"    

        bot.cliqueCSS("#detail > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button") 
        # esse clique é pra impedir que ele leia antes q a page carregue 
        
        partida = Partidas()
        casa = Estatisticas()
        fora = Estatisticas()    

        partida = bot.recolher_Info_Partida(driver,tipoPartida)
        casa = bot.recolher_Estatistica_Time_Base(driver,True)
        fora = bot.recolher_Estatistica_Time_Base(driver,False)
        casa.CasaOuFora='Casa'
        fora.CasaOuFora='Fora'
           
        casa.GolSofrido=fora.Gol
        fora.GolSofrido=casa.Gol
        
        
        # não busca informações em jogos amistosos ele n valem de nada
        if partida.Campeonato=="AMISTOSO INTERCLUBES":
            driver.quit()
            return
    
        InstanciarPartidaZerada(casa)
        InstanciarPartidaZerada(fora)
        desc="falha ao dados da classe Eststisticas Partida"           
        
        
        rows =driver.find_elements(By.CLASS_NAME, "wcl-row_OFViZ")
        for row in rows:
            sessao = 0
            linha = 0
            variacao = 0

            try:
                        # Tenta encontrar o <strong> dentro da linha
                full_path = driver.execute_script("""
                    function getDivPath(element) {
                        let path = [];
                        while (element !== document.body && element.parentNode) {
                            if (element.tagName.toLowerCase() === 'div') {
                                let index = Array.from(element.parentNode.children)
                                    .filter(el => el.tagName.toLowerCase() === 'div')
                                    .indexOf(element) + 1;
                                path.unshift(`div:nth-child(${index})`);
                            }
                            element = element.parentNode;
                        }
                        return path.join(" > ");
                    }
                    return getDivPath(arguments[0]);
                """, row)

                # Exemplo de full_path: (era pra ser assim )
                # "div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)"

                parts = full_path.split(" > ")
                variacao = int(parts[6].split("(")[1].replace(")", "") if len(parts) > 0 else "N/A")
                sessao = int(parts[8].split("(")[1].replace(")", "") if len(parts) > 2 else "N/A")
                linha = int(parts[9].split("(")[1].replace(")", "") if len(parts) > 3 else "N/A")
            except Exception as e:
                # print(f"Erro ao processar linha: {e}")
                continue 

            bot.pressionar_tecla(Keys.DOWN)
            
            if sessao == 2 and linha == 2: #detail > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong            
                bot.cliqueCSS(f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")        
            
            texto = ""
            try:
                texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong").text                              
                if linha == 2 and texto == 'Gols esperados (xG)':
                    continue
            except:
                print("Não está reconhecendo a linha")    
            
            bot.pressionar_tecla(Keys.ARROW_DOWN)       

            try:
                casa = bot.Partida(driver,casa,True,variacao, sessao,linha)
                fora = bot.Partida(driver, fora, False,variacao, sessao ,linha)
            except:
                print("Erro ao extrair dados da partida")
        if casa.Posse_de_bola==0 and casa.Passes==0 or fora.Posse_de_bola==0 and fora.Passes==0  :
            desc="Falha ao reconhecer dados da classe de estatisticas Partidas, Aparentemente uma variação nova ou partidas sem estatisticas"
            driver.quit() 
            raise
        else:            
            mandarDados(casa,fora,partida)
            
        driver.quit()
    except:  
        try:
            driver.quit()
        except:
            print("")
        bot.BackLogs(url,1,desc)
        return    


def InstanciarPartidaZerada(estatisticas:Estatisticas):
    #isso é para evitar q saia alguma informação nula para API

    estatisticas.Posse_de_bola = 0
    estatisticas.Total_Finalizacao = 0
    estatisticas.Chances_claras = 0
    estatisticas.Escanteios = 0
    estatisticas.Bolas_na_trave = 0
    estatisticas.Gols_de_cabeca = 0
    estatisticas.Defesas_do_goleiro = 0
    estatisticas.Impedimentos = 0
    estatisticas.Faltas = 0
    estatisticas.Cartoes_Amarelos = 0
    estatisticas.Cartoes_Vermelhos = 0
    estatisticas.Laterais_Cobrados = 0
    estatisticas.Toques_na_area_adversaria = 0
    estatisticas.Passes = 0
    estatisticas.Passes_Totais = 0
    estatisticas.Precisao_Passes = 0
    estatisticas.Passes_no_terco_final = 0
    estatisticas.Cruzamentos = 0
    estatisticas.Desarmes = 0
    estatisticas.Bolas_afastadas = 0
    estatisticas.Interceptacoes = 0
    return estatisticas


#Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/Cd7a4M4e/#/resumo-de-jogo/resumo-de-jogo", "Fora")   
