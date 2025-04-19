from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from models.ErrosLogs import ErrosLogs
import json
import requests

def MandraBackLogs( Erros:ErrosLogs) :
    #acertar a URL dps pois ainda n criei o metodo na api
    url = "http://Junglernauti819.somee.com/botFlashScore/ErrosLogs/"  
    
    ErrosLogs = {
        "Id": 0,
        "qualPageFoi": Erros.emQualPageFoi,
        "qualUrl": Erros.QualaUrl,
        "OqueProvavelmenteAConteceu": Erros.OqueProvavelmenteAConteceu       
    }
    
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=ErrosLogs, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print("❌DEU MERDA VE AI A CAGADA O ID É:", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
            
        # url=url+"GetAll"
        # response = requests.get(url, json=ErrosLogs, headers=headers)
        # print(response) 
        # data = response.json()
        # print("✅ Dados enviados com sucesso! ID:", data)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)
        

# erro =ErrosLogs()

# erro.emQualPageFoi="aaa"
# erro.QualaUrl="aaa.com.br"
# erro.OqueProvavelmenteAConteceu="sei la ve ai "
# MandraBackLogs(erro)