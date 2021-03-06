import azure.cognitiveservices.speech as speechsdk
import os, requests, time 
from xml.etree import ElementTree
import uuid, json

suscripcionVoz = "e0e9508dd52542cf8ffa4a27dceec35b"

def getTextoDeVoz():
    """
    #Asignacion de parametros de la licencia y el idioma
    regionVoz = "eastus"
    speech_config = speechsdk.SpeechConfig(subscription=suscripcionVoz, region=regionVoz, speech_recognition_language= idiomaVoz)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Escuchando...")

    #Realiza reconocimiento. 
    #Recognize_once (), para una sola emision.
    #start_continuous_recognition (), para varias emisiones de sonido.

    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    """

    regionVoz = "eastus"
    speech_config = speechsdk.SpeechConfig(subscription=suscripcionVoz, region=regionVoz)
    auto_detect_source_language_config = \
        speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["es-MX", "en-US"])
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, auto_detect_source_language_config=auto_detect_source_language_config)
    print("Escuchando...")
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
        #print("Recognized: {} in language {}".format(result.text, auto_detect_source_language_result.language))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No se reconocio el idioma.")


def getAudioDeTexto(texto, nombreAgente, idioma):
    
    timestr = time.strftime("%Y%m%d-%H%M")
    access_token = get_token()

    base_url = 'https://eastus.tts.speech.microsoft.com/'
    path = 'cognitiveservices/v1'
    constructed_url = base_url + path
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'User-Agent': 'SpeechInterprete'
    }
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', idioma)
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', idioma)
    pathAgente = 'Microsoft Server Speech Text to Speech Voice (' + idioma + ', ' + nombreAgente + ')'
    voice.set('name', pathAgente)
    voice.text = texto
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)
    if response.status_code == 200:
        with open('audiosd' + '.wav', 'wb') as audio:
            audio.write(response.content)
            print("\nStatus code: " + str(response.status_code) + "\nEl audio esta listo.\n")
    else:
        print("\nStatus code: " + str(response.status_code) + "\nHay un error con las cabeceras de las licencias.\n")


def getVozPorIdiomaGeneroPersona(idioma, genero):
    if(idioma=='es-MX'):
        if(genero=='Femenino'):
            return "HildaRUS"
        else:
            return "Raul, Apollo"
    else:
        if(genero=='Femenino'):
            return "JessaRUS"
        else:
            return "BenjaminRUS"

def get_token():
    fetch_token_url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    headers = {
        'Ocp-Apim-Subscription-Key': suscripcionVoz
    }
    response = requests.post(fetch_token_url, headers=headers)
    return str(response.text)