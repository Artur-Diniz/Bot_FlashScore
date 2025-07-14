
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from selenium.webdriver.support import expected_conditions as EC
import json
import requests
from datetime import datetime
from models.Node import criar_lista_encadeada,imprimir_lista_encadeada
from models.Palpites import Palpites

def converter_json_para_Palpites(dados_api):
    partidas_analisadas = []
    
    for item in dados_api:
        IdPartida = item.get("idPartida", 0)
                
        partidas_analisadas.append(IdPartida)
    
    return partidas_analisadas


def GetPartidasPassadas( ) :  
    url = "http://Junglernauti819.somee.com/botFlashScore/"  
     
    PalpitesAnalise = []

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url+"Palpite/GetPalpitesEmAndamento", headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
            PalpitesAnalise= converter_json_para_Palpites(data)
           
        else:
            print("❌ Erro ao Solicitar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
    return PalpitesAnalise
   
def id_Partidasemprocesso():
# Obter os palpites
    palpites = GetPartidasPassadas()


    # Criar lista encadeada com os ids
    lista_encadeada = criar_lista_encadeada(palpites)

    # Exibir lista encadeada
    imprimir_lista_encadeada(lista_encadeada)
    
#id_Partidasemprocesso()
