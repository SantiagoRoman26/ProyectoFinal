import sys
from TextAPI import traducirTexto 
from VozAPI import getAudioDeTexto, getTextoDeVoz, getVozPorIdiomaGeneroPersona
from playsound import playsound
from os import remove
import keyboard

#idiomaEntrada = "es-MX"
#idiomaEntrada = "en-US"
#idiomaSalida = "es-MX"
#idiomaSalida = "en-US"
#generoVoz = "Femenino"
generoVoz = "Masculino"
NOMBRE_ARCHIVO = 'audiosd.wav'
detener=""
while (detener == ""):
	idiomaEntrada = "es-MX"
	idiomaSalida = "en-US"
	mensajeCaptado = getTextoDeVoz()
	print(mensajeCaptado)
	mensajeTraducido = traducirTexto(mensajeCaptado, idiomaEntrada, idiomaSalida)
	if mensajeCaptado == mensajeTraducido:
		idiomaEntrada="en-US"
		idiomaSalida = "es-MX"
		mensajeTraducido = traducirTexto(mensajeCaptado, idiomaEntrada, idiomaSalida)       
	print(mensajeTraducido)

	nombreAgente = getVozPorIdiomaGeneroPersona(idiomaSalida,generoVoz)
	getAudioDeTexto(mensajeTraducido, nombreAgente, idiomaSalida)

	playsound(NOMBRE_ARCHIVO)
	remove(NOMBRE_ARCHIVO)
