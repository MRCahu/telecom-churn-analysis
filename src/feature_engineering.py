import os
import pandas as pd

# -------------------------------------------------
# 1) Definir caminhos de entrada e saída
# -------------------------------------------------
# Caminho para o CSV limpo que criamos em data_cleaning.py
BASE_DIR = os.path.dirname(__file__)                     # .../src
CLEANED_CSV = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_cleaned.csv")

# Caminho para onde vamos salvar o CSV com a nova feature
OUTPUT_DIR = os.path.join(BASE_DIR, os.pardir, "data", "clean")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "telecom_churn_features.csv")

# -------------------------------------------------
# 2) Carregar o DataFrame limpo
# -------------------------------------------------
print("Carregando CSV limpo de:", CLEANED_CSV)
df = pd.read_csv(CLEANED_CSV)

print("Dimensões antes de adicionar nova coluna:", df.shape)
print()

# -------------------------------------------------
# 3) Criar a coluna 'Contas_Diarias'
# -------------------------------------------------
# Assumimos que 'account.Charges.Monthly' existe e representa o valor cobrado no mês
if "account.Charges.Monthly" not in df.columns:
    raise KeyError("Coluna 'account.Charges.Monthly' não encontrada no DataFrame.")

# Calcule o valor diário como MonthlyCharges dividido por 30
df["Contas_Diarias"] = df["account.Charges.Monthly"] / 30

# Opcional: arredonde para 2 casas decimais
df["Contas_Diarias"] = df["Contas_Diarias"].round(2)

print("Coluna 'Contas_Diarias' criada com sucesso.")
print("Dimensões após adicionar a coluna:", df.shape)
print()

# -------------------------------------------------
# 4) Salvar o novo DataFrame com a feature
# -------------------------------------------------
# Garante que a pasta de saída exista
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Salva em CSV
df.to_csv(OUTPUT_CSV, index=False)
print(f"DataFrame com nova feature salvo em: {OUTPUT_CSV}")
