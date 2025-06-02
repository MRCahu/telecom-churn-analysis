import os
import json
import pandas as pd

# -------------------------------------------------
# 1) Carregar JSON bruto e normalizar em DataFrame
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

df_full = pd.json_normalize(data_json)

# -------------------------------------------------
# 2) Verificar quais colunas existem (para conferência)
# -------------------------------------------------
print("Colunas disponíveis em df_full:\n")
for col in df_full.columns:
    print(f"  - {col}")
print(f"\nTotal de colunas: {len(df_full.columns)}\n")

# -------------------------------------------------
# 3) Criar o subset com as colunas relevantes
#    Use exatamente estes nomes, conforme o JSON
# -------------------------------------------------
colunas_relevantes = [
    "customerID",               # ID do cliente
    "Churn",                    # coluna alvo (True/False ou Yes/No)
    # Perfil demográfico
    "customer.gender",
    "customer.SeniorCitizen",
    "customer.Partner",
    "customer.Dependents",
    "customer.tenure",          # tempo em meses
    # Serviços de telefone
    "phone.PhoneService",
    "phone.MultipleLines",
    # Serviços de internet
    "internet.InternetService",
    "internet.OnlineSecurity",
    "internet.OnlineBackup",
    "internet.DeviceProtection",
    "internet.TechSupport",
    "internet.StreamingTV",
    "internet.StreamingMovies",
    # Dados de conta/contrato
    "account.Contract",
    "account.PaperlessBilling",
    "account.PaymentMethod",
    "account.Charges.Monthly",
    "account.Charges.Total"
]

colunas_existentes = [c for c in colunas_relevantes if c in df_full.columns]
df = df_full[colunas_existentes].copy()

print("Dimensões iniciais do subset:", df.shape)
print("Colunas selecionadas:", colunas_existentes, "\n")

# -------------------------------------------------
# 4) Tratar valores ausentes (missing values)
# -------------------------------------------------
print("1) TRATAMENTO DE VALORES AUSENTES (missing values)")
missing_before = df.isna().sum().sort_values(ascending=False)
print("Valores ausentes antes do tratamento:")
print(missing_before[missing_before > 0], "\n")

# Preencher account.Charges.Total com mediana, se houver missing
if "account.Charges.Total" in df.columns:
    n_missing = df["account.Charges.Total"].isna().sum()
    if n_missing > 0:
        mediana = df["account.Charges.Total"].median()
        df["account.Charges.Total"].fillna(mediana, inplace=True)
        print(f"  • Preencheu {n_missing} missings em 'account.Charges.Total' com mediana = {mediana:.2f}")

# Preencher outras numéricas com mediana (caso apareçam)
for col in df.select_dtypes(include="number").columns:
    if df[col].isna().sum() > 0:
        med = df[col].median()
        df[col].fillna(med, inplace=True)
        print(f"  • Preencheu missings em '{col}' com mediana {med:.2f}")

# Preencher categóricas com 'unknown'
for col in df.select_dtypes(include="object").columns:
    if df[col].isna().sum() > 0:
        n_miss = df[col].isna().sum()
        df[col].fillna("unknown", inplace=True)
        print(f"  • Preencheu {n_miss} missings em '{col}' com 'unknown'")

print("\nValores ausentes após tratamento (deve estar vazio):")
print(df.isna().sum()[df.isna().sum() > 0], "\n")

# -------------------------------------------------
# 5) Remover duplicados
# -------------------------------------------------
print("2) TRATAMENTO DE DADOS DUPLICADOS")
if "customerID" in df.columns:
    dup_count = df.duplicated(subset=["customerID"]).sum()
    print(f"  • {dup_count} registros duplicados em 'customerID' antes de remover")
    df.drop_duplicates(subset=["customerID"], keep="first", inplace=True)
    print(f"  • Removidos duplicados, agora dimensões: {df.shape}")
else:
    dup_total = df.duplicated().sum()
    print(f"  • {dup_total} registros duplicados (todas as colunas) antes de remover")
    df.drop_duplicates(keep="first", inplace=True)
    print(f"  • Removidos duplicados, agora dimensões: {df.shape}")
print()

# -------------------------------------------------
# 6) Padronizar strings em colunas categóricas
# -------------------------------------------------
print("3) PADRONIZAÇÃO DE STRINGS (strip + lower)")

categorical_cols = [
    "customer.gender",
    "customer.Partner",
    "customer.Dependents",
    "phone.PhoneService",
    "phone.MultipleLines",
    "internet.InternetService",
    "internet.OnlineSecurity",
    "internet.OnlineBackup",
    "internet.DeviceProtection",
    "internet.TechSupport",
    "internet.StreamingTV",
    "internet.StreamingMovies",
    "account.Contract",
    "account.PaperlessBilling",
    "account.PaymentMethod",
    "Churn"
]

for col in categorical_cols:
    if col in df.columns and df[col].dtype == "object":
        df[col] = df[col].str.strip().str.lower()
        print(f"  • '{col}': strip() e lower() aplicados")
