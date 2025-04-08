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



class automacao:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
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
            print(f"Erro ao clicar no elemento {xpath}: {e}")
    
    def cliqueCSS(self, cssSelector):
        """Método para clicar em um elemento usando seu cssSelector"""
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector)))
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {cssSelector}: {e}")
    

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
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[3]/div/div[2]") # abre aba
            
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

class automacaoUltimosJogos (automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def reconhecerUltimosJogos(self, count, contador): #aqui eu tercerizei o método de clicar no ultimo jogos de cada time
                                                       # pois vou usar em outra pagina pra n ter q repetir esse tranbolho
        try:
            driver = self.driver  
            original_window = driver.current_window_handle

            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"#detail > div.h2hSection > div.h2h > div:nth-child({count}) > div.rows > div:nth-child({contador})")
            )).click()

            self.wait.until(lambda driver: len(driver.window_handles) > 1)
            for window in driver.window_handles:
                if window != original_window:
                    driver.switch_to.window(window)
                    break

            current_url = driver.current_url
            driver.close()
            driver.switch_to.window(original_window)
            return current_url

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return ''


   
        
    
class RecolherEstatisticas(automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def recolher_Partida(self,driver,tipoPartida, EstatisticasPartida ):
        if EstatisticasPartida==True:
            partida = Partidas()
        else:
            partida = Estatisticas()
            
        partida.NomeTimeCasa = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__home > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow").text
        partida.NomeTimeFora = driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__away > div.participant__participantNameWrapper > div.participant__participantName.participant__overflow").text
        nome = driver.find_element(By.CSS_SELECTOR, "#detail > div.detail__breadcrumbs > nav > ol > li:nth-child(3) > a").text
        nomepart = nome.split(" - ")
        partida.Campeonato = nomepart[0].strip()
        partida.PartidaAnalise = True
        diajogo =str(driver.find_element(By.CSS_SELECTOR, "#detail > div.duelParticipant > div.duelParticipant__startTime > div").text)
        partida.data = datetime.strptime(diajogo, "%d.%m.%Y %H:%M")
        partida.TipoPartida = tipoPartida

        
        return partida    
 
    
    def Partida(self,driver,contador,estatistica,casafora,variacao):
        if contador==2: 
            self.cliqueCSS("#detail > div.subFilterOver.subFilterOver--indent.subFilterOver--radius > div > a.active > button")
                                                        ##detail > div:nth-child(8) > div:nth-child(2) > div.wcl-category_ITphf > div.wcl-category_7qsgP > strong
        texto = driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-category_7qsgP > Strong").text                              
            
        try:
            if texto == "Posse de bola" and estatistica.Posse_de_bola==0:            
                estatistica.Posse_de_bola= self.atributo(driver,contador,casafora,variacao) 
                        
            elif texto =="Total de finalizações" and estatistica.Total_Finalizacao==0:
                estatistica.Total_Finalizacao= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Chutes Bloqueados" and estatistica.Chutes_Bloqueados==0:
                estatistica.Chutes_Bloqueados= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Chances claras" and estatistica.Chances_claras==0:
                estatistica.Chances_claras= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Escanteios" and estatistica.Escanteios==0:
                estatistica.Escanteios= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Bolas na trave" and estatistica.Bolas_na_trave==0:
                estatistica.Bolas_na_trave= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Gols de cabeça" and estatistica.Gols_de_cabeca==0:
                estatistica.Gols_de_cabeca= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Defesas do goleiro" and estatistica.Defesas_do_goleiro==0:
                estatistica.Defesas_do_goleiro= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Faltas" and estatistica.Faltas==0:
                estatistica.Faltas= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Impedimentos" and estatistica.Impedimentos==0:
                estatistica.Impedimentos= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Cartões Amarelos" and estatistica.Cartoes_Amarelos==0:
                estatistica.Cartoes_Amarelos= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Cartões Vermelhos" and estatistica.Cartoes_Vermelhos:
                estatistica.Cartoes_Vermelhos= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Laterais Cobrados" and estatistica.Laterais_Cobrados==0:
                estatistica.Laterais_Cobrados= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Toques na área adversária" and estatistica.Toques_na_area_adversaria==0:
                estatistica.Toques_na_area_adversaria= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Passes no terço final" and  estatistica.Passes_no_terco_final==0:
                estatistica.Passes_no_terco_final= self.atributo_Concluidos(driver,contador,casafora,variacao)
            elif texto =="Cruzamentos" and estatistica.Cruzamentos==0:
                estatistica.Cruzamentos= self.atributo_Concluidos(driver,contador,casafora,variacao)
            elif texto =="Desarmes" and estatistica.Desarmes==0:
                estatistica.Desarmes= self.atributo_Concluidos(driver,contador,casafora,variacao)
            elif texto =="Bolas afastadas" and estatistica.Bolas_afastadas==0:
                estatistica.Bolas_afastadas= self.atributo(driver,contador,casafora,variacao)
            elif texto =="Interceptações" and estatistica.Interceptacoes==0:
                estatistica.Interceptacoes= self.atributo(driver,contador,casafora,variacao)
            elif texto == "Passes" and estatistica.Passes==0:
                estatistica.Passes= self.atributo_Concluidos(driver,contador,casafora,variacao)
                estatistica.Passes_Totais= self.atributo_Total(driver,contador,casafora,variacao)
                estatistica.Precisao_Passes= self.atributo_Porcentagem(driver,contador,casafora,variacao)
        except: 
            print("")
   
        return estatistica

    def atributo(self,driver, contador, timeCasa ,variacao):
        atributo=0                                           
        if timeCasa==True:                                  
            atributo =int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > strong ").text.rstrip("%"))
        else:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > strong").text.rstrip("%"))
        self.pressionar_tecla(Keys.ARROW_DOWN)
        return atributo    
    

    def atributo_Concluidos(self,driver, contador, timeCasa,variacao ):
        atributo=0        
        if timeCasa==True:       
            texto = (driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > span").text).split("/")[0].strip("(").strip(")")
            atributo = int(texto)
        else:    
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span").text.split("/")[0].strip("(").strip(")")
            atributo = int(texto)
        return atributo
        ##detail > div:nth-child(13) > div:nth-child(3) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span
    
    def atributo_Total(self,driver, contador, timeCasa,variacao ):
        atributo=0 
        if timeCasa==True: 
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > span ").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        else:
            texto=driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > span").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        return atributo
    
   
    def atributo_Porcentagem(self,driver, contador, timeCasa,variacao ):
        atributo=0        
        if timeCasa ==True:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-homeValue_-iJBW > strong ").text.rstrip("%").rstrip(" "))
        else:
            atributo = int(driver.find_element(By.CSS_SELECTOR, f"#detail > div:nth-child({variacao}) > div:nth-child({contador}) > div.wcl-category_ITphf > div.wcl-value_IuyQw.wcl-awayValue_rQvxs > strong").text.rstrip("%").rstrip(" "))
            
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

