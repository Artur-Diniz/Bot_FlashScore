
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from models.ErrosLogs import ErrosLogs
from selenium.webdriver.support import expected_conditions as EC
from models.ErrosLogs import ErrosLogs 
import json
import requests
import os
from datetime import datetime

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

def ReceberLogs():
    url = "http://Junglernauti819.somee.com/botFlashScore/ErrosLogs/GetAll"  
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logs = response.json()  # Supondo que 'logs' seja uma lista de dicionários
        salvar_logs_por_data(logs)
        print("✅ Logs salvos em 'erros_consolidado.txt'!")
    else:
        print(f"❌ Erro na API: {response.status_code}")

def salvar_logs_por_data(logs):    
    logs_por_data = {}
    for log in logs:
        # Se seus logs já têm um campo 'data', use: data = log['data'].split('T')[0]
        # Caso contrário, usamos a data atual:
        data = datetime.now().strftime("%Y-%m-%d")  # Formato: ANO-MÊS-DIA
        
        if data not in logs_por_data:
            logs_por_data[data] = []
        logs_por_data[data].append(log)
    
    # Salva um arquivo por data
    for data, logs_dia in logs_por_data.items():
        caminho_arquivo = os.path.join("LOG", f"erros_{data}.txt")
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            for log in logs_dia:
                linha = json.dumps(log, ensure_ascii=False)
                file.write(linha + "\n \n \n ")



# ReceberLogs()
