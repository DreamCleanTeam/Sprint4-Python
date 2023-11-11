import requests
import json
from datetime import datetime

def conexao_Arduino():
    url = "http://46.17.108.113:1026/v2/entities/urn:ngsi-ld:DreamClean:008/attrs/distance"

    payload = {}
    headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/',
    'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        data = response.json()

        # Extrai e imprime o valor da chave "value"
        value = data.get("value")
        print("Valor:", value)

        # Recebe o valor do request e armazena na variável timeInstant
        timeInstant = data.get("metadata",{}).get("TimeInstant",{}).get("value")
        
        # Converte a string para um objeto datetime
        data = datetime.strptime(timeInstant, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Formata o objeto datetime para um formato mais legível
        dataFormatada = data.strftime("%d/%m/%Y %H:%M:%S")

        print("Data e hora:", dataFormatada)
    else:
        print("Erro na solicitação:", response.status_code)


conexao_Arduino()