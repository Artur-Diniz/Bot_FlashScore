import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

import json
import requests
from Obter_Estatisticas import Obter_Estatisticas



def GerarestatisticaEsperadas(url: str):

    headers = {"Content-Type": "application/json"}

    response = requests.get(url+"Partida/PartidasAnalisadas/", headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Resposta bruta:", response.text)        
        
        for item in data:
            partida =item.get("url_Partida", "")
            if partida!= "":
                Obter_Estatisticas(partida,"Partida_Anterior")
           
        return "solcitado e enviado corretamente"
        
    else:
        print("❌ Erro ao Solicitar dados:")
        print("Status Code:", response.status_code)
        print("Motivo:", response.reason)
        print("Resposta do servidor:", response.text)
        return "Erro ao fazer Solicitação"

#GerarestatisticaEsperadas("http://Junglernauti819.somee.com/botFlashScore/")