print()

# -------------------------------------------------
# 7) Corrigir valores inconsistentes em categorias
# -------------------------------------------------
print("4) CORREÇÃO DE VALORES INCONSISTENTES (mapeamento)")

# Churn: mapear 'yes'/'no' para boolean (True/False)
if "Churn" in df.columns:
    df["Churn"] = df["Churn"].replace({"yes": True, "no": False})
    print("  • 'Churn': mapeou 'yes' → True e 'no' → False")

# gender: mapear 'male'/'female' conforme dicionário (pode deixar como está)
# senior citizen já é numérico (0/1)  
# Não há colunas extra em gênero, então não precisa mapear.

# phone.PhoneService: manter 'yes' ou 'no'
# multiple lines: manter 'yes' / 'no' / 'no phone service'
if "phone.MultipleLines" in df.columns:
    df["phone.MultipleLines"] = df["phone.MultipleLines"].replace({
        "no phone service": "no phone service",
        "no": "no",
        "yes": "yes"
    })
    print("  • 'phone.MultipleLines': valores padronizados")

# internet.InternetService
if "internet.InternetService" in df.columns:
    df["internet.InternetService"] = df["internet.InternetService"].replace({
        "dsl": "dsl",
        "fiber optic": "fiber optic",
        "no": "no"
    })
    print("  • 'internet.InternetService': valores padronizados (dsl/fiber optic/no)")

# Para colunas que têm “no internet service” vs “no” vs “yes”:
col_internet_cat = [
    "internet.OnlineSecurity",
    "internet.OnlineBackup",
    "internet.DeviceProtection",
    "internet.TechSupport",
    "internet.StreamingTV",
    "internet.StreamingMovies"
]
for col in col_internet_cat:
    if col in df.columns:
        df[col] = df[col].replace({
            "no": "no",
            "yes": "yes",
            "no internet service": "no internet service"
        })
        print(f"  • '{col}': valores padronizados (yes / no / no internet service)")

# contract: mapear possíveis variações (ex.: 'month-to-month', 'one year', 'two year')
if "account.Contract" in df.columns:
    df["account.Contract"] = df["account.Contract"].replace({
        "month-to-month": "month-to-month",
        "one year": "one year",
        "two year": "two year"
    })
    print("  • 'account.Contract': valores padronizados")

# paperless billing: 'yes' / 'no'
if "account.PaperlessBilling" in df.columns:
    df["account.PaperlessBilling"] = df["account.PaperlessBilling"].replace({
        "yes": "yes",
        "no": "no"
    })
    print("  • 'account.PaperlessBilling': valores padronizados")

# payment method: mapear as strings já convertidas para lower (e.g., 'electronic check', 'mailed check', etc.)
if "account.PaymentMethod" in df.columns:
    # Exemplo de mapeamento (se necessário)
    df["account.PaymentMethod"] = df["account.PaymentMethod"].replace({
        "electronic check": "electronic check",
        "mailed check": "mailed check",
        "bank transfer (automatic)": "bank transfer (automatic)",
        "credit card (automatic)": "credit card (automatic)"
    })
    print("  • 'account.PaymentMethod': valores padronizados")
print()

# -------------------------------------------------
# 8) Tratar outliers em colunas numéricas (opcional)
# -------------------------------------------------
print("5) TRATAMENTO DE OUTLIERS EM COLUNAS NUMÉRICAS (opcional)")
numeric_cols = ["customer.SeniorCitizen", "customer.tenure", "account.Charges.Monthly", "account.Charges.Total"]
for col in numeric_cols:
    if col in df.columns:
        # Exemplo genérico: remover valores negativos ou absurdos (se existirem)
        if df[col].dtype in ["int64", "float64"]:
            cond_invalid = (df[col] < 0)
            n_out = cond_invalid.sum()
            if n_out > 0:
                print(f"  • Encontrou {n_out} valores inválidos em '{col}'. Removendo.")
                df = df[~cond_invalid].copy()
                print(f"  • Novo tamanho após remover outliers de '{col}': {df.shape}")
print()

# -------------------------------------------------
# 9) (Opcional) Filtrar datas anômalas – **não aplicável** pois não existem colunas de data
# -------------------------------------------------
print("6) TRATAMENTO DE DATAS ANÔMALAS (não aplicável)")

# -------------------------------------------------
# 10) Mostrar resultado final e salvar
# -------------------------------------------------
print("Dimensões finais após limpeza:", df.shape)
print("Colunas finais:", df.columns.tolist())

clean_dir = os.path.join(os.path.dirname(__file__), os.pardir, "data", "clean")
os.makedirs(clean_dir, exist_ok=True)
cleaned_path = os.path.join(clean_dir, "telecom_churn_cleaned.csv")
df.to_csv(cleaned_path, index=False)
print(f"\nDataFrame completamente limpo salvo em: {cleaned_path}")
