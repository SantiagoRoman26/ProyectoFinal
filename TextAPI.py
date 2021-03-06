import os, requests, time 
from xml.etree import ElementTree
import uuid, json

suscripcionTexto = "f1924689359a4e1bbb9fa2022c794a6f"

def traducirTexto(texto, idiomaInicial, idiomaFinal):
    
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to='+idiomaFinal
    constructed_url = base_url + path + params
    headers = {
        'Ocp-Apim-Subscription-Key': suscripcionTexto,
         'Ocp-Apim-Subscription-Region': 'westeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text' : texto
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = json.loads(str(request.text))
    return (response[0]['translations'][0]['text'])
