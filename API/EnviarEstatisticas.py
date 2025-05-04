
import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from metodos import RecolherEstatisticas
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas
from models.Partida_Estatistica_Dto import PartidaCompletaDto
import json
import requests

def mandarDados( estatisticasCasa: Estatisticas,estatisticasFora: Estatisticas, partida: Partidas) :
    url = "http://Junglernauti819.somee.com/botFlashScore/Estatistica/Partida"  
    #url = "http://localhost:5194/Estatistica/Partida"  
    
    
    estatisticaCasa = {
        "Id": 0,
        "CasaOuFora": estatisticasCasa.CasaOuFora,
        "NomeTime": estatisticasCasa.Nome,
        "NomeTimeRival": estatisticasCasa.NomeRival,
        "Gol": estatisticasCasa.Gol,
        "GolSofrido": estatisticasCasa.GolSofrido,
        "Posse_bola": estatisticasCasa.Posse_de_bola,
        "Total_Finalizacao": estatisticasCasa.Total_Finalizacao,
        "Chances_claras": estatisticasCasa.Chances_claras,
        "Escanteios": estatisticasCasa.Escanteios,
        "bolas_trave": estatisticasCasa.Bolas_na_trave,
        "gols_de_cabeça": estatisticasCasa.Gols_de_cabeca,
        "defesas_Goleiro": estatisticasCasa.Defesas_do_goleiro,
        "Impedimentos": estatisticasCasa.Impedimentos,
        "Faltas": estatisticasCasa.Faltas,
        "cartoes_Amarelos": estatisticasCasa.Cartoes_Amarelos,
        "cartoes_Vermelhos": estatisticasCasa.Cartoes_Vermelhos,
        "Laterais_Cobrados": estatisticasCasa.Laterais_Cobrados,
        "toque_area_adversaria": estatisticasCasa.Toques_na_area_adversaria,
        "Passes": estatisticasCasa.Passes,
        "Passes_Totais": estatisticasCasa.Passes_Totais,
        "Precisao_Passes": estatisticasCasa.Precisao_Passes,
        "passes_terco_Final": estatisticasCasa.Passes_no_terco_final,
        "Cruzamentos": estatisticasCasa.Cruzamentos,
        "Desarmes": estatisticasCasa.Desarmes,
        "Bolas_afastadas": estatisticasCasa.Bolas_afastadas,
        "Interceptacoes": estatisticasCasa.Interceptacoes,
        "TipoPartida":partida.TipoPartida,
        
        "gol_HT": estatisticasCasa.Gol_HT,
        "golSofrido_HT": estatisticasCasa.GolSofrido_HT,
        "posse_Bola_HT": estatisticasCasa.Posse_de_bola_HT,
        "total_Finalizacao_HT": estatisticasCasa.Total_Finalizacao_HT,
        "chances_Claras_HT": estatisticasCasa.Chances_claras_HT,
        "escanteios_HT": estatisticasCasa.Escanteios_HT,
        "bolas_trave_HT": estatisticasCasa.Bolas_na_trave_HT,
        "gols_de_cabeça_HT": estatisticasCasa.Gols_de_cabeca_HT,
        "defesas_Goleiro_HT": estatisticasCasa.Defesas_do_goleiro_HT,
        "impedimentos_HT": estatisticasCasa.Impedimentos_HT,
        "faltas_HT": estatisticasCasa.Faltas_HT,
        "cartoes_Amarelos_HT": estatisticasCasa.Cartoes_Amarelos_HT,
        "cartoes_Vermelhos_HT": estatisticasCasa.Cartoes_Vermelhos_HT,
        "laterais_Cobrados_HT": estatisticasCasa.Laterais_Cobrados_HT,
        "toque_Area_Adversaria_HT": estatisticasCasa.Toques_na_area_adversaria_HT,
        "passes_HT": estatisticasCasa.Passes_HT,
        "passes_Totais_HT": estatisticasCasa.Passes_Totais_HT,
        "precisao_Passes_HT": estatisticasCasa.Precisao_Passes_HT,
        "passes_terco_Final_HT": estatisticasCasa.Passes_no_terco_final_HT,
        "cruzamentos_HT": estatisticasCasa.Cruzamentos_HT,
        "desarmes_HT": estatisticasCasa.Desarmes_HT,
        "bolas_Afastadas_HT": estatisticasCasa.Bolas_afastadas_HT,
        "interceptacoes_HT": estatisticasCasa.Interceptacoes_HT,

    }
    
    estatisticaFora = {
        "Id": 0,
        "CasaOuFora": estatisticasFora.CasaOuFora,
        "NomeTime": estatisticasFora.Nome,
        "NomeTimeRival": estatisticasFora.NomeRival,
        "Gol": estatisticasFora.Gol,
        "GolSofrido": estatisticasFora.GolSofrido,
        "Posse_bola": estatisticasFora.Posse_de_bola,
        "Total_Finalizacao": estatisticasFora.Total_Finalizacao,
        "Chances_claras": estatisticasFora.Chances_claras,
        "Escanteios": estatisticasFora.Escanteios,
        "Bolas_na_trave": estatisticasFora.Bolas_na_trave,
        "Gols_de_cabeca": estatisticasFora.Gols_de_cabeca,
        "defesas_Goleiro": estatisticasFora.Defesas_do_goleiro,
        "Impedimentos": estatisticasFora.Impedimentos,
        "Faltas": estatisticasFora.Faltas,
        "cartoes_Amarelos": estatisticasFora.Cartoes_Amarelos,
        "cartoes_Vermelhos": estatisticasFora.Cartoes_Vermelhos,
        "Laterais_Cobrados": estatisticasFora.Laterais_Cobrados,
        "toque_Area_Adversaria": estatisticasFora.Toques_na_area_adversaria,
        "Passes": estatisticasFora.Passes,
        "Passes_Totais": estatisticasFora.Passes_Totais,
        "Precisao_Passes": estatisticasFora.Precisao_Passes,
        "passes_terco_Final": estatisticasFora.Passes_no_terco_final,
        "Cruzamentos": estatisticasFora.Cruzamentos,
        "Desarmes": estatisticasFora.Desarmes,
        "Bolas_afastadas": estatisticasFora.Bolas_afastadas,
        "Interceptacoes": estatisticasFora.Interceptacoes,
        "TipoPartida":partida.TipoPartida,        
        "CasaOuFora": estatisticasFora.CasaOuFora,

        "gol_HT": estatisticasFora.Gol_HT,
        "golSofrido_HT": estatisticasFora.GolSofrido_HT,
        "posse_Bola_HT": estatisticasFora.Posse_de_bola_HT,
        "total_Finalizacao_HT": estatisticasFora.Total_Finalizacao_HT,
        "chances_Claras_HT": estatisticasFora.Chances_claras_HT,
        "escanteios_HT": estatisticasFora.Escanteios_HT,
        "bolas_trave_HT": estatisticasFora.Bolas_na_trave_HT,
        "gols_de_cabeça_HT": estatisticasFora.Gols_de_cabeca_HT,
        "defesas_Goleiro_HT": estatisticasFora.Defesas_do_goleiro_HT,
        "impedimentos_HT": estatisticasFora.Impedimentos_HT,
        "faltas_HT": estatisticasFora.Faltas_HT,
        "cartoes_Amarelos_HT": estatisticasFora.Cartoes_Amarelos_HT,
        "cartoes_Vermelhos_HT": estatisticasFora.Cartoes_Vermelhos_HT,
        "laterais_Cobrados_HT": estatisticasFora.Laterais_Cobrados_HT,
        "toque_Area_Adversaria_HT": estatisticasFora.Toques_na_area_adversaria_HT,
        "passes_HT": estatisticasFora.Passes_HT,
        "passes_Totais_HT": estatisticasFora.Passes_Totais_HT,
        "precisao_Passes_HT": estatisticasFora.Precisao_Passes_HT,
        "passes_terco_Final_HT": estatisticasFora.Passes_no_terco_final_HT,
        "cruzamentos_HT": estatisticasFora.Cruzamentos_HT,
        "desarmes_HT": estatisticasFora.Desarmes_HT,
        "bolas_Afastadas_HT": estatisticasFora.Bolas_afastadas_HT,
        "interceptacoes_HT": estatisticasFora.Interceptacoes_HT,
      

    }
    
    Partida = {
        "Id": 0,
        "Id_EstatisticaCasa": 0,
        "Id_EstatisticaFora": 0,
        "NomeTimeCasa": estatisticasCasa.Nome,  
        "NomeTimeFora": estatisticasFora.Nome,
        "Url_Partida": partida.Url_Partida,
        "DataPartida": partida.data.isoformat(),
        "Campeonato": partida.Campeonato,
        "PartidaAnalise": False,
        "TipoPartida": partida.TipoPartida
    }
    
    EstatisticaPartida= PartidaCompletaDto()

    EstatisticaPartida = {
        "estatisticaCasa": estatisticaCasa,
        "estatisticaFora": estatisticaFora,
        "partida": Partida
    }

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=EstatisticaPartida, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Dados enviados com sucesso! ID:", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)

    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        




