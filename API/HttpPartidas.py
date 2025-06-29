
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from selenium.webdriver.support import expected_conditions as EC
from API.GerarEstatisticasEsperdas import converter_json_para_partidas
import json
import requests
from datetime import datetime



def GetPartidasPassadas( ) :  
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
        
    return partidas_analisadas
   

