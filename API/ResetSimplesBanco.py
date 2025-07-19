
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from selenium.webdriver.support import expected_conditions as EC
import json
import requests



def DeleteBaseAPI(caminho:str) :  
    url = "http://Junglernauti819.somee.com/botFlashScore/"  
     
    partidas_analisadas = []
    url=url+caminho
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print(data)
            except json.JSONDecodeError:
                print("Resposta do Servidor : ", response.text)
        else:
            print("❌ Erro ao Solicitar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
    return partidas_analisadas
   

def ResetSimplesDatabase():
    print("================ Resetando Tabelas Temporarias ================")
    print("Apagando tabela temporaria de Estatistica")
    DeleteBaseAPI("Estatistica/Apague")
    print("Apagando tabela temporaria de EstatisticaTimes")
    DeleteBaseAPI("EstatisticaTimes/Apague")
    print("Apagando tabela temporaria de Partidas")
    DeleteBaseAPI("Partida/Apague")
    print("================ Tabelas Apagadas Com Sucesso ================")
    

#ResetSimplesDatabase()