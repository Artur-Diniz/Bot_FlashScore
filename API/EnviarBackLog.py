
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from models.ErrosLogs import ErrosLogs
from selenium.webdriver.support import expected_conditions as EC
from models.ErrosLogs import ErrosLogs 
import json
import requests
import os
from datetime  import datetime, timezone

def MandraBackLogs( Erros:ErrosLogs) :
    #acertar a URL dps pois ainda n criei o metodo na api
    url = "http://Junglernauti819.somee.com/botFlashScore/ErrosLogs/"  
    
    hora_erro = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z")

       
    ErrosLogs = {
        "Id": 0,
        "QualPageFoi": Erros.emQualPageFoi,  # Nome exato da coluna no SQL
        "QualUrl": Erros.QualaUrl,
        "horaErro": hora_erro,  # Formato: "2025-05-10T20:30:45.123Z"
        "OqueProvavelmenteAConteceu": Erros.OqueProvavelmenteAConteceu
    }

    # 3. Configuração da requisição
    url = "http://Junglernauti819.somee.com/botFlashScore/ErrosLogs/"  
    headers = {"Content-Type": "application/json"}

    # 4. Envie e trate erros
    try:
        response = requests.post(url, json=ErrosLogs, headers=headers)
        response.raise_for_status()  # Lança erro se status != 200-299
        print("✅ Log enviado com sucesso!")
        print("Resposta do servidor:", response.json())
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro HTTP {e.response.status_code}: {e.response.text}")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
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



#ReceberLogs()
