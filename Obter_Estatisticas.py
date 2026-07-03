from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metodos import RecolherEstatisticas
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from models.Odd import OddMarket
from DTB.processarJogo import ProcessarJogo,GetPartidabyNamesAndDate 
from time import sleep
import psutil
from selenium.webdriver.chrome.options import Options
import random


def  Obter_Estatisticas(url:str, tipoPartida:str):
    """Retorna somente o ID da Partida Ou Zero """
    tentativa=0
    while tentativa<2 :
        tentativa+=1
        desc= f"erro ao incializar {psutil.virtual_memory()}"    
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

            bot = RecolherEstatisticas(driver)
            cokie = WebDriverWait(driver, 15)
            driver.get(url)
            sleep(random.uniform(5.0, 7.5)) 

            cokie.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler"))).click()
            try:
                cokie.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail-breadcrumbs > div:nth-child(2) > div > div > div.wcl-onboardingHeader_Mwn3C > button"))).click()
            except:
                None

            desc="erro ao  recolher sumario"  
            
            Gol_HT = bot.Sumario(driver)
            



            
            desc="falhou ao pressionar botão de estatisticas, pode ser que seja um jogo sem estatisticas, ou pode ser um jogo com mais uma variação"    
            # btnEstatistica=0
            bot.pressionar_tecla(Keys.DOWN)                
            bot.pressionar_tecla(Keys.DOWN)          
            sleep(2)   
                
            btnODDS = bot.cliqueCSS("#detail > div.detailOver > div > a:nth-child(2) > button")    
            

            seletor = """
            a[data-analytics-alias='under-over']
            """
            # seletor = """
            # a[data-analytics-alias='1x2'],
            # a[data-analytics-alias='under-over'],
            # a[data-analytics-alias='both-teams-to-score'],
            # a[data-analytics-alias='asian-handicap'],
            # a[data-analytics-alias='double-chance'],
            # a[data-analytics-alias='european-handicap'],
            # a[data-analytics-alias='draw-no-bet'],
            # a[data-analytics-alias='correct-score']
            # """
            
            
            sleep(5)
            abas = driver.find_elements(By.CSS_SELECTOR, seletor)

            BOOKMAP = {
                "16": "bet365",
                "574": "betano",
                "833": "estrela_bet",
                "933": "super_bet",
                "1157": "one_xbet"
            }

            POSITION_MAP = {
                "1x2": ["home", "draw", "away"],
                "under-over": ["line", "over", "under"],
                "both-teams-to-score": ["yes", "no"],
                "asian-handicap": ["line", "home", "away"],
                "double-chance": ["home_draw", "home_away", "draw_away"],
                "european-handicap": ["line", "home", "draw", "away"],
                "draw-no-bet": ["home", "away"],
                "correct-score": ["score", "odd"]
            }

            all_rows = []

            for aba in abas:

                alias = aba.get_attribute("data-analytics-alias")

                bot.pressionar_tecla(Keys.HOME)
                bot.cliqueElemento(aba)
                sleep(1.5)
                bot.pressionar_tecla(Keys.END)

                linhas = driver.find_elements(By.CSS_SELECTOR, ".ui-table__row")

                buffer = {}

                expected = POSITION_MAP.get(alias)

                for linha in linhas:

                    elementos = linha.find_elements(
                        By.CSS_SELECTOR,
                        "a.oddsCell__odd"
                    )

                    # -----------------------------
                    # CONTEXTO DA LINHA
                    # -----------------------------
                    market_line = None
                    selection_ctx = None

                    try:
                        ctx = linha.find_element(
                            By.CSS_SELECTOR,
                            "[data-testid='wcl-oddsValue']"
                        ).text.strip()
                    except:
                        ctx = None

                    if alias in ["under-over", "asian-handicap", "european-handicap"]:
                        market_line = ctx

                    elif alias == "correct-score":
                        selection_ctx = ctx

                    # -----------------------------
                    # 1x2: seleção por índice FIXA
                    # -----------------------------
                    for i, el in enumerate(elementos):

                        bookmaker_id = el.get_attribute("data-analytics-bookmaker-id")

                        if bookmaker_id not in BOOKMAP:
                            continue

                        col = BOOKMAP[bookmaker_id]

                        value = el.text.strip()

                        if not value or len(value) > 5:
                            continue

                        try:
                            odd_value = float(value)
                        except:
                            continue

                        selection = None

                        # -----------------------------
                        # SELEÇÃO CORRETA POR MERCADO
                        # -----------------------------
                        if alias == "1x2" and expected and i < len(expected):
                            selection = expected[i]

                        elif alias == "correct-score":
                            selection = selection_ctx

                        elif alias != "1x2":
                            # fallback genérico (caso necessário)
                            selection = None

                        # -----------------------------
                        # CHAVE FINAL (AGORA CORRETA)
                        # -----------------------------
                        key = (alias, market_line, selection)

                        if key not in buffer:
                            buffer[key] = {
                                "match_id": 1,
                                "market_type": alias,
                                "market_line": market_line,
                                "selection": selection,
                                "bet365": None,
                                "betano": None,
                                "estrela_bet": None,
                                "super_bet": None,
                                "one_xbet": None,
                                "extras": {}
                            }

                        obj = buffer[key]

                        obj[col] = odd_value

                all_rows = list(buffer.values())


            # ===========================
            # OUTPUT FINAL
            # ===========================

            for row in all_rows:
                print(row)

                                                        
                
            btnEstatisticas = bot.cliqueCSS("#detail > div.tabContent__match-summary > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")    
            
            
            desc="falha ao dados da classe partida"    

            bot.cliqueCSS("#detail > div.duelParticipant__container") 
            
            partida = Partidas()
            casa = Estatisticas()
            fora = Estatisticas()    
            InstanciarPartidaZerada(casa)
            InstanciarPartidaZerada(fora)

            partida = bot.recolher_Info_Partida(driver,tipoPartida)
            partida.Url_Partida=url
            casa = bot.recolher_Estatistica_Time_Base(driver,True)
            fora = bot.recolher_Estatistica_Time_Base(driver,False)
            casa.CasaOuFora='casa'
            fora.CasaOuFora='fora'
            
            casa.Gol_HT = Gol_HT.get("gol_casa")
            fora.Gol_HT = Gol_HT.get("gol_fora")

            if partida.Campeonato == "SÉRIE A" or partida.Campeonato == "BRASILEIRÃO SÉRIE B SUPERBET" : 
                isBrasileirao = driver.find_element(By.CSS_SELECTOR, "#detail > div.detail__breadcrumbs > nav > ol > li:nth-child(2) > a > span").text
                if isBrasileirao == "BRASIL" and partida.Campeonato == "SÉRIE A":
                    partida.Campeonato= "BRASILEIRÃO BETANO"
                elif  partida.Campeonato == "BRASILEIRÃO SÉRIE B SUPERBET":
                    partida.Campeonato= "SÉRIE B"


            casa.GolSofrido_HT=fora.Gol_HT
            fora.GolSofrido_HT=casa.Gol_HT
            casa.GolSofrido=fora.Gol
            fora.GolSofrido=casa.Gol


            
            # PartidaExistente = GetPartidabyNamesAndDate(casa.Nome,fora.Nome,partida.data)            
            # if PartidaExistente != 0: #aqui caso a partida ja tenha sido analisada anteriormente
            #     driver.quit()
            #     return PartidaExistente[0]
            
            
            # em jogos disputado por penaltis o site do flash score adiciona um gol para quem passa e isso altera 
            # a quantidade de gols feitos em tempo regulamentar q é o que é esperado pelas casas de aposta
            try:                                                #detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__fullTime
                penaltis=driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__status > span").text
                if penaltis!="ENCERRADO":
                    if casa.Gol>fora.Gol:
                        casa.Gol+= -1
                    else:
                        fora.Gol+= -1                    
            except:
                print("")
            
            

            # não busca informações em jogos amistosos ele n valem de nada
            if partida.Campeonato=="AMISTOSO INTERCLUBES":
                driver.quit()
                return
        

            desc="falha ao dados da classe Eststisticas Partida"           
            
                                                        #wcl-category_Ydwqh
                                                        
                                                        #detail > div.tabContent__match-summary
            rows=driver.find_elements(By.CLASS_NAME, "wcl-row_2oCpS")
            if len(rows)==0:
                rows = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="wcl-statistics"]'))
                    )

                    
            ft=0
            while  2>ft:
                bot.pressionar_tecla(Keys.ARROW_DOWN)
                bot.pressionar_tecla(Keys.ARROW_DOWN)

                ft+=1
                if ft>1:
                    tempo1=bot.cliqueCSS("#detail > div.tabContent__match-summary > div.tabContent__match-statistics > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a:nth-child(2) > button")

                
                for row in rows:
                    try:
                        bot.pressionar_tecla(Keys.ARROW_DOWN)

                        bot.Partida(driver, casa, True, ft,row)
                        bot.Partida(driver, fora, False, ft,row)

                    except Exception as e:
                        print("Erro ao extrair dados da partida:", e)
                
                bot.pressionar_tecla(Keys.HOME)

                        
                if casa.Posse_de_bola==0 and casa.Passes==0 or fora.Posse_de_bola==0 and fora.Passes==0  :
                    desc="Falha ao reconhecer dados da classe de estatisticas Partidas, Aparentemente uma variação nova ou partidas sem estatisticas"
                    driver.quit() 
                    raise           
                
            
            else:         
                ProcessarJogo(partida,casa,fora)              
                # partidaLida = GetPartidabyNamesAndDate(casa.Nome,fora.Nome,partida.data)
              
                # if partidaLida != 0: #aqui caso a partida ja tenha sido lida 
                #     driver.quit()
                #     return partidaLida[0]
                
                tentativa+=1
            driver.quit()
        except:  
            try:
                driver.quit()
            except:
                print("")
            if tentativa>1:
                bot.BackLogs(url,1,desc)
            else:
                print("Falha em Obter estatisticas")


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
    
    estatisticas.Posse_de_bola_HT = 0
    estatisticas.Total_Finalizacao_HT = 0
    estatisticas.Chances_claras_HT = 0
    estatisticas.Escanteios_HT = 0
    estatisticas.Bolas_na_trave_HT = 0
    estatisticas.Gols_de_cabeca_HT = 0
    estatisticas.Defesas_do_goleiro_HT = 0
    estatisticas.Impedimentos_HT = 0
    estatisticas.Faltas_HT = 0
    estatisticas.Cartoes_Amarelos_HT = 0
    estatisticas.Cartoes_Vermelhos_HT = 0
    estatisticas.Laterais_Cobrados_HT = 0
    estatisticas.Toques_na_area_adversaria_HT = 0
    estatisticas.Passes_HT = 0
    estatisticas.Passes_Totais_HT = 0
    estatisticas.Precisao_Passes_HT = 0
    estatisticas.Passes_no_terco_final_HT = 0
    estatisticas.Cruzamentos_HT = 0
    estatisticas.Desarmes_HT = 0
    estatisticas.Bolas_afastadas_HT = 0
    estatisticas.Interceptacoes_HT = 0
    return estatisticas

    
