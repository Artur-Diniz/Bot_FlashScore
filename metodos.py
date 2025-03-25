from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from datetime import datetime



class automacao:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def pressionar_tecla(self, tecla):
        """
        Método para pressionar uma tecla específica.
        :param tecla: A tecla a ser pressionada (ex: Keys.END, Keys.ENTER, etc.)
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
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/a")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/span[1]/span")
            self.clique("/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[10]/a")
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
            return None


class RecolherEstatisticas(automacao):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def recolher_Partida(self,driver,tipoPartida, EstatisticasPartida ):
        if EstatisticasPartida==True:
            partida = Partidas()
        else:
            partida = Estatisticas()
            
        partida.NomeTimeCasa = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[4]/div[2]/div[3]/div[2]/a").text
        partida.NomeTimeFora = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[4]/div[4]/div[3]/div[1]/a").text
        nome = driver.find_element(By.XPATH, "//*[@id=\"detail\"]/div[3]/div/span[3]/a").text
        nomepart = nome.split(" - ")
        partida.Campeonato = nomepart[0].strip()
        partida.PartidaAnalise = True
        diajogo =str(driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]").text)
        partida.data = datetime.strptime(diajogo, "%d.%m.%Y %H:%M")
        partida.TipoPartida = tipoPartida
        
        return partida    
 
    
    def Partida(self,driver,contador,estatistica,casafora):
        
        texto = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[2]/strong").text 
       
        if texto == "Posse de bola":            
            estatistica.Posse_de_bola= self.atributo(driver,contador,casafora)            
        elif texto =="Total de finalizações":
            estatistica.Total_Finalizacao= self.atributo(driver,contador,casafora)
        elif texto =="Chutes Bloqueados":
            estatistica.Chutes_Bloqueados= self.atributo(driver,contador,casafora)
        elif texto =="Chances claras":
            estatistica.Chances_claras= self.atributo(driver,contador,casafora)
        elif texto =="Escanteios":
            estatistica.Escanteios= self.atributo(driver,contador,casafora)
        elif texto =="Bolas na trave":
            estatistica.Bolas_na_trave= self.atributo(driver,contador,casafora)
        elif texto =="Gols de cabeça":
            estatistica.Gols_de_cabeca= self.atributo(driver,contador,casafora)
        elif texto =="Defesas do goleiro":
            estatistica.Defesas_do_goleiro= self.atributo(driver,contador,casafora)
        elif texto =="Faltas":
            estatistica.Faltas= self.atributo(driver,contador,casafora)
        elif texto =="Impedimentos":
            estatistica.Impedimentos= self.atributo(driver,contador,casafora)
        elif texto =="Cartões Amarelos":
            estatistica.Cartoes_Amarelos= self.atributo(driver,contador,casafora)
        elif texto =="Cartões Vermelhos":
            estatistica.Cartoes_Vermelhos= self.atributo(driver,contador,casafora)
        elif texto =="Laterais Cobrados":
            estatistica.Laterais_Cobrados= self.atributo(driver,contador,casafora)
        elif texto =="Toques na área adversária":
            estatistica.Toques_na_area_adversaria= self.atributo(driver,contador,casafora)
        elif texto =="Passes no terço final":
            estatistica.Passes_no_terco_final= self.atributo_Concluidos(driver,contador,casafora)
        elif texto =="Cruzamentos":
            estatistica.Cruzamentos= self.atributo_Concluidos(driver,contador,casafora)
        elif texto =="Desarmes":
            estatistica.Desarmes= self.atributo_Concluidos(driver,contador,casafora)
        elif texto =="Bolas afastadas":
            estatistica.Bolas_afastadas= self.atributo(driver,contador,casafora)
        elif texto =="Interceptações":
            estatistica.Interceptacoes= self.atributo(driver,contador,casafora)
        elif texto == "Passes":
            estatistica.Passes= self.atributo_Concluidos(driver,contador,casafora)
            estatistica.Passes_Totais= self.atributo_Total(driver,contador,casafora)
            estatistica.Precisao_Passes= self.atributo_Porcentagem(driver,contador,casafora)

            

        return estatistica

    def atributo(self,driver, contador, timeCasa ):
        atributo=0
        if timeCasa==True:
            atributo =int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[1]/strong").text.rstrip("%"))
        else:
            atributo = int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[3]/strong").text.rstrip("%"))
            
        return atributo    
    

    def atributo_Concluidos(self,driver, contador, timeCasa ):
        atributo=0        
        if timeCasa==True:
            atributo = int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[1]/strong").text.split("(")[1].split("/")[0])
        else:
            atributo = int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[3]/strong").text.split("(")[1].split("/")[0])
        return atributo
    

    
    def atributo_Total(self,driver, contador, timeCasa ):
        atributo=0 
        if timeCasa==True: 
            texto=driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[1]/strong").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        else:
            texto=driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[3]/strong").text.split("(")[1].split("/")[1].rstrip(")")
            atributo = int(texto)
        return atributo
    
   
    def atributo_Porcentagem(self,driver, contador, timeCasa ):
        atributo=0        
        if timeCasa ==True:
            atributo = int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[1]/strong").text.split("(")[0].rstrip("% "))
        else:
            atributo = int(driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[10]/div[{contador}]/div[1]/div[3]/strong").text.split("(")[0].rstrip("% "))
            
        return atributo
    
