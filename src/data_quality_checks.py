import os
import json
import pandas as pd

# -------------------------------------------------
# 1) Carregar o JSON bruto e criar o DataFrame completo
# -------------------------------------------------
raw_path = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    "data",
    "raw",
    "TelecomX_Data.json"
)

with open(raw_path, "r", encoding="utf-8") as f:
    data_json = json.load(f)

df = pd.json_normalize(data_json)

# Converter colunas de data para datetime, se existirem
if "signup_date" in df.columns:
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
if "last_active_date" in df.columns:
    df["last_active_date"] = pd.to_datetime(df["last_active_date"], errors="coerce")

# -------------------------------------------------
# 2) Selecionar colunas relevantes para churn (criar subset em memória)
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

print("Executando Data Quality Checks sobre o subset criado em memória …\n")

# -------------------------------------------------
# 3) Checar valores ausentes (missing values)
# -------------------------------------------------
print("1) MISSING VALUES")
missing_counts = df_subset.isna().sum().sort_values(ascending=False)
print(missing_counts[missing_counts > 0], "\n")

total_rows = df_subset.shape[0]
missing_pct = (df_subset.isna().sum() / total_rows * 100).sort_values(ascending=False)
print("Porcentagem de missing (se > 0):")
print(missing_pct[missing_pct > 0].round(2).astype(str) + "%", "\n")

# -------------------------------------------------
# 4) Checar duplicados
# -------------------------------------------------
print("2) DUPLICADOS")
if "customer_id" in df_subset.columns:
    duped = df_subset.duplicated(subset=["customer_id"]).sum()
    print(f"Duplicados em 'customer_id': {duped}\n")
else:
    duped = df_subset.duplicated().sum()
    print(f"Duplicados totais: {duped}\n")

# -------------------------------------------------
# 5) Tipos de dados e formatação
# -------------------------------------------------
print("3) TIPOS DE DADOS")
print(df_subset.dtypes, "\n")

categorical_cols = [
    "gender", "partner", "dependents", "phone_service", "multiple_lines",
    "internet_service", "online_security", "online_backup",
    "device_protection", "tech_support", "streaming_tv", "streaming_movies",
    "contract_type", "paperless_billing", "payment_method"
]

print("Valores únicos em colunas categóricas:")
for col in categorical_cols:
    if col in df_subset.columns:
        uniques = df_subset[col].unique()
        print(f"  - {col} ({len(uniques)}): {uniques}")
print()

# -------------------------------------------------
# 6) Verificar formatação de strings
# -------------------------------------------------
print("4) FORMATAÇÃO DE STRINGS")
for col in categorical_cols:
    if col in df_subset.columns and df_subset[col].dtype == "object":
        stripped = df_subset[col].str.strip()
        n_spaces = (stripped != df_subset[col]).sum()
        if n_spaces > 0:
            print(f"  • {col}: há {n_spaces} valores com espaços em branco.")
        lower = df_subset[col].str.lower()
        if any(df_subset[col].str.lower() != df_subset[col]):
            print(f"  • {col}: diferenças de maiúsculas/minúsculas detectadas.")
print()

# -------------------------------------------------
# 7) Outliers em colunas numéricas
# -------------------------------------------------
print("5) OUTLIERS EM NUMÉRICOS")
numeric_cols = df_subset.select_dtypes(include=["int64", "float64"]).columns.tolist()
for col in numeric_cols:
    desc = df_subset[col].describe()
    print(f"  • {col}: count={desc['count']}, mean={desc['mean']:.2f}, min={desc['min']}, 25%={desc['25%']}, 50%={desc['50%']}, 75%={desc['75%']}, max={desc['max']}\n")

# -------------------------------------------------
# 8) Range de datas
# -------------------------------------------------
print("6) RANGE DE DATAS")
date_cols = df_subset.select_dtypes(include=["datetime64[ns]"]).columns.tolist()
for col in date_cols:
    min_date = df_subset[col].min()
    max_date = df_subset[col].max()
    print(f"  • {col}: de {min_date.date()} até {max_date.date()}")
print()

print("Data Quality Checks finalizado.")
