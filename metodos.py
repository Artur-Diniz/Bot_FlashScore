from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from models.EstatisticaTimes import EstatisticasTimes
from datetime import datetime
from models.ErrosLogs import ErrosLogs
from API.EnviarBackLog import MandraBackLogs


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
    
    def digitar_texto(self, seletor, texto):
        try:
            # Localiza o elemento
            elemento = self.driver.find_element(By.XPATH, seletor)

            # Digita o texto no campo
            elemento.send_keys(texto)
        except Exception as e:
            print(f"Erro ao digitar o texto '{texto}' no elemento com seletor '{seletor}': {e}")

    def clique(self, xpath):
        """Método para clicar em um elemento usando seu XPath"""
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {xpath} ")
    
    def cliqueCSS(self, cssSelector):
        """Método para clicar em um elemento usando seu cssSelector"""
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector)))
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {cssSelector} ")
    
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
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/[10]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/[10]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/[10]/a")
        except Exception as e:
            print("Erro ao adicionar Argentina:", e)
            
    def alemanha(self):
        try:
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/a/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[4]/a/span")        
        except Exception as e:
            print("Erro ao adicionar alemanha:", e)
            
    def portugal(self):
        try:
            self.pressionar_tecla(Keys.PAGE_DOWN)
            elemento_hover = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[140]/a"))
        )
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[140]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[140]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[140]/a")    
        except Exception as e:
            print("Erro ao adicionar portugal:", )
    
    
    def holanda(self):
        try:
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[133]/a")# cliaca na aba
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[133]/span[1]/span")# add liga
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[133]/a")# fecha aba
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
    
    def reconhecerUltimosJogos(self, count, linha):
        driver = self.driver
        original_url = driver.current_url
        new_url = None  # Variável para armazenar a nova URL
        
        # Tentativas de clique em diferentes seletores CSS
        selectors = [
            f"#detail > div:nth-child(5) > div > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({linha})",
            f"#detail > div:nth-child(6) > div > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({linha})",
            f"#detail > div:nth-child(7) > div > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({linha})",
            f"#detail > div:nth-child(8) > div > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({linha})"
        ]
        
        clicked = False
        for selector in selectors:
            try:
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
                clicked = True
                break
            except:
                continue
        
        if not clicked:
            print("Não foi possível clicar em nenhum dos elementos")
            return None  # Retorna None se não conseguir clicar

        try:
            # Espera por nova janela ou mudança de URL
            WebDriverWait(driver, 3).until(
                lambda d: len(d.window_handles) > 1 or d.current_url != original_url
            )
            
            if len(driver.window_handles) > 1:
                # Se abriu nova janela, muda para ela e pega a URL
                for window in driver.window_handles:
                    if window != driver.current_window_handle:
                        driver.switch_to.window(window)
                        new_url = driver.current_url  # Armazena a nova URL
                        break
            else:
                # Se mudou a URL, armazena antes de voltar
                if driver.current_url != original_url:
                    new_url = driver.current_url  # Guarda a URL nova
                    driver.back()  # Volta para a original
                    self.wait.until(lambda d: d.current_url == original_url)
                    
        except Exception as e:
            print(f"Ocorreu um erro após o clique: {e}")
            return None

        return new_url 
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
    
