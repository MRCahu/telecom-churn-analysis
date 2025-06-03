# Telecom Churn Analysis

## Descrição
Projeto de análise de churn (evasão de clientes) para a Telecom X.  
Este repositório contém todo o pipeline — desde ETL e limpeza de dados até análise exploratória e recomendações — para identificar fatores que influenciam o cancelamento de clientes.

## Estrutura do Projeto
telecom-churn-analysis/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│ ├── raw/
│ │ └── TelecomX_Data.json
│ ├── clean/
│ │ ├── telecom_churn_cleaned.csv
│ │ ├── telecom_churn_features.csv
│ │ └── telecom_churn_transformed.csv
│ └── …
├── reports/
│ ├── boxplot_cobranca_total_churn.png
│ ├── hist_cobranca_total_churn.png
│ ├── boxplot_meses_contratado_churn.png
│ ├── hist_meses_contratado_churn.png
│ ├── heatmap_correlation.png
│ └── … (outros PNGs gerados)
├── src/
│ ├── load_telecom_data.py
│ ├── data_quality_checks.py
│ ├── data_cleaning.py
│ ├── data_transformation.py
│ ├── exploratory_analysis.py
│ ├── churn_numeric_analysis.py
│ └── … (outros scripts Python)
└── TelecomX_Churn_Analysis.ipynb

- **`.gitignore`**: define quais arquivos/pastas não devem ser versionados pelo Git (por exemplo, `.venv/`, arquivos temporários etc.).
- **`README.md`**: este arquivo, com instruções sobre o projeto.
- **`requirements.txt`**: lista de dependências Python usadas no projeto.
- **`data/`**:
  - **`raw/`**: dados brutos (JSON original).
  - **`clean/`**: dados intermediários tratados (CSV).
- **`reports/`**: gráficos gerados pela análise (PNG).
- **`src/`**: scripts Python que fazem ETL, limpeza, transformação e EDA.
- **`TelecomX_Churn_Analysis.ipynb`**: notebook final com relatório completo.

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/SEU_USUARIO/telecom-churn-analysis.git
   cd telecom-churn-analysis