def gerarEstatiscasMedias(casa,fora):
    urlcasa=f"http://Junglernauti819.somee.com/botFlashScore/EstatisticaTimes/GerarEstatistica/{casa}" 
    try:
        response = requests.post(urlcasa)

        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Dados enviados com sucesso! ID:", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)

    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
        
    urlfora=f"http://Junglernauti819.somee.com/botFlashScore/EstatisticaTimes/GerarEstatistica/{fora}" 
    try:
        response = requests.post(urlfora)

        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Dados enviados com sucesso! ID:", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)

    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
def mandarPartidaAnalise(partida: Partidas) :
    url = "http://Junglernauti819.somee.com/botFlashScore/Partida/"  
    
    Partida = {
        "Id": 0,
        "Id_EstatisticaCasa": 0,
        "Id_EstatisticaFora": 0,
        "NomeTimeCasa": partida.NomeTimeCasa,  
        "NomeTimeFora": partida.NomeTimeFora,
        "DataPartida": partida.data.isoformat(),
        "Campeonato": partida.Campeonato,
        "PartidaAnalise": True,
        "TipoPartida": partida.TipoPartida
    }
    
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=Partida, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Dados enviados com sucesso! ID:", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)

    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
        
#gerarEstatiscasMedias("Juventude","Mirassol")