class RecolherEstatisticas(automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        
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
    def recolher_Estatistica_Time_Base(self,driver,CasaOufora ):
        Estatistica = Estatisticas()    
        if CasaOufora==True:                                                
            Estatistica.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
            Estatistica.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
            Estatistica.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(1)").text)            
        else :                                                                      
            Estatistica.NomeRival = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
            Estatistica.Nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow > a").text
            Estatistica.Gol=int(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant__container > div.duelParticipant > div.duelParticipant__score > div > div.detailScore__wrapper > span:nth-child(3)").text)            

    
        return Estatistica    
 
    
    def Partida(self,driver,estatistica,casafora,variacao,sessao,linha):
        if linha==2 and sessao==2: 
            self.cliqueCSS(f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")
 #           texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({sessao}) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong").text                              
                            
        texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child(2) > div:nth-child({sessao}) > div:nth-child({linha}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong").text                              
            
        try:
            if texto == "Posse de bola" and estatistica.Posse_de_bola==0:            
                estatistica.Posse_de_bola= self.atributo(driver,casafora,variacao,sessao,linha) 
                        
            elif texto =="Total de finalizações" and estatistica.Total_Finalizacao==0:
                estatistica.Total_Finalizacao= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Chutes Bloqueados" and estatistica.Chutes_Bloqueados==0:
                estatistica.Chutes_Bloqueados= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Chances claras" and estatistica.Chances_claras==0:
                estatistica.Chances_claras= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Escanteios" and estatistica.Escanteios==0:
                estatistica.Escanteios= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Bolas na trave" and estatistica.Bolas_na_trave==0:
                estatistica.Bolas_na_trave= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Gols de cabeça" and estatistica.Gols_de_cabeca==0:
                estatistica.Gols_de_cabeca= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Defesas do goleiro" and estatistica.Defesas_do_goleiro==0:
                estatistica.Defesas_do_goleiro= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Faltas" and estatistica.Faltas==0:
                estatistica.Faltas= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Impedimentos" and estatistica.Impedimentos==0:
                estatistica.Impedimentos= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Cartões Amarelos" and estatistica.Cartoes_Amarelos==0:
                estatistica.Cartoes_Amarelos= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Cartões Vermelhos" and estatistica.Cartoes_Vermelhos:
                estatistica.Cartoes_Vermelhos= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Laterais Cobrados" and estatistica.Laterais_Cobrados==0:
                estatistica.Laterais_Cobrados= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Toques na área adversária" and estatistica.Toques_na_area_adversaria==0:
                estatistica.Toques_na_area_adversaria= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Passes no terço final" and  estatistica.Passes_no_terco_final==0:
                estatistica.Passes_no_terco_final= self.atributo_Concluidos(driver,casafora,variacao,sessao,linha)
            elif texto =="Cruzamentos" and estatistica.Cruzamentos==0:
                estatistica.Cruzamentos= self.atributo_Concluidos(driver,casafora,variacao,sessao,linha)
            elif texto =="Desarmes" and estatistica.Desarmes==0:
                estatistica.Desarmes= self.atributo_Concluidos(driver,casafora,variacao,sessao,linha)
            elif texto =="Bolas afastadas" and estatistica.Bolas_afastadas==0:
                estatistica.Bolas_afastadas= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto =="Interceptações" and estatistica.Interceptacoes==0:
                estatistica.Interceptacoes= self.atributo(driver,casafora,variacao,sessao,linha)
            elif texto == "Passes" and estatistica.Passes==0:
                estatistica.Passes= self.atributo_Concluidos(driver,casafora,variacao,sessao,linha)
                estatistica.Passes_Totais= self.atributo_Total(driver,casafora,variacao,sessao,linha)
                estatistica.Precisao_Passes= self.atributo_Porcentagem(driver,casafora,variacao,sessao,linha)
        except: 
            print("")
   
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
    

class AnalisadorEstatisticoAvancado:
    @staticmethod
    def calcular_medias_contextuais(partidas_casa: list, 
                                  partidas_fora: list, 
                                  confrontos_diretos: list) -> EstatisticasTimes:
        estatisticas = EstatisticasTimes()
        
        # 1. Médias do time jogando EM CASA (contra vários adversários)
        if partidas_casa:
            estatisticas = AnalisadorEstatisticoAvancado._calcular_medias(
                partidas_casa, estatisticas, sufixo='')
        
        # 2. Médias do time jogando FORA (contra vários adversários)
        if partidas_fora:
            # Aqui armazenamos como "Adversaria" pois é o desempenho do time quando visita
            estatisticas = AnalisadorEstatisticoAvancado._calcular_medias(
                partidas_fora, estatisticas, sufixo='_Adversaria')
        
        # 3. Médias específicas de confrontos diretos
        if confrontos_diretos:
            estatisticas = AnalisadorEstatisticoAvancado._calcular_medias(
                confrontos_diretos, estatisticas, sufixo='_Confronto')
        
        return estatisticas
    
    @staticmethod
    def _calcular_medias(partidas: list, estatisticas: EstatisticasTimes, sufixo: str) -> EstatisticasTimes:
        atributos = [attr for attr in dir(EstatisticasTimes()) 
                    if not attr.startswith('__') 
                    and not attr.endswith(('_Adversaria', '_Confronto'))
                    and attr != 'Id']
        
        for attr in atributos:
            attr_alvo = attr + sufixo
            valores = [getattr(p, attr) for p in partidas if hasattr(p, attr)]
            
            if valores:
                # Calcula média ponderada pelo nível do adversário (opcional)
                media = sum(valores) / len(valores)
                setattr(estatisticas, attr_alvo, round(media, 2))
        
        return estatisticas

    @staticmethod
    def validar_dados(partidas: list, contexto: str) -> bool:
        """Verifica se os dados são consistentes para análise"""
        if not partidas:
            print(f"Aviso: Sem dados para {contexto}")
            return False
            
        # Verifica se há variação suficiente nos adversários
        adversarios = set([p.nome_adversario for p in partidas])
        if len(adversarios) < 3 and len(partidas) >= 3:
            print(f"Aviso: Pouca variação de adversários em {contexto}")
            return False
            
        return True

