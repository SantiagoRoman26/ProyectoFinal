import sys
from TextAPI import traducirTexto 
from VozAPI import getAudioDeTexto, getTextoDeVoz, getVozPorIdiomaGeneroPersona
from playsound import playsound

idiomaEntrada = "es-MX"
#idiomaEntrada = "en-US"
#idiomaSalida = "es-MX"
idiomaSalida = "en-US"
#generoVoz = "Femenino"
generoVoz = "Masculino"
NOMBRE_ARCHIVO = 'audio.wav'

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
