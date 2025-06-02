import os
import pandas as pd

# -------------------------------------------------
# 1) Definir caminho de entrada (CSV transformado)
# -------------------------------------------------

BASE_DIR = os.path.dirname(__file__)  # .../src
INPUT_CSV = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_transformed.csv")

# -------------------------------------------------
# 2) Carregar o DataFrame transformado
# -------------------------------------------------

print("Carregando dados de:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV)

print("Dimensoes do DataFrame:", df.shape)
print()

# -------------------------------------------------
# 3) Estatísticas gerais com describe()
# -------------------------------------------------

print("=== Estatísticas Descritivas GERAIS (DataFrame.describe) ===")
# describe() por padrão mostra count, mean, std, min, 25%, 50%, 75%, max para colunas numéricas
stats_gerais = df.describe()
print(stats_gerais)
print()

# Se quiser incluir também colunas categóricas (para contar valores únicos), use describe(include='all'):
print("=== Estatísticas Descritivas COMPLETAS (DataFrame.describe include='all') ===")
stats_all = df.describe(include="all")
print(stats_all)
print()

# -------------------------------------------------
# 4) Mediana e outras métricas específicas
# -------------------------------------------------

# Exemplo: calcular mediana manualmente para Cobranca_Mensal e Meses_Contratado
if "Cobranca_Mensal" in df.columns:
    mediana_mensal = df["Cobranca_Mensal"].median()
    print(f"Mediana de Cobranca_Mensal: {mediana_mensal:.2f}")

if "Meses_Contratado" in df.columns:
    mediana_tenure = df["Meses_Contratado"].median()
    print(f"Mediana de Meses_Contratado: {mediana_tenure:.2f}")
print()

# Outras métricas: variância, amplitude (max - min), coeficiente de variação
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
print("=== Métricas ADICIONAIS para colunas numéricas ===")
for col in numeric_cols:
    series = df[col]
    media = series.mean()
    desvio = series.std()
    variancia = series.var()
    minimo = series.min()
    maximo = series.max()
    amplitude = maximo - minimo
    coef_var = desvio / media if media != 0 else float("nan")
    print(f"- {col}:")
    print(f"    count = {series.count()}")
    print(f"    média = {media:.2f}")
    print(f"    mediana = {series.median():.2f}")
    print(f"    desvio padrão = {desvio:.2f}")
    print(f"    variância = {variancia:.2f}")
    print(f"    mínimo = {minimo:.2f}")
    print(f"    25% = {series.quantile(0.25):.2f}")
    print(f"    50% = {series.quantile(0.50):.2f}")
    print(f"    75% = {series.quantile(0.75):.2f}")
    print(f"    máximo = {maximo:.2f}")
    print(f"    amplitude (max-min) = {amplitude:.2f}")
    print(f"    coeficiente de variação (std/mean) = {coef_var:.2f}")
    print()

# -------------------------------------------------
# 5) Contagem de frequências para colunas categóricas
# -------------------------------------------------

print("=== CONTAGEM DE FREQUÊNCIAS PARA COLUNAS CATEGÓRICAS ===")
categorical_cols = [
    "Genero", "Idoso", "Tem_Conjuge", "Tem_Dependentes",
    "Tem_Telefone", "Tipo_Internet", "Tipo_Contrato",
    "Fatura_Digital", "Metodo_Pagamento"
]

for col in categorical_cols:
    if col in df.columns:
        contagens = df[col].value_counts(dropna=False)
        porcentagens = df[col].value_counts(normalize=True, dropna=False) * 100
        print(f"- {col}:")
        print("   Frequência absoluta:")
        print(contagens.to_dict())
        print("   Frequência relativa (%):")
        print(porcentagens.round(2).to_dict())
        print()

# -------------------------------------------------
# 6) Grupos de estatísticas (por Evasao = 0/1)
# -------------------------------------------------

if "Evasao" in df.columns:
    print("=== ESTATÍSTICAS POR Evasao (0 = não evadiu, 1 = evadiu) ===\n")
    grupos = df.groupby("Evasao")
    for nome, grupo in grupos:
        print(f"-- Evasao = {int(nome)} --")
        print(grupo.describe(include="all"))
        print()

print("\nAnálise descritiva concluída.")
