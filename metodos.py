from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from models.partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from datetime import datetime
from models.ErrosLogs import ErrosLogs
from API.EnviarBackLog import MandraBackLogs
import psutil
from time import sleep
from models.Node import ListaEncadeada


class automacao:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
    
    def pressionar_tecla(self, tecla):
        """
         A tecla a ser pressionada (ex: Keys.END, Keys.ENTER, etc.)
        """
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(tecla).perform()
        except Exception as e:
            print(f"Erro ao pressionar a tecla {tecla}: {e}")
    
    def digitar_texto(self, xpath, texto):
        try:
            # Localiza o elemento
            elemento = self.driver.find_element(By.XPATH, xpath)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)

            elemento = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            
            # Digita o texto no campo
            elemento.send_keys(texto)
            return elemento     
        except Exception as e:
            print(f"Erro ao digitar o texto '{texto}' no elemento com xpath '{xpath}': {e}")
            
    def digitar_textoCSS(self, CSS_SELECTOR, texto):
        try:
            # Localiza o elemento
            elemento = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)

            elemento = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
            )

            # Digita o texto no campo
            elemento.send_keys(texto)
            return elemento     
        except Exception as e:
            print(f"Erro ao digitar o texto '{texto}' no elemento com CSS_SELECTOR '{CSS_SELECTOR}': {e}")            
            

    def clique(self, xpath):
        """Método para clicar em um elemento usando seu XPath"""
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)

            elemento = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {xpath} ")
        return elemento     

    
    def cliqueCSS(self, cssSelector):
        """Método para clicar em um elemento usando seu cssSelector"""
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector)))
            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)

            elemento = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector))
            )
                
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {cssSelector} ")
            
        return elemento     
    
    
    def BackLogs(self, url:str,Page:int,descricao:str):
        
        erro = ErrosLogs()
        
        
        if Page==1:
            erro.emQualPageFoi="Obter_Estatisticas.py"        
        elif Page==2:
            erro.emQualPageFoi="Obter_Ultimos_jogos.py"
        elif Page==3:
            erro.emQualPageFoi="Home.py"
        elif Page==4:
            erro.emQualPageFoi="ObterJogosEspecificos.py"
        elif Page==5:
            erro.emQualPageFoi="EnviarEstatistica.py"
            
        erro.QualaUrl=url
        erro.OqueProvavelmenteAConteceu=descricao
        
        MandraBackLogs(erro)
        
    

class AutomacaoHomePage(automacao):
    
    

    def argentina(self):
        try:
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/a/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/a/span")
        except Exception as e: #/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/a/span
            print("Erro ao adicionar Argentina:", e) #
            
    def alemanha(self):
        try:
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/a/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/a/span")        
        except Exception as e:
            print("Erro ao adicionar alemanha:", e)
    def championship(self):
        try:#/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[83]/span[2]/span/svg
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[83]/a/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[83]/span[2]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[83]/a/span")        
        except Exception as e:
            print("Erro ao adicionar alemanha:", e)
            
    def portugal(self):
        try:
            self.pressionar_tecla(Keys.PAGE_DOWN)
            elemento_hover = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[134]/a"))
        )          
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[134]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[134]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[134]/a")    
        except Exception as e:
            print("Erro ao adicionar portugal:", )
            
    def turquia(self):
        try:
            self.pressionar_tecla(Keys.PAGE_DOWN)
            elemento_hover = self.wait.until(         
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[172]/a"))
        )               
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[172]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[172]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[172]/a")    
        except Exception as e:
            print("Erro ao adicionar portugal:", )
    
    def egito(self):
        try:
            self.pressionar_tecla(Keys.PAGE_DOWN)
            elemento_hover = self.wait.until(      
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[53]/a"))
        )               
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[53]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[53]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[53]/a")    
        except Exception as e:
            print("Erro ao adicionar portugal:", )
    
    
    def holanda(self):
        try:
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[127]/a")# cliaca na aba
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[127]/span[1]/span")# add liga
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[127]/a")# fecha aba
        except Exception as e:
            print("Erro ao adicionar holanda:", )
    
    def times(self):
        try:
                      
            self.clique("/html/body/div[8]/section/div[1]/input")
            self.digitar_texto("/html/body/div[8]/section/div[1]/input", "al ahly")# caixa de texto
            self.clique("/html/body/div[8]/section/div[2]/div/a[1]/div[4]/div")# add o time
            self.clique("/html/body/div[8]/section/div[1]/input")
            self.apagar() 
            
            self.digitar_texto("/html/body/div[8]/section/div[1]/input", "inter Miami")
            self.clique("/html/body/div[8]/section/div[2]/div/a[1]/div[4]/div")
            self.clique("/html/body/div[8]/section/div[1]/input")
            self.apagar() 
            
            self.digitar_texto("/html/body/div[8]/section/div[1]/input", "al-hilal")
            self.clique("/html/body/div[8]/section/div[2]/div/a[1]/div[4]/div")
            self.clique("/html/body/div[8]/section/div[1]/input")
            self.apagar() 
            
            self.clique("/html/body/div[8]/section/header/div/button")# fecha aba
        except Exception as e:
            print("Erro ao adicionar os times:", e )
    

        
    
    
    def apagar(self):
        try:

            cont=0
            while cont <100:
                self.pressionar_tecla(Keys.BACK_SPACE)
                cont= cont+1
        except Exception as e:
            print("Erro ao adicionar holanda:", )