def get_or_create_market(buffer, key, base_obj):
    if key not in buffer:
        buffer[key] = base_obj
    return buffer[key]

def build_key(match_id, alias, market_line, selection):
    return (match_id, alias, market_line, selection)

def parse_market_values(alias, elementos):
    values = [
        e.text.strip()
        for e in elementos
        if len(e.text.strip()) <= 5
    ]

    return values

def extract_market_context(linha, alias):
    market_line = None
    selection = None

    try:
        if alias in ["under-over", "asian-handicap", "european-handicap"]:
            market_line = linha.find_element(
                By.CSS_SELECTOR,
                "[data-testid='wcl-oddsValue']"
            ).text

        elif alias == "correct-score":
            selection = linha.find_element(
                By.CSS_SELECTOR,
                "[data-testid='wcl-oddsValue']"
            ).text

    except:
        pass

    return market_line, selection


def build_market_object(alias, base_obj, elementos, BOOKMAP):
    obj = OddMarket()
    obj.match_id = base_obj["match_id"]
    obj.market_type = alias

    for elemento in elementos:

        bookmaker_id = elemento.get_attribute("data-analytics-bookmaker-id")

        if bookmaker_id not in BOOKMAP:
            continue

        col = BOOKMAP[bookmaker_id]

        value = elemento.text.strip()

        if len(value) > 5:
            continue

        try:
            setattr(obj, col, float(value))
        except:
            pass

    return obj

Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/botafogo-sp-2yRUzy5N/crb-QHa3bLrj/?mid=rXIPzJNb", "Teste") 
  
#Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/Yg2idzak/#/resumo-de-jogo/resumo-de-jogo", "Teste")   


