## importando bibliotecas necessarias

import json
import requests

## link da api

api_link = "https://dicio-api-ten.vercel.app/v2/paralelepipedo"

## requests

r = requests.get(api_link)

## convertendo os dados do request em dicionario

dados = r.json()



print(dados)


