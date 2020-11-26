import requests
import pandas as pd

from pandas import json_normalize
from utils import get_address_df
from config import KEY, BASE_URL

address_df = get_address_df()

print("INICIANDO COLETA DE ENDEREÇO")
for address in address_df:
    try:
        params = {'sensor': 'false', 'address': address, "key": KEY}
        r = requests.get(BASE_URL, params=params)
        results = r.json()

        location = results["results"][0]["geometry"]["location"]

        with open('data/address.txt', 'a', encoding="utf-8") as f:
                f.write(str(location["lat"]) + ',' + str(location["lng"]) + '\n')
                f.close()

        print(location)
    except:
        
        print("FALHA AO GERAR COORDENADAS")
        with open('data/fail.txt', 'a', encoding="utf-8") as f:
                f.write(address + '\n')
                f.close()

        continue