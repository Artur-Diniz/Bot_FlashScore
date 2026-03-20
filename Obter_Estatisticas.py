from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metodos import RecolherEstatisticas
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from API.EnviarEstatisticas import mandarDadosPartida,mandarDadosPartidaAnalisada
from time import sleep
import psutil
from selenium.webdriver.chrome.options import Options
import random

import time

def  Obter_Estatisticas(url:str, tipoPartida:str):
    
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
            
                       
            #Gols_ht = bot.Sumario(driver)


            
            desc="falhou ao pressionar botão de estatisticas, pode ser que seja um jogo sem estatisticas, ou pode ser um jogo com mais uma variação"    
            # btnEstatistica=0
            bot.pressionar_tecla(Keys.DOWN)                
            bot.pressionar_tecla(Keys.DOWN)          
            sleep(2)   
                
            btnEstatisticas = bot.cliqueCSS("#detail > div.tabContent__match-summary > div.filterOver.filterOver--indent > div > a:nth-child(2) > button")    
            
            # try:            #detail > div:nth-child(5) > div.filterOver.filterOver--indent > div > a:nth-child(2) > button
               
                  
                
            #     if  btnEstatisticas.text=="ESTATÍSTICAS" or  btnEstatisticas.text=="Estatísticas":
            #         btnEstatistica=1
            #     else:
            #             driver.quit() 
            #             raise
            # except:
            #     driver.quit() 
            #     raise



            # if btnEstatistica==0:
            #     driver.quit()       
            #     raise 
                
            
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
            casa.CasaOuFora='Casa'
            fora.CasaOuFora='Fora'
            
            # casa.Gol_HT = Gols_ht.get("gol_casa")
            # fora.Gol_HT = Gols_ht.get("gol_fora")

            casa.GolSofrido_HT=fora.Gol_HT
            fora.GolSofrido_HT=casa.Gol_HT
            casa.GolSofrido=fora.Gol
            fora.GolSofrido=casa.Gol
            
            
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
            variacao=0
            sessao=0
            linha=0
            while  2>ft:
                bot.pressionar_tecla(Keys.ARROW_DOWN)
                bot.pressionar_tecla(Keys.ARROW_DOWN)

                ft+=1
                if ft>1:
                    tempo1=bot.cliqueCSS("#detail > div.tabContent__match-summary > div.tabContent__match-statistics > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a:nth-child(2) > button")

                    
                # for row in rows:              

                #     try:
                #                 # Tenta encontrar o <strong> dentro da linha
                #         full_path = driver.execute_script("""
                #             function getDivPath(element) {
                #                 let path = [];
                #                 while (element !== document.body && element.parentNode) {
                #                     if (element.tagName.toLowerCase() === 'div') {
                #                         let index = Array.from(element.parentNode.children)
                #                             .filter(el => el.tagName.toLowerCase() === 'div')
                #                             .indexOf(element) + 1;
                #                         path.unshift(`div:nth-child(${index})`);
                #                     }
                #                     element = element.parentNode;
                #                 }
                #                 return path.join(" > ");
                #             }
                #             return getDivPath(arguments[0]);
                #         """, row)

                #         # Exemplo de full_path: (era pra ser assim porém pode mudar com o tempo)

                #         # "div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)"

                #         parts = full_path.split(" > ")
                #         # variacao = int(parts[6].split("(")[1].replace(")", "") if len(parts) > 0 else "N/A")
                #         sessao = int(parts[9].split("(")[1].replace(")", "") if len(parts) > 1 else "N/A")
                #         linha = int(parts[10].split("(")[1].replace(")", "") if len(parts) > 3 else "N/A")
                #     except Exception as e:
                #         # print(f"Erro ao processar linha: {e}")
                #         continue 

                #     bot.pressionar_tecla(Keys.DOWN)
                    
                    
                #     # if sessao == 2 and linha == 2: #detail > div:nth-child(5) > div:nth-child(2) > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button           
                #     #     bot.cliqueCSS(f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")        
                    
                #     # texto = ""                                            
                #     # try:                                                #detail > div.tabContent__match-summary > div.tabContent__match-statistics > div.sectionsWrapper > div:nth-child(1) > div:nth-child(2) > div.wcl-category_Ydwqh > div.wcl-category_6sT1J > span
                #     #     texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div.tabContent__match-summary > div.tabContent__match-statistics > div.sectionsWrapper > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_Ydwqh > div.wcl-category_6sT1J > span").text                              
                #     #     if linha == 2 and texto == 'Gols esperados (xG)':
                #     #         continue
                #     # except:
                #     #     print("Não está reconhecendo a linha")    
                    
                #     bot.pressionar_tecla(Keys.ARROW_DOWN)       

                #     try:
                #         bot.Partida(driver,casa,True,ft,variacao,sessao,linha),
                #         bot.Partida(driver,fora,False,ft,variacao,sessao,linha)                    
                #     except:
                #         print("Erro ao extrair dados da partida")
                
                for row in rows:
                    try:
                        bot.pressionar_tecla(Keys.ARROW_DOWN)

                        bot.Partida(driver, casa, True, ft, variacao, row)
                        bot.Partida(driver, fora, False, ft, variacao, row)

                    except Exception as e:
                        print("Erro ao extrair dados da partida:", e)
                
                bot.pressionar_tecla(Keys.HOME)

                        
                if casa.Posse_de_bola==0 and casa.Passes==0 or fora.Posse_de_bola==0 and fora.Passes==0  :
                    desc="Falha ao reconhecer dados da classe de estatisticas Partidas, Aparentemente uma variação nova ou partidas sem estatisticas"
                    driver.quit() 
                    raise           
                
            
            else:            
                if tipoPartida=="Analisada":
                    mandarDadosPartidaAnalisada(casa,fora,partida)
                else:
                    mandarDadosPartida(casa,fora,partida)
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

    
 
Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/mirassol-pQ8ryEe7/palmeiras-hMn9FTbH/?mid=WQmXs9qR", "Teste") 
  
#Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/Yg2idzak/#/resumo-de-jogo/resumo-de-jogo", "Teste")   



