import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)
from models.Partidas import Partidas

import json
import requests
from datetime import datetime

def converter_json_para_partidas(dados_api):
    partidas_analisadas = []
    
    for item in dados_api:
        partida = Partidas()
        partida.Id_Partida = item.get("id", 0)
        partida.NomeTimeCasa = item.get("nomeTimeCasa", "")
        partida.NomeTimeFora = item.get("nomeTimeFora", "")
        partida.Url_Partida = item.get("url_Partida", "")
        
        # Convertendo a data (com tratamento de erro)
        try:
            partida.data = datetime.strptime(item["dataPartida"], "%Y-%m-%dT%H:%M:%S")
        except (KeyError, ValueError):
            partida.data = datetime.today()
        
        partida.Campeonato = item.get("campeonato", "")
        partida.PartidaAnalise = item.get("partidaAnalise", False)
        partida.TipoPartida = item.get("tipoPartida", "")
        
        partidas_analisadas.append(partida)
    
    return partidas_analisadas




def GerarestatisticaEsperadas(Id_Partida:int, url: str):

    headers = {"Content-Type": "application/json"}#http://localhost:5194/EstatisticaEsperadas/GerarEstatisticasEsperadas/

    response = requests.post(url+f"EstatisticaEsperadas/GerarEstatisticasEsperadas/{Id_Partida}", headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            print(data)
        except json.JSONDecodeError:
            print("Resposta bruta:", response.text)        
        
        return "solcitado e enviado corretamente"
        
    else:
        print("❌ Erro ao Solicitar dados:")
        print("Status Code:", response.status_code)
        print("Motivo:", response.reason)
        print("Resposta do servidor:", response.text)
        return "Erro ao fazer Solicitação"
    
def GerarPartidaEstatisticaEsperadas(Id_Partida:int, url: str):

    headers = {"Content-Type": "application/json"}#http://localhost:5194/PartidaEstatisticaEsperadas/GerarEstatisticasEsperadas/

    response = requests.post(url+f"PartidaEstatisticaEsperadas/GerarEstatisticasEsperadas/{Id_Partida}", headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            print(data)
        except json.JSONDecodeError:
            print("Resposta bruta:", response.text)        
        
        return "solcitado e enviado corretamente"
        
    else:
        print("❌ Erro ao Solicitar dados:")
        print("Status Code:", response.status_code)
        print("Motivo:", response.reason)
        print("Resposta do servidor:", response.text)
        return "Erro ao fazer Solicitação"


def GerarEstatisticaIA( ) :  
    url = "http://Junglernauti819.somee.com/botFlashScore/"  
     
    partidas_analisadas = []

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url+"Partida/PartidasAnalisadas", headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print(data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
            partidas_analisadas= converter_json_para_partidas(data)
        else:
            print("❌ Erro ao Solicitar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
    for partida in partidas_analisadas:
        
  
        resposta=''
        id_partida=0
        id_partida=partida.Id_Partida
        print(f"foi solicitado para gerar a estatisticas esperadas da partida: {id_partida}"  )        
        
        resposta = GerarestatisticaEsperadas(id_partida, url)
        if resposta =="solcitado e enviado corretamente":            
            print(resposta)
            resposta = GerarPartidaEstatisticaEsperadas(id_partida, url)
            if resposta == " solcitado e enviado corretamente ":            
                print(resposta)            
        elif resposta =="Erro ao fazer Solicitação": 
            print(resposta +"\npassando para Proxima partida")
        
        
        
#GerarEstatisticaIA()
