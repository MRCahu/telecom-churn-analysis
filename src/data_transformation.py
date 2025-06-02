import os
import pandas as pd

# -------------------------------------------------
# 1) Definir caminhos de entrada e saída
# -------------------------------------------------

BASE_DIR = os.path.dirname(__file__)                      # .../src
INPUT_CSV = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_features.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, os.pardir, "data", "clean")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "telecom_churn_transformed.csv")

# -------------------------------------------------
# 2) Carregar o CSV com features já calculadas
# -------------------------------------------------

print("Carregando dados para transformacao de:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV)

print("Dimensoes antes da transformacao:", df.shape)
print()

# -------------------------------------------------
# 3) Renomear colunas para nomes em portugues
# -------------------------------------------------
mapeamento_colunas = {
    "customerID":              "ID_Cliente",
    "Churn":                   "Evasao",
    "customer.gender":         "Genero",
    "customer.SeniorCitizen":  "Idoso",
    "customer.Partner":        "Tem_Conjuge",
    "customer.Dependents":     "Tem_Dependentes",
    "customer.tenure":         "Meses_Contratado",
    "phone.PhoneService":      "Tem_Telefone",
    "phone.MultipleLines":     "Linhas_Adicionais",
    "internet.InternetService":"Tipo_Internet",
    "internet.OnlineSecurity": "Seg_Online",
    "internet.OnlineBackup":   "Backup_Online",
    "internet.DeviceProtection":"Prot_Dispositivos",
    "internet.TechSupport":    "Suporte_Tecnico",
    "internet.StreamingTV":    "Streaming_TV",
    "internet.StreamingMovies":"Streaming_Filmes",
    "account.Contract":        "Tipo_Contrato",
    "account.PaperlessBilling":"Fatura_Digital",
    "account.PaymentMethod":   "Metodo_Pagamento",
    "account.Charges.Monthly": "Cobranca_Mensal",
    "account.Charges.Total":   "Cobranca_Total",
    "Contas_Diarias":          "Cobranca_Diaria"
}

df.rename(columns=mapeamento_colunas, inplace=True)

print("Colunas renomeadas para portugues (ou nomes claros).")
print("Novas colunas:", df.columns.tolist())
print()

# -------------------------------------------------
# 4) Converter valores textuais para binarios ou 'Sim'/'Nao'
# -------------------------------------------------

print("1) Conversao de valores textuais para binarios")

# (a) Converter Evasao (True/False) para 1/0
df["Evasao"] = df["Evasao"].map({True: 1, False: 0})
print("  - Coluna 'Evasao' convertida para 1 (Sim) / 0 (Nao)")

# (b) Converter colunas yes/no -> 1/0
cols_yes_no = [
    "Tem_Conjuge", "Tem_Dependentes", "Tem_Telefone",
    "Fatura_Digital"
]

for col in cols_yes_no:
    if col in df.columns:
        df[col] = df[col].map({"yes": 1, "no": 0, "unknown": 0})
        print(f"  - '{col}' mapeado para 1/0 (yes->1, no->0)")

# (c) Colunas com 'yes' / 'no' / 'no internet service' -> 1/0
cols_three_cats = [
    "Linhas_Adicionais",
    "Seg_Online", "Backup_Online", "Prot_Dispositivos",
    "Suporte_Tecnico", "Streaming_TV", "Streaming_Filmes"
]

for col in cols_three_cats:
    if col in df.columns:
        df[col] = df[col].map({
            "yes": 1,
            "no": 0,
            "no internet service": 0
        })
        print(f"  - '{col}' mapeado (yes->1, no->0, no internet service->0)")

# (d) Traduzir Tipo_Internet
if "Tipo_Internet" in df.columns:
    df["Tipo_Internet"] = df["Tipo_Internet"].map({
        "dsl": "DSL",
        "fiber optic": "Fibra Optica",
        "no": "Sem Internet"
    })
    print("  - 'Tipo_Internet' traduzido: dsl->DSL, fiber optic->Fibra Optica, no->Sem Internet")

# (e) Traduzir Tipo_Contrato
if "Tipo_Contrato" in df.columns:
    df["Tipo_Contrato"] = df["Tipo_Contrato"].map({
        "month-to-month": "Mensal",
        "one year": "Anual",
        "two year": "Bienal"
    })
    print("  - 'Tipo_Contrato' traduzido: month-to-month->Mensal, one year->Anual, two year->Bienal")

# (f) Traduzir Metodo_Pagamento
if "Metodo_Pagamento" in df.columns:
    df["Metodo_Pagamento"] = df["Metodo_Pagamento"].map({
        "electronic check": "Cheque Eletronico",
        "mailed check": "Cheque Enviado",
        "bank transfer (automatic)": "Transferencia Bancaria (Automatica)",
        "credit card (automatic)": "Cartao de Credito (Automatico)"
    })
    print("  - 'Metodo_Pagamento' traduzido para portugues")

print()

# -------------------------------------------------
# 5) Converter 'Genero' para 1/0 (opcional)
# -------------------------------------------------
if "Genero" in df.columns:
    df["Genero"] = df["Genero"].map({"female": 1, "male": 0})
    print("  - 'Genero' mapeado: female->1, male->0")
print()

# -------------------------------------------------
# 6) Garantir 'Idoso' como 0/1
# -------------------------------------------------
if "Idoso" in df.columns:
    df["Idoso"] = df["Idoso"].astype(int)
    print("  - 'Idoso' mantido como 0/1")
print()

# -------------------------------------------------
# 7) Mostra as primeiras 5 linhas para conferência
# -------------------------------------------------
print("Primeiras 5 linhas apos transformacoes:\n")
print(df.head(), "\n")

# -------------------------------------------------
# 8) Salvar o DataFrame transformado
# -------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
df.to_csv(OUTPUT_CSV, index=False)
print(f"DataFrame transformado salvo em: {OUTPUT_CSV}")
