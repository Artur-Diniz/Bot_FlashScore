
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from selenium.webdriver.support import expected_conditions as EC
import json
import requests
from datetime import datetime
from models.Palpites import Palpites


def converter_json_para_Palpites(dados_api):
    Palpites_EmAndamentos = []
    
    for item in dados_api:
        urlPartidaPassadas = item.get("id", "")
                
        Palpites_EmAndamentos.append(urlPartidaPassadas)
    
    return Palpites_EmAndamentos


def GetPalpitesPassados() :  
    url = "http://Junglernauti819.somee.com/botFlashScore/"  
     
    Id_palpites = []

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url+"Palpite/GetPalpitesEmAndamento", headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
            Id_palpites= converter_json_para_Palpites(data)
           
        else:
            print("❌ Erro ao Solicitar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
    return Id_palpites
   
GetPalpitesPassados()

def UpdatePalpites(id):
    url = "http://Junglernauti819.somee.com/botFlashScore/"  
     

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.put(url+f"Palpite/ConfirmarPalpites/{id}", headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print(data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
       
           
        else:
            print("❌ Erro ao Solicitar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        
    return 

#pdatePalpites(3)



def analisando_Palpite():
    Palpites_emAndamento = GetPalpitesPassados() 

    for id in Palpites_emAndamento:
        UpdatePalpites(id)
