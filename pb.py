# API for DNI

from urllib.request import urlopen
import json

dni = 72088685

url = "https://dniruc.apisperu.com/api/v1/dni/"+ dni +"?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdhYnJpZWxzb3RvY2NveWFAZ21haWwuY29tIn0.BRxBA3nIZYvMzKNpljaAdICLSUa7UoGpgp7_I3qCQec"

response = urlopen(url)
data = json.loads(response.read())

state = data["succes"]
dni = data["dni"]
nombres = data["nombres"]
AP_paterno = data["apellidoPaterno"]
AP_materno = data["apellidoMaterno"]