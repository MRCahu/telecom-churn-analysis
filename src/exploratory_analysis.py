import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# 1) Configurações iniciais
# -------------------------------------------------

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# Caminhos
BASE_DIR    = os.path.dirname(__file__)            # .../src
CLEAN_CSV   = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_cleaned.csv")
REPORTS_DIR = os.path.join(BASE_DIR, os.pardir, "reports")

# Garante que a pasta reports/ exista
os.makedirs(REPORTS_DIR, exist_ok=True)

# -------------------------------------------------
# 2) Carregar o CSV limpo
# -------------------------------------------------

print("Carregando dados limpos de:", CLEAN_CSV)
df = pd.read_csv(CLEAN_CSV)

print("Dimensoes do DataFrame limpo:", df.shape)
print()

# -------------------------------------------------
# 3) Estatísticas Descritivas
# -------------------------------------------------

print("=== Estatísticas Descritivas (todas as colunas) ===")
print(df.describe(include="all"))
print("\n")

# Se quiser estatísticas separadas para churn = True/False:
if "Churn" in df.columns:
    print("=== Estatísticas para clientes que churnaram (Churn=True) ===")
    print(df[df["Churn"] == True].describe(include="all"))
    print("\n")
    print("=== Estatísticas para clientes que permaneceram (Churn=False) ===")
    print(df[df["Churn"] == False].describe(include="all"))
    print("\n")

# -------------------------------------------------
# 4) Gráficos Básicos
# -------------------------------------------------

# 4.1) Histograma de monthly charges
if "account.Charges.Monthly" in df.columns:
    plt.figure()
    sns.histplot(df["account.Charges.Monthly"], bins=30, kde=True)
    plt.title("Distribuição de Monthly Charges")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Contagem")
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "hist_monthly_charges.png")
    plt.savefig(out_path)
    plt.close()
    print("Histograma de 'account.Charges.Monthly' salvo em:", out_path)

# 4.2) Boxplot: monthly charges × churn
if {"account.Charges.Monthly", "Churn"}.issubset(df.columns):
    plt.figure()
    sns.boxplot(x="Churn", y="account.Charges.Monthly", data=df)
    plt.title("Boxplot: Monthly Charges por Churn")
    plt.xlabel("Churn (False=permanece, True=cancelou)")
    plt.ylabel("Monthly Charges")
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "boxplot_monthly_charges_churn.png")
    plt.savefig(out_path)
    plt.close()
    print("Boxplot 'Monthly Charges × Churn' salvo em:", out_path)

# 4.3) Countplot: contrato × churn
if {"account.Contract", "Churn"}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="account.Contract", hue="Churn", data=df)
    plt.title("Contagem de Churn por Tipo de Contrato")
    plt.xlabel("Contract")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45)
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "count_churn_contract.png")
    plt.savefig(out_path)
    plt.close()
    print("Countplot 'Churn × Account.Contract' salvo em:", out_path)

# 4.4) Countplot: internet service × churn
if {"internet.InternetService", "Churn"}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="internet.InternetService", hue="Churn", data=df)
    plt.title("Contagem de Churn por Internet Service")
    plt.xlabel("Internet Service")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45)
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "count_churn_internet_service.png")
    plt.savefig(out_path)
    plt.close()
    print("Countplot 'Churn × Internet Service' salvo em:", out_path)

# 4.5) Countplot: gender × churn
if {"customer.gender", "Churn"}.issubset(df.columns):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="customer.gender", hue="Churn", data=df)
    plt.title("Contagem de Churn por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Contagem")
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "count_churn_gender.png")
    plt.savefig(out_path)
    plt.close()
    print("Countplot 'Churn × Gender' salvo em:", out_path)

# -------------------------------------------------
# 5) Heatmap de Correlação (apenas numéricos)
# -------------------------------------------------

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
if len(numeric_cols) >= 2:
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Mapa de Correlação - Variáveis Numéricas")
    plt.tight_layout()
    out_path = os.path.join(REPORTS_DIR, "heatmap_correlation.png")
    plt.savefig(out_path)
    plt.close()
    print("Heatmap de correlação salvo em:", out_path)

# -------------------------------------------------
# 6) Gráficos adicionais sugeridos
#    (exemplos de variáveis de serviço × churn)
# -------------------------------------------------

serv_cols = [
    "internet.OnlineSecurity", "internet.OnlineBackup", "internet.DeviceProtection",
    "internet.TechSupport", "internet.StreamingTV", "internet.StreamingMovies"
]
for col in serv_cols:
    if {col, "Churn"}.issubset(df.columns):
        plt.figure(figsize=(6, 4))
        sns.countplot(x=col, hue="Churn", data=df)
        plt.title(f"Churn por {col}")
        plt.xlabel(col)
        plt.ylabel("Contagem")
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename = f"count_churn_{col.replace('.', '_')}.png"
        out_path = os.path.join(REPORTS_DIR, filename)
        plt.savefig(out_path)
        plt.close()
        print(f"Countplot 'Churn × {col}' salvo em:", out_path)

# -------------------------------------------------
# 7) Finalização
# -------------------------------------------------

print("\nAnalise exploratoria concluida. Confira a pasta 'reports/' para os PNGs.")

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# Configurações iniciais
# -------------------------------------------------

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

BASE_DIR    = os.path.dirname(__file__)            # pasta src/
INPUT_CSV   = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_transformed.csv")
REPORTS_DIR = os.path.join(BASE_DIR, os.pardir, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# -------------------------------------------------
# Carregar dados transformados
# -------------------------------------------------

print("Carregando dados de:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV)

print("Dimensoes do DataFrame:", df.shape)
print()

# -------------------------------------------------
# Lista de variáveis categóricas para explorar churn
# -------------------------------------------------

# Essas colunas já estão em português e mapeadas como 0/1 ou categorias legíveis
categorical_cols = [
    "Genero",           # 1=female, 0=male
    "Idoso",            # 1 se idoso, 0 caso contrário
    "Tem_Conjuge",      # 1/0
    "Tem_Dependentes",  # 1/0
    "Tipo_Contrato",    # Mensal, Anual, Bienal
    "Metodo_Pagamento", # Cheque Eletronico, Cheque Enviado, Transferencia..., Cartao...
    "Tipo_Internet",    # DSL, Fibra Optica, Sem Internet
    "Fatura_Digital",   # 1/0
]

# -------------------------------------------------
# Para cada coluna categórica, gerar countplot de churn
# -------------------------------------------------

for col in categorical_cols:
    if col not in df.columns:
        continue

    # 1) Gráfico de barras / countplot
    plt.figure()
    # hue="Evasao" mostra separado quem permaneceu vs saiu
    sns.countplot(x=col, hue="Evasao", data=df, palette="pastel")
    plt.title(f"Churn por {col}")
    plt.xlabel(col)
    plt.ylabel("Quantidade de Clientes")
    plt.xticks(rotation=45)
    plt.legend(title="Evasão", labels=["Permaneceu", "Saiu"])
    plt.tight_layout()

    # Salvar a figura
    filename = f"churn_by_{col.lower()}.png"
    out_path = os.path.join(REPORTS_DIR, filename)
    plt.savefig(out_path)
    plt.close()
    print(f"Gráfico 'Churn × {col}' salvo em: {out_path}")

    # 2) Exibir contagens e porcentagens no console
    print(f"\n=== Contagens por {col} e Evasao ===")
    cross_tab = pd.crosstab(df[col], df["Evasao"], margins=False)
    # Renomear colunas 0 e 1 para legibilidade
    cross_tab.columns = ["Permaneceu", "Saiu"]
    print(cross_tab)
    print("\n=== Porcentagens por {col} ===")
    cross_pct = cross_tab.div(cross_tab.sum(axis=1), axis=0) * 100
    print(cross_pct.round(2))
    print("\n" + "-"*50 + "\n")

print("Análise de churn por variáveis categóricas concluída.")

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# Configurações iniciais
# -------------------------------------------------

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

BASE_DIR    = os.path.dirname(__file__)            # pasta src/
INPUT_CSV   = os.path.join(BASE_DIR, os.pardir, "data", "clean", "telecom_churn_transformed.csv")
REPORTS_DIR = os.path.join(BASE_DIR, os.pardir, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# -------------------------------------------------
# Carregar dados transformados
# -------------------------------------------------

print("Carregando dados de:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV)

print("Dimensoes do DataFrame:", df.shape)
print()

# -------------------------------------------------
# 1) Distribuição de 'Cobranca_Total' por Evasao
# -------------------------------------------------

if "Cobranca_Total" in df.columns and "Evasao" in df.columns:
    # (a) Boxplot de Cobranca_Total × Evasao
    plt.figure()
    sns.boxplot(x="Evasao", y="Cobranca_Total", data=df, palette="pastel")
    plt.title("Boxplot: Total Gasto por Evasao")
    plt.xlabel("Evasao (0 = permaneceu, 1 = saiu)")
    plt.ylabel("Cobranca Total (R$)")
    plt.tight_layout()
    box_tot_path = os.path.join(REPORTS_DIR, "boxplot_cobranca_total_churn.png")
    plt.savefig(box_tot_path)
    plt.close()
    print("Boxplot 'Cobranca_Total × Evasao' salvo em:", box_tot_path)

    # (b) Histograma comparativo de Cobranca_Total
    plt.figure()
    sns.histplot(df[df["Evasao"] == 0]["Cobranca_Total"], color="#a8dadc", label="Permaneceu", kde=True, stat="density", bins=30)
    sns.histplot(df[df["Evasao"] == 1]["Cobranca_Total"], color="#f4a261", label="Saiu", kde=True, stat="density", bins=30)
    plt.title("Distribuição de Cobranca_Total por Evasao")
    plt.xlabel("Cobranca Total (R$)")
    plt.ylabel("Densidade")
    plt.legend(title="Status")
    plt.tight_layout()
    hist_tot_path = os.path.join(REPORTS_DIR, "hist_cobranca_total_churn.png")
    plt.savefig(hist_tot_path)
    plt.close()
    print("Histograma 'Cobranca_Total por Evasao' salvo em:", hist_tot_path)

    # (c) Estatísticas resumidas
    print("\n=== Estatísticas de Cobranca_Total por Evasao ===")
    stats_ct = df.groupby("Evasao")["Cobranca_Total"].describe().round(2)
    # Renomear índice para legibilidade
    stats_ct.index = ["Permaneceu", "Saiu"]
    print(stats_ct)
    print()
else:
    print("Coluna 'Cobranca_Total' ou 'Evasao' não encontrada no DataFrame.")

# -------------------------------------------------
# 2) Distribuição de 'Meses_Contratado' por Evasao
# -------------------------------------------------

if "Meses_Contratado" in df.columns and "Evasao" in df.columns:
    # (a) Boxplot de Meses_Contratado × Evasao
    plt.figure()
    sns.boxplot(x="Evasao", y="Meses_Contratado", data=df, palette="pastel")
    plt.title("Boxplot: Meses_Contratado por Evasao")
    plt.xlabel("Evasao (0 = permaneceu, 1 = saiu)")
    plt.ylabel("Meses Contratado")
    plt.tight_layout()
    box_ten_path = os.path.join(REPORTS_DIR, "boxplot_meses_contratado_churn.png")
    plt.savefig(box_ten_path)
    plt.close()
    print("Boxplot 'Meses_Contratado × Evasao' salvo em:", box_ten_path)

    # (b) Histograma comparativo de Meses_Contratado
    plt.figure()
    sns.histplot(df[df["Evasao"] == 0]["Meses_Contratado"], color="#a8dadc", label="Permaneceu", kde=True, stat="density", bins=30)
    sns.histplot(df[df["Evasao"] == 1]["Meses_Contratado"], color="#f4a261", label="Saiu", kde=True, stat="density", bins=30)
    plt.title("Distribuição de Meses_Contratado por Evasao")
    plt.xlabel("Meses Contratado")
    plt.ylabel("Densidade")
    plt.legend(title="Status")
    plt.tight_layout()
    hist_ten_path = os.path.join(REPORTS_DIR, "hist_meses_contratado_churn.png")
    plt.savefig(hist_ten_path)
    plt.close()
    print("Histograma 'Meses_Contratado por Evasao' salvo em:", hist_ten_path)

    # (c) Estatísticas resumidas
    print("\n=== Estatísticas de Meses_Contratado por Evasao ===")
    stats_mt = df.groupby("Evasao")["Meses_Contratado"].describe().round(2)
    stats_mt.index = ["Permaneceu", "Saiu"]
    print(stats_mt)
    print()
else:
    print("Coluna 'Meses_Contratado' ou 'Evasao' não encontrada no DataFrame.")

print("Analise numerica de churn concluida.")

# -------------------------------------------------
# 7) Análise Numérica de churn: Cobranca_Total e Meses_Contratado
# -------------------------------------------------

# Importante: verifique se, antes deste bloco, você já importou:
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# E se definiu:
# BASE_DIR, REPORTS_DIR, df (DataFrame limpo ou transformado conforme seu pipeline atual).
#
# No exemplo abaixo, assumimos que df já foi carregado e contém as colunas:
#    - 'Cobranca_Total'
#    - 'Meses_Contratado'
#    - 'Evasao'

# 7.1) Boxplot de Cobranca_Total × Evasao
if "Cobranca_Total" in df.columns and "Evasao" in df.columns:
    plt.figure()
    sns.boxplot(x="Evasao", y="Cobranca_Total", data=df, palette="pastel")
    plt.title("Boxplot: Cobranca_Total por Evasao")
    plt.xlabel("Evasao (0 = permaneceu, 1 = saiu)")
    plt.ylabel("Cobranca Total (R$)")
    plt.tight_layout()

    box_tot_path = os.path.join(REPORTS_DIR, "boxplot_cobranca_total_churn.png")
    plt.savefig(box_tot_path)
    plt.close()
    print("Boxplot 'Cobranca_Total × Evasao' salvo em:", box_tot_path)

    # Histograma comparativo de Cobranca_Total
    plt.figure()
    sns.histplot(
        df[df["Evasao"] == 0]["Cobranca_Total"],
        color="#a8dadc",
        label="Permaneceu",
        kde=True,
        stat="density",
        bins=30
    )
    sns.histplot(
        df[df["Evasao"] == 1]["Cobranca_Total"],
        color="#f4a261",
        label="Saiu",
        kde=True,
        stat="density",
        bins=30
    )
    plt.title("Distribuicao de Cobranca_Total por Evasao")
    plt.xlabel("Cobranca Total (R$)")
    plt.ylabel("Densidade")
    plt.legend(title="Status")
    plt.tight_layout()

    hist_tot_path = os.path.join(REPORTS_DIR, "hist_cobranca_total_churn.png")
    plt.savefig(hist_tot_path)
    plt.close()
    print("Histograma 'Cobranca_Total por Evasao' salvo em:", hist_tot_path)

    # Estatísticas resumidas
    print("\n=== Estatísticas de Cobranca_Total por Evasao ===")
    stats_ct = df.groupby("Evasao")["Cobranca_Total"].describe().round(2)
    stats_ct.index = ["Permaneceu", "Saiu"]
    print(stats_ct)
    print()
else:
    print("Coluna 'Cobranca_Total' ou 'Evasao' não encontrada no DataFrame.")

# 7.2) Boxplot de Meses_Contratado × Evasao
if "Meses_Contratado" in df.columns and "Evasao" in df.columns:
    plt.figure()
    sns.boxplot(x="Evasao", y="Meses_Contratado", data=df, palette="pastel")
    plt.title("Boxplot: Meses_Contratado por Evasao")
    plt.xlabel("Evasao (0 = permaneceu, 1 = saiu)")
    plt.ylabel("Meses Contratado")
    plt.tight_layout()

    box_ten_path = os.path.join(REPORTS_DIR, "boxplot_meses_contratado_churn.png")
    plt.savefig(box_ten_path)
    plt.close()
    print("Boxplot 'Meses_Contratado × Evasao' salvo em:", box_ten_path)

    # Histograma comparativo de Meses_Contratado
    plt.figure()
    sns.histplot(
        df[df["Evasao"] == 0]["Meses_Contratado"],
        color="#a8dadc",
        label="Permaneceu",
        kde=True,
        stat="density",
        bins=30
    )
    sns.histplot(
        df[df["Evasao"] == 1]["Meses_Contratado"],
        color="#f4a261",
        label="Saiu",
        kde=True,
        stat="density",
        bins=30
    )
    plt.title("Distribuicao de Meses_Contratado por Evasao")
    plt.xlabel("Meses Contratado")
    plt.ylabel("Densidade")
    plt.legend(title="Status")
    plt.tight_layout()

    hist_ten_path = os.path.join(REPORTS_DIR, "hist_meses_contratado_churn.png")
    plt.savefig(hist_ten_path)
    plt.close()
    print("Histograma 'Meses_Contratado por Evasao' salvo em:", hist_ten_path)

    # Estatísticas resumidas
    print("\n=== Estatísticas de Meses_Contratado por Evasao ===")
    stats_mt = df.groupby("Evasao")["Meses_Contratado"].describe().round(2)
    stats_mt.index = ["Permaneceu", "Saiu"]
    print(stats_mt)
    print()
else:
    print("Coluna 'Meses_Contratado' ou 'Evasao' não encontrada no DataFrame.")

print("Analise numerica de churn concluida.")
