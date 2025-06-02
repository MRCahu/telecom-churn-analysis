import os
import json
import pandas as pd

# -------------------------------------------------
# 1) Carregar JSON bruto e criar DataFrame
# -------------------------------------------------
path_raw = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    "data",
    "raw",
    "TelecomX_Data.json"
)

with open(path_raw, "r", encoding="utf-8") as f:
    data_json = json.load(f)

df = pd.json_normalize(data_json)

# -------------------------------------------------
# 2) Inspeção inicial (dimensões, head, info, dtypes)
# -------------------------------------------------
print("Dimensões do DataFrame:", df.shape)
print("\nPrimeiras 10 linhas:")
print(df.head(10))

print("\nEstrutura (info) do DataFrame:")
df.info()

print("\nTipos de cada coluna:")
print(df.dtypes)

# -------------------------------------------------
# 3) Converter colunas de data para datetime
# -------------------------------------------------
if "signup_date" in df.columns:
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
if "last_active_date" in df.columns:
    df["last_active_date"] = pd.to_datetime(df["last_active_date"], errors="coerce")

print("\nApós conversão de datas:")
if "signup_date" in df.columns:
    print("signup_date:", df["signup_date"].dtype)
if "last_active_date" in df.columns:
    print("last_active_date:", df["last_active_date"].dtype)

# -------------------------------------------------
# 4) Selecionar colunas mais relevantes para churn
# -------------------------------------------------
colunas_relevantes = [
    "customer_id", "churn_flag",
    "gender", "senior_citizen", "partner", "dependents",
    "tenure_months", "contract_type", "paperless_billing", "payment_method",
    "monthly_charges", "total_charges",
    "internet_service", "tech_support",
    "signup_date", "last_active_date"
]
colunas_existentes = [c for c in colunas_relevantes if c in df.columns]
df_subset = df[colunas_existentes].copy()

print("\nDimensões do DataFrame subset:", df_subset.shape)
print("Colunas usadas no subset:", colunas_existentes)
print("\nPrimeiras 5 linhas do subset:")
print(df_subset.head())

# -------------------------------------------------
# 5) Salvar o subset limpo em CSV na pasta data/clean/
# -------------------------------------------------
clean_dir = os.path.join(os.path.dirname(__file__), os.pardir, "data", "clean")
os.makedirs(clean_dir, exist_ok=True)

subset_path = os.path.join(clean_dir, "telecom_churn_subset.csv")
df_subset.to_csv(subset_path, index=False)
print(f"\nSubset salvo em: {subset_path}")
