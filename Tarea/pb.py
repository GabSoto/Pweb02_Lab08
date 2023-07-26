# API for DNI

from urllib.request import urlopen
import json
'''
dni = 72088685

url = "https://dniruc.apisperu.com/api/v1/dni/"+ dni +"?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdhYnJpZWxzb3RvY2NveWFAZ21haWwuY29tIn0.BRxBA3nIZYvMzKNpljaAdICLSUa7UoGpgp7_I3qCQec"

response = urlopen(url)
data = json.loads(response.read())

state = data["succes"]
dni = data["dni"]
nombres = data["nombres"]
AP_paterno = data["apellidoPaterno"]
AP_materno = data["apellidoMaterno"]
'''
# Cadena con secuencia de escape Unicode
cadena_unicode_escapada = "PE\u00d1A"

# Al imprimir, Python interpreta automáticamente la secuencia de escape y muestra PEÑA
print(cadena_unicode_escapada.encode('utf-8'))  # Salida: PEÑA

# Python reconoce que la cadena ya es de tipo Unicode
print(type(cadena_unicode_escapada))  # Salida: <class 'str'>