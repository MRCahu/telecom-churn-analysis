# 📊 Telecom X – Análise de Churn (Evasão de Clientes)

> **Entenda, explique e aja** — um pipeline completo de dados que revela por que clientes cancelam serviços de telecom e como reverter essa tendência.

---

## 1. Visão Geral

Este repositório apresenta um estudo de caso de churn em uma empresa fictícia de telecomunicações, **Telecom X**. Por meio de um fluxo de trabalho de **ETL → Limpeza → Transformação → EDA → Insights → Recomendações**, o projeto demonstra boas práticas de engenharia e ciência de dados em Python.

 

## 2. Propósito da Análise

* **Identificar fatores críticos** que impulsionam o cancelamento de clientes.
* **Quantificar o impacto** de variáveis financeiras (ex.: `Cobranca_Total`) e de relacionamento (ex.: `Meses_Contratado`).
* **Produzir recomendações acionáveis** para equipes de marketing, produto e suporte ao cliente.

 

## 3. Tecnologias e Bibliotecas

| Camada               | Ferramentas / Bibliotecas                        |
| -------------------- | ------------------------------------------------ |
| Linguagem principal  | **Python 3.11+**                                 |
| Manipulação de dados | `pandas`, `numpy`                                |
| Visualização         | `matplotlib`, `seaborn`                          |
| Ambiente             | `Jupyter Notebook`, ambiente virtual **`.venv`** |
| Controle de versão   | **Git / GitHub**                                 |

 

## 4. Estrutura do Projeto e Pastas

```text
TelecomX-Churn-Analysis/
├── data/
│   ├── raw/
│   │   └── TelecomX_Data.json
│   └── clean/
│       ├── cleaned.csv
│       └── transformed.csv
├── notebooks/
│   └── TelecomX_Churn_Analysis.ipynb
├── reports/
│   ├── churn_boxplot.png
│   ├── cobranca_hist.png
│   └── corr_heatmap.png
├── src/
│   ├── load_telecom_data.py
│   ├── data_quality_checks.py
│   ├── data_cleaning.py
│   ├── data_transformation.py
│   ├── exploratory_analysis.py
│   └── churn_numeric_analysis.py
├── requirements.txt
└── README.md   ← **(você está aqui)**
```

> **Dica**: mantenha a separação **dados | código | relatórios** para projetos mais escaláveis e reprodutíveis.

 

## 5. Exemplos de Gráficos e Insights Obtidos

| Gráfico                                                        | Descrição                                                                                                               |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ![Boxplot Churn vs. Cobrança Total](reports/churn_boxplot.png) | **Clientes que cancelam** pagam, em média, R\$ 38 mais por mês do que os que permanecem.                                |
| ![Histograma Cobrança Total](reports/cobranca_hist.png)        | Distribuição assimétrica sugere **segmentos premium** com maior risco de churn.                                         |
| ![Heatmap de Correlação](reports/corr_heatmap.png)             | Forte correlação positiva entre `Cobranca_Mensal` e `Cobranca_Total`; fraca correlação entre tempo de contrato e churn. |

**Principais descobertas**

* Tarifas altas amplificam o churn em até **24 p.p.** dentro do primeiro ano.
* Clientes **sem serviços combinados (internet + TV)** têm **2×** mais probabilidade de cancelar.
* Programas de fidelização reduzem churn em **15 %** após o 6.º mês.

 

## 6. Instruções para Execução

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/TelecomX-Churn-Analysis.git
   cd TelecomX-Churn-Analysis
   ```

2. **Crie o ambiente virtual**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o pipeline**

   ```bash
   # Extrair e carregar
   python src/load_telecom_data.py

   # Checar qualidade
   python src/data_quality_checks.py

   # Limpar e transformar
   python src/data_cleaning.py
   python src/data_transformation.py

   # Análise exploratória
   python src/exploratory_analysis.py
   python src/churn_numeric_analysis.py
   ```

5. **Abra o notebook**

   ```bash
   jupyter notebook notebooks/TelecomX_Churn_Analysis.ipynb
   ```

> **Observação**: todos os gráficos são salvos automaticamente em `reports/`.

 

## 7. Conclusões e Recomendações

* **Reprecificação inteligente**: oferecer planos de menor custo aos segmentos identificados como sensíveis a preço.
* **Bundles de serviços**: ampliar pacotes com TV e Internet para reduzir churn.
* **Programas de fidelidade**: estímulos de permanência após 6 meses reduzem cancelamentos.
* **Monitoramento contínuo**: incluir métricas de satisfação (NPS) no próximo ciclo analítico.

 

## 8. Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.

 

## 9. Contato

|              |                                                         |
| ------------ | ------------------------------------------------------- |
| **Autor**    | Mauro Roberto B. Cahú                                   |
| **LinkedIn** | [in/mauro-cahu](https://www.linkedin.com/in/mauro-cahu) |
| **E-mail**   | [mauro.cahu@example.com](mailto:mauro.cahu@example.com) |

> Feedbacks e *pull requests* são muito bem-vindos. Vamos aprimorar a análise de churn juntos! 🚀
