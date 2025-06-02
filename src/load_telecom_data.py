import os
import json
import pandas as pd

# Caminho local para o JSON bruto
# Observe que o JSON está em data/raw/TelecomX_Data.json
path_raw = os.path.join(
    os.path.dirname(__file__),  # pasta src/
    os.pardir,                  # sobe uma pasta (telecom-churn-analysis/)
    "data",
    "raw",
    "TelecomX_Data.json"
)

# 1) Abra o arquivo JSON e carregue em uma list/dict
with open(path_raw, "r", encoding="utf-8") as f:
    data_json = json.load(f)

# 2) Converta para DataFrame do Pandas
df = pd.json_normalize(data_json)

# 3) Mostre algumas informações no console
print("→ Dimensões do DataFrame:", df.shape)
print("\n→ Primeiras 10 linhas:")
print(df.head(10))

print("\n→ Estrutura (info) do DataFrame:")
df.info()

print("\n→ Tipos de cada coluna:")
print(df.dtypes)
