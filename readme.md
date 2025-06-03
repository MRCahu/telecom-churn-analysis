# 📊 Telecom X – Análise de Churn (Evasão de Clientes)

> Projeto de Ciência de Dados com foco na identificação de fatores críticos que influenciam a evasão de clientes em uma empresa fictícia de telecomunicações. Aplicação completa de um pipeline de dados — da aquisição à geração de insights acionáveis.

---

## 📌 Visão Geral

Este repositório apresenta um estudo completo sobre **Churn** (evasão de clientes) na empresa fictícia **Telecom X**. Através de um pipeline de ciência de dados, exploramos e visualizamos padrões comportamentais dos clientes, identificando variáveis que contribuem significativamente para o cancelamento de serviços.

---

## 🎯 Propósito da Análise

- Compreender os principais motivos que levam clientes a cancelar seus serviços.
- Auxiliar equipes de marketing, atendimento e produto a desenvolver estratégias de retenção.
- Demonstrar a aplicação de técnicas práticas de ETL, análise exploratória, limpeza e visualização de dados.
- Servir como portfólio técnico para cientistas de dados em início ou transição de carreira.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.x**
- **Pandas**, **NumPy** – manipulação e análise de dados
- **Matplotlib**, **Seaborn** – visualização de dados
- **Jupyter Notebook** – documentação interativa
- **Ambiente Virtual (.venv)** – isolamento do ambiente de execução
- **Git** – controle de versão

---

## 📁 Estrutura do Projeto

```plaintext
├── data/
│   ├── raw/
│   │   └── TelecomX_Data.json           # Dados originais
│   └── clean/
│       ├── cleaned.csv                  # Após limpeza
│       └── transformed.csv              # Após transformação
├── reports/
│   └── *.png                            # Gráficos gerados
├── scripts/
│   ├── load_telecom_data.py            # API → DataFrame
│   ├── data_quality_checks.py          # Verificação de dados
│   ├── data_cleaning.py                # Limpeza e padronização
│   ├── data_transformation.py          # Derivação e tradução
│   ├── exploratory_analysis.py         # Visualização de dados
│   └── churn_numeric_analysis.py       # Análise quantitativa
├── TelecomX_Churn_Analysis.ipynb       # Notebook final com insights
└── README.md