class automacaoUltimosJogos(automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)    

    
    def recolherUltimasPartidas(self,driver, confrontoDireto):
        jogos = []
        rows_list = driver.find_elements("css selector", "div.rows")
        
        try:
            if confrontoDireto:
                linhas = rows_list[2]  # terceiro elemento
            else:
                linhas = rows_list[0]  # terceiro elemento
        except Exception as e:
            print(f"Ocorreu ao recloher url de das ultimás partidas: {e}")
            return []
        
        
        matches = linhas.find_elements("css selector", "a.h2h__row")

        for match in matches:
            url = match.get_attribute("href")
            jogos.append(url) 

        
        return  jogos
        
        
        

    # Retorna a nova URL (ou None se falhar)
    def recolher_Info_Partida(self,driver,tipoPartida):
        partida = Partidas()                                #detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a
        partida.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
        partida.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
        nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.detail__breadcrumbs > nav > ol > li:nth-child(3) > a > span").text
        nomepart = nome.split(" - ")
        partida.Campeonato = nomepart[0].strip()
        partida.PartidaAnalise = True
        diajogo =str(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__startTime > div").text)
        partida.data = datetime.strptime(diajogo, "%d.%m.%Y %H:%M")
        partida.TipoPartida = tipoPartida

        
        return partida 
    def aguardar_se_memoria_alta(self,limite_percent=80, tempo_espera=10):
        uso_ram = psutil.virtual_memory().percent
        if uso_ram >= limite_percent:
            print(f"[!] RAM em {uso_ram:.2f}% — aguardando {tempo_espera}s para liberar memória...")
            sleep(tempo_espera)
    
class RecolherEstatisticas(automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        
    def recolher_Info_Partida(self,driver,tipoPartida):
        partida = Partidas()                                #detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a
        partida.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
        partida.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
        nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.detail__breadcrumbs > nav > ol > li:nth-child(3) > a > span").text
        nomepart = nome.split(" - ")
        partida.Campeonato = nomepart[0].strip()
        partida.PartidaAnalise = True
        diajogo =str(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__startTime > div").text)
        partida.data = datetime.strptime(diajogo, "%d.%m.%Y %H:%M")
        partida.TipoPartida = tipoPartida

        
        return partida 
    def recolher_Estatistica_Time_Base(self,driver,CasaOufora ):
        Estatistica = Estatisticas()    
        if CasaOufora==True:                                        #detail > div.tabContent__match-summary > div.tabContent__match-statistics > div.sectionsWrapper > div:nth-child(1) > div:nth-child(2) > div.wcl-category_Ydwqh > div.wcl-value_XJG99.wcl-homeValue_3Q-7P > span                                            
            Estatistica.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
            Estatistica.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
            Estatistica.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(1)").text)            
        else :                                                                      
            Estatistica.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
            Estatistica.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text.lower().strip()
            Estatistica.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(3)").text)            

    
        return Estatistica    
 
    
    def Partida(self, driver, estatistica, casafora, temp,  row):
        try:
            texto = row.find_element(By.CSS_SELECTOR, '[data-testid="wcl-statistics-category"]').text

            valores = row.find_elements(By.CSS_SELECTOR, '[data-testid="wcl-statistics-value"]')
            valor = valores[0].text if casafora else valores[1].text

            stat_map = {
                "Posse de bola": ("Posse_de_bola", "atributo"),
                "Total de finalizações": ("Total_Finalizacao", "atributo"),
                "Chutes Bloqueados": ("Chutes_Bloqueados", "atributo"),
                "Chances claras": ("Chances_claras", "atributo"),
                "Escanteios": ("Escanteios", "atributo"),
                "Bolas na trave": ("Bolas_na_trave", "atributo"),
                "Gols de cabeça": ("Gols_de_cabeca", "atributo"),
                "Defesas do goleiro": ("Defesas_do_goleiro", "atributo"),
                "Faltas": ("Faltas", "atributo"),
                "Impedimentos": ("Impedimentos", "atributo"),
                "Cartões amarelos": ("Cartoes_Amarelos", "atributo"),
                "Cartões vermelhos": ("Cartoes_Vermelhos", "atributo"),
                "Laterais Cobrados": ("Laterais_Cobrados", "atributo"),
                "Toques dentro da área adversária": ("Toques_na_area_adversaria", "atributo"),
                "Passes no terço final": ("Passes_no_terco_final", "atributo_Concluidos"),
                "Cruzamentos": ("Cruzamentos", "atributo_Concluidos"),
                "Desarmes": ("Desarmes", "atributo_Concluidos"),
                "Interceptações": ("Interceptacoes", "atributo"),
                "Passes": ("Passes", "special")
            }
            if texto in stat_map:
                attr, func = stat_map[texto]
                attr += "_HT" if temp == 2 else ""

                if func == "special":
                    spans = valores[0].find_elements(By.CSS_SELECTOR, '[data-testid="wcl-scores-simple-text-01"]') if casafora else valores[1].find_elements(By.CSS_SELECTOR, '[data-testid="wcl-scores-simple-text-01"]')

                    try:
                        precisao = spans[0].text.replace("%", "")
                        passes = spans[1].text.replace("(", "").replace(")", "")

                        passes_conc, passes_tot = passes.split("/")

                        passes_conc = int(passes_conc)
                        passes_tot = int(passes_tot)
                        precisao = int(precisao)

                    except Exception as e:
                        print("Erro ao tratar passes:", spans, "| erro:", e)
                        passes_conc, passes_tot, precisao = 0, 0, 0
                    sufixo = "_HT" if temp == 2 else ""

                    setattr(estatistica, f"Passes{sufixo}", passes_conc)
                    setattr(estatistica, f"Passes_Totais{sufixo}", passes_tot)
                    setattr(estatistica, f"Precisao_Passes{sufixo}", precisao)

                else:
                    try:
                        valor_limpo = valor.strip().replace(",", ".")

                        # separa quando vem com quebra de linha
                        if "\n" in valor_limpo:
                            parte1, parte2 = valor_limpo.split("\n")

                            # parte1 → "70%"
                            # parte2 → "(68/97)"

                            if "%" in parte1:
                                valor_limpo = parte1.replace("%", "")
                            elif "/" in parte2:
                                valor_limpo = parte2.replace("(", "").replace(")", "")

                        valor_limpo = valor_limpo.replace("%", "")

                        if func == "atributo_Concluidos":
                            valor_tratado = int(valor_limpo.split("/")[0])

                        else:
                            if "." in valor_limpo:
                                valor_tratado = float(valor_limpo)
                                if valor_tratado.is_integer():
                                    valor_tratado = int(valor_tratado)
                            else:
                                valor_tratado = int(valor_limpo)

                    except Exception as e:
                        print("Erro ao tratar valor:", valor, "| erro:", e)
                        valor_tratado = 0

                    setattr(estatistica, attr, valor_tratado)

        except Exception as e:
                        print("Erro no Partida:", e)

        return estatistica

    def atributo(self,driver, timeCasa,variacao, sessao,linha ):
        atributo=0                                           
        if timeCasa==True:                                     #detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong
            atributo =int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > strong ").text.rstrip("%"))
        else:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > strong").text.rstrip("%"))
        self.pressionar_tecla(Keys.ARROW_DOWN)
        return atributo    
    

    def atributo_Concluidos(self,driver, timeCasa,variacao, sessao,linha ):
        atributo=0        
        if timeCasa==True:       
            texto = (driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > span").text).split("/")[0].strip("(").strip(")")
            atributo = int(texto)
        else:    
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span").text.split("/")[0].strip("(").strip(")")
            atributo = int(texto)
        return atributo
        ##detail > div:nth-child(13) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span
    
    def atributo_Total(self,driver, timeCasa,variacao, sessao,linha ):
        atributo=0 
        if timeCasa==True: 
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > span ").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        else:
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        return atributo
    
   
    def atributo_Porcentagem(self,driver, timeCasa,variacao, sessao,linha ):
        atributo=0        
        if timeCasa ==True:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > strong ").text.rstrip("%").rstrip(" "))
        else:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > strong").text.rstrip("%").rstrip(" "))
            
        return atributo
    
    def Sumario(self,driver):
        eventos = ListaEncadeada()
        
        self.pressionar_tecla(Keys.PAGE_DOWN)
        
        events = driver.find_elements(By.CLASS_NAME, "smv__incident")

        for event in events:#
            #smv__timeBox
            tempo=0
            try:
                tempo = event.find_element(By.CLASS_NAME, "smv__timeBox").text
            except:
                continue

            jogador=""
            try:
                jogador = event.find_element(By.CLASS_NAME, "smv__playerName").text
            except:
                continue
            descricao=""
            try:
                try:
                    try:
                        try:#
                            descricao = event.find_element(By.CLASS_NAME, "#smv__incidentSubOut smv__incidentSideAway").text
                        except:
                            descricao = event.find_element(By.CLASS_NAME, "smv__assist ").text
                    except:
                        descricao = event.find_element(By.CLASS_NAME, "smv__subIncident").text                
                except:
                        descricao = event.find_element(By.CLASS_NAME, "smv__subDown smv__playerName").text                
            except:
                continue                
            if descricao=='':
                continue
                
            descricao.rstrip("(").rstrip(")")
            tipos_eventos = [
                ("cartão amarelo", "card-ico yellowCard-ico"),#card-ico yellowCard-ico
                # ("substituição", "substitution"),
                ("gol", "smv__incidentHomeScore"),
                ("gol", "smv__incidentAwayScore"), 
                ("cartão vermelho", "card-ico redCard-ico")
            ]
            
            # Verifica cada tipo de evento
            for nome_evento, classe in tipos_eventos:
                if " " in classe:
                    seletor_css = f"svg.{'.'.join(classe.split())}"
                    elementos = event.find_elements(By.CSS_SELECTOR, seletor_css)
                else:
                    elementos = event.find_elements(By.CLASS_NAME, classe)


                for elemento in elementos:
                    eventos.adicionar({"tipo": nome_evento, "texto": elemento.text, "tempo": tempo,"jogador": jogador,"descricao": descricao} )
                
        self.pressionar_tecla(Keys.PAGE_UP)
        
        return self.recolherGolHt(eventos)
                #card-ico yellowCard-ico 
                #substitution 
                #smv__incidentHomeScore
                #smv__incidentAwayScore
    
    def recolherGolHt(self,sumario:ListaEncadeada):
        resultado = {
            "gol_casa": 0,
            "gol_fora": 0
        }

        ultimo_placar = (0, 0)  # começa 0x0

        for event in sumario:
            if event.get('tipo') == 'gol':
                tempo = event.get('tempo', '')
                if "'" in tempo:
                    tempo_limpo = tempo.replace("'", "")
                    if '+' in tempo_limpo:
                        minutos = int(tempo_limpo.split('+')[0])
                    else:
                        minutos = int(tempo_limpo)

                    if minutos <= 45:
                        placar = event.get('texto', '')
                        if ' - ' in placar:
                            gols_casa, gols_fora = map(int, placar.split(' - '))

                            if gols_casa > ultimo_placar[0]:
                                resultado["gol_casa"] += 1
                            elif gols_fora > ultimo_placar[1]:
                                resultado["gol_fora"] += 1

                            ultimo_placar = (gols_casa, gols_fora)

        return resultado


