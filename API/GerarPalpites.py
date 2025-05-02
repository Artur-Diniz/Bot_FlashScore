
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


def SolicitarPalpites( ) :
    #acertar a URL dps pois ainda n criei o metodo na api
    url = "http://Junglernauti819.somee.com/botFlashScore/Palpite/Gerar_Palpites"  
     
    
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                print("✅DEU BOM AI OS PALPITES SÃO : ", data)
            except json.JSONDecodeError:
                print("Resposta bruta:", response.text)
        else:
            print("❌ Erro ao enviar dados:")
            print("Status Code:", response.status_code)
            print("Motivo:", response.reason)
            print("Resposta do servidor:", response.text)
    except requests.RequestException as e:
        print("❌ Erro de requisição:", e)

def ReceberOsPalpites():
    url = "http://Junglernauti819.somee.com/botFlashScore/Palpite/GetAll"  
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        palpites = response.json()  # Supondo que 'logs' seja uma lista de dicionários
        salvar_Palpites_do_dia(palpites)
        print("✅ Palpites salvos em 'Palpites.txt'!")
    else:
        print(f"❌ Erro na API: {response.status_code}")

def salvar_Palpites_do_dia(Palpite):    
    Palpites_Dia = {}
    for palpites in Palpite:
        data = datetime.now().strftime("%Y-%m-%d")  # Formato: ANO-MÊS-DIA
        
        if data not in Palpites_Dia:
            Palpites_Dia[data] = []
        Palpites_Dia[data].append(palpites)
    
    for data, logs_dia in Palpites_Dia.items():
        caminho_arquivo = os.path.join("Palpites", "Palpites.txt")
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            for palpites in logs_dia:
                linha = json.dumps(palpites, ensure_ascii=False)
                file.write(linha + "\n \n \n ")


# SolicitarPalpites( )

#ReceberOsPalpites()

def GerarRelatorio():
    url = "http://Junglernauti819.somee.com/botFlashScore/Partida/Relatorio"  
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        Relatorio = response.json()  # Supondo que 'logs' seja uma lista de dicionários
        print(Relatorio)
        return Relatorio
    else:
        print(f"❌ Erro na API: {response.status_code}")
    
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     palpites = response.json()  # Supondo que 'logs' seja uma lista de dicionários
    #     salvar_Palpites_do_dia(palpites)
    #     print("✅ Palpites salvos em 'Palpites.txt'!")

GerarRelatorio()
