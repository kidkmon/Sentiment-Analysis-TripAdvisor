import requests
import pandas as pd

from pandas import json_normalize
from utils import get_address_df
from config import KEY, BASE_URL

address_df = get_address_df()
cont = 0

print("INICIANDO COLETA DE ENDEREÇO")

for address in address_df["address"]:
    cont = cont + 1

    print("QUANTIDADE DE ENDEREÇOS COLETADOS: ", cont)
    try:
        params = {'sensor': 'false', 'address': address, "key": KEY}
        r = requests.get(BASE_URL, params=params)
        results = r.json()

        city = results["results"][0]["address_components"][3]["long_name"]
        state = results["results"][0]["address_components"][4]["long_name"]
        location = results["results"][0]["geometry"]["location"]

        with open('data/address.txt', 'a', encoding="utf-8") as f:
            f.write(city + ',' + state + ',' +  str(location["lat"]) + ',' + str(location["lng"]) + '\n')
            f.close()

        print(location)
    except:

        print("FALHA AO GERAR COORDENADAS")
        with open('data/address.txt', 'a', encoding="utf-8") as f:
            f.write(",,," + '\n')
            f.close()

        continue
