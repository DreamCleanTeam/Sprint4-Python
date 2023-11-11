import requests
import json
from datetime import datetime

def conexao_Arduino():
    url = "http://46.17.108.113:1026/v2/entities/urn:ngsi-ld:DreamClean:008/attrs"

    payload = {}
    headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/',
    'accept': 'application/json'
    }

    responseWeight = requests.request("GET", url + "/weight", headers=headers, data=payload)
    responseDistance = requests.request("GET", url + "/distance", headers=headers, data=payload)


    if responseWeight.status_code == 200 and responseDistance.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dataWeight = responseWeight.json()
        dataDistance = responseDistance.json()


        #### Armazena o valor do weight (peso) ####
        weight = dataWeight.get("value")
        
        #### Armazena o valor da distância (volume) ####
        distance = dataDistance.get("value")


        ### Armazena o valor da data e hora da última checagem ####
        timeInstant = dataDistance.get("metadata",{}).get("TimeInstant",{}).get("value")
        
        # Converte a string para um objeto datetime
        data = datetime.strptime(timeInstant, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Formata o objeto datetime para um formato mais legível
        dataFormatada = data.strftime("%d/%m/%Y %H:%M:%S")

        
        #Retorna os valores de distância, peso e data
        return distance, weight, dataFormatada
    else:
        print("Erro na solicitação:", responseDistance.status_code)
        print("Erro na solicitação:", responseWeight.status_code)