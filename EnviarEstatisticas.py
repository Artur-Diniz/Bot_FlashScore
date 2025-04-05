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
import requests

def mandarDados(estatisticasCasa,estatisticasFora,partida):
    url = "http://Junglernauti819.somee.com/botFlashScore/Estatistica/"  
    
    estatisticaCasa = {
        "Id": 0,
        "CasaOuFora": estatisticasCasa.CasaOuFora,
        "Nome": estatisticasCasa.Nome,
        "Gol": estatisticasCasa.Nome,
        "GolSofrido": estatisticasCasa.GolSofrido,
        "Posse_de_bola": estatisticasCasa.Posse_de_bola,
        "Total_Finalizacao": estatisticasCasa.Total_Finalizacao,
        "Chances_claras": estatisticasCasa.Chances_claras,
        "Escanteios": estatisticasCasa.Escanteios,
        "Bolas_na_trave": estatisticasCasa.Bolas_na_trave,
        "Gols_de_cabeca": estatisticasCasa.Gols_de_cabeca,
        "Defesas_do_goleiro": estatisticasCasa.Defesas_do_goleiro,
        "Impedimentos": estatisticasCasa.Impedimentos,
        "Faltas": estatisticasCasa.Faltas,
        "Cartoes_Amarelos": estatisticasCasa.Cartoes_Amarelos,
        "Cartoes_Vermelhos": estatisticasCasa.Cartoes_Vermelhos,
        "Laterais_Cobrados": estatisticasCasa.Laterais_Cobrados,
        "Toques_na_area_adversaria": estatisticasCasa.Toques_na_area_adversaria,
        "Passes": estatisticasCasa.Passes,
        "Passes_Totais": estatisticasCasa.Passes_Totais,
        "Precisao_Passes": estatisticasCasa.Precisao_Passes,
        "Passes_no_terco_final": estatisticasCasa.Passes_no_terco_final,
        "Cruzamentos": estatisticasCasa.Cruzamentos,
        "Desarmes": estatisticasCasa.Desarmes,
        "Bolas_afastadas": estatisticasCasa.Bolas_afastadas,
        "Interceptacoes": estatisticasCasa.Interceptacoes,
        
        "Id": 0,
        "Id_EstatisticaCasa": 0,
        "Id_EstatisticaFora": 0,
        "NomeTimeCasa": partida.NomeTimeCasa,  
        "NomeTimeFora": partida.NomeTimeFora,
        "DataPartida": partida.data,
        "Campeonato": partida.Campeonato,
        "PartidaAnalise": False,
        "TipoPartida": partida.TipoPartida
    }
    
    estatisticaFora = {
        "Id": 0,
        "CasaOuFora": estatisticasFora.CasaOuFora,
        "Nome": estatisticasFora.Nome,
        "Gol": estatisticasFora.Nome,
        "GolSofrido": estatisticasFora.GolSofrido,
        "Posse_de_bola": estatisticasFora.Posse_de_bola,
        "Total_Finalizacao": estatisticasFora.Total_Finalizacao,
        "Chances_claras": estatisticasFora.Chances_claras,
        "Escanteios": estatisticasFora.Escanteios,
        "Bolas_na_trave": estatisticasFora.Bolas_na_trave,
        "Gols_de_cabeca": estatisticasFora.Gols_de_cabeca,
        "Defesas_do_goleiro": estatisticasFora.Defesas_do_goleiro,
        "Impedimentos": estatisticasFora.Impedimentos,
        "Faltas": estatisticasFora.Faltas,
        "Cartoes_Amarelos": estatisticasFora.Cartoes_Amarelos,
        "Cartoes_Vermelhos": estatisticasFora.Cartoes_Vermelhos,
        "Laterais_Cobrados": estatisticasFora.Laterais_Cobrados,
        "Toques_na_area_adversaria": estatisticasFora.Toques_na_area_adversaria,
        "Passes": estatisticasFora.Passes,
        "Passes_Totais": estatisticasFora.Passes_Totais,
        "Precisao_Passes": estatisticasFora.Precisao_Passes,
        "Passes_no_terco_final": estatisticasFora.Passes_no_terco_final,
        "Cruzamentos": estatisticasFora.Cruzamentos,
        "Desarmes": estatisticasFora.Desarmes,
        "Bolas_afastadas": estatisticasFora.Bolas_afastadas,
        "Interceptacoes": estatisticasFora.Interceptacoes,
        
        "Id": 0,
        "Id_EstatisticaCasa": 0,
        "Id_EstatisticaFora": 0,
        "NomeTimeCasa": partida.NomeTimeCasa,  
        "NomeTimeFora": partida.NomeTimeFora,
        "DataPartida": partida.data,
        "Campeonato": partida.Campeonato,
        "PartidaAnalise": False,
        "TipoPartida": partida.TipoPartida
    }
    
    Partida = {
        "Id": 0,
        "Id_EstatisticaCasa": 0,
        "Id_EstatisticaFora": 0,
        "NomeTimeCasa": partida.NomeTimeCasa,  
        "NomeTimeFora": partida.NomeTimeFora,
        "DataPartida": partida.data,
        "Campeonato": partida.Campeonato,
        "PartidaAnalise": False,
        "TipoPartida": partida.TipoPartida
    }
    

    EstatisticaPartida = {
        "estatisticaCasa": estatisticaCasa,
        "estatisticaFora": estatisticaFora,
        "partida": Partida
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=EstatisticaPartida, headers=headers)
    print("o id recebido é esse aqui veinho", response.json(), "  \n informação recebida com sucesso bora pra Proxima!")


partida=Partidas()

estatisticasCasa = Estatisticas()
estatisticasFora = Estatisticas()
mandarDados(estatisticasCasa,estatisticasFora,partida)
