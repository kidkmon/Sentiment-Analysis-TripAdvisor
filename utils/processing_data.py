import urllib.request # biblioteca que trabalha com requisições HTTP
import json # biblioteca para processamento de dados do tipo JSON

import pandas as pd
from pandas import json_normalize


def load_data():
  print("GERANDO BASE DE DADOS")

  url = "http://tiagodemelo.info/datasets/dataset-v2.dat"
  dat_file = urllib.request.urlopen(url)

  json_format_file = [json.loads(line) for line in dat_file]

  df = pd.DataFrame(json_format_file)

  return df


def get_address_df():
  df = load_data()
  item_reviewed = json_normalize(df["itemReviewed"])

  columns = ["name", "address.streetAddress", "address.addressLocality", "address.addressRegion", "address.postalCode"]

  address_group = item_reviewed.groupby(columns).size().reset_index()
  address_group["address"] = address_group[columns].apply(lambda value: " ".join(value), axis=1)

  return address_group
