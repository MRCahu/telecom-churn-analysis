````markdown
# 📊 Telecom X – Análise de Churn

> **Entenda, explique e aja** — um pipeline de dados completo que revela **por que** clientes cancelam serviços de telecomunicações e **como** reverter essa tendência.

---

## 1. Visão Geral

Este repositório apresenta um estudo de churn para a empresa fictícia **Telecom X**.  
O fluxo de trabalho segue as etapas:

> **ETL → Limpeza → Transformação → EDA → Insights → Recomendações**

Demonstramos boas práticas de engenharia e ciência de dados em Python — do _raw data_ até insights acionáveis.

---

## 2. Propósito da Análise

- **Identificar fatores críticos** que impulsionam o cancelamento de clientes.  
- **Mensurar o impacto** de variáveis financeiras (ex.: `Cobranca_Total`) e contratuais (ex.: `Meses_Contratado`).  
- **Gerar recomendações** para as equipes de Marketing, Produto e Suporte ao Cliente.  

---

## 3. Tecnologias & Bibliotecas

| Camada               | Ferramentas / Bibliotecas                          |
| -------------------- | -------------------------------------------------- |
| Linguagem            | **Python 3.11+**                                   |
| Manipulação de dados | `pandas`, `numpy`                                  |
| Visualização         | `matplotlib`, `seaborn`                            |
| Ambiente             | Jupyter Notebook · ambiente virtual **`.venv`**    |
| Controle de versão   | **Git ∙ GitHub**                                   |

---

## 4. Estrutura do Projeto

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
└── README.md
````

> **Boa prática:** manter a separação **dados | código | relatórios** garante projetos escaláveis e reprodutíveis.

---

## 5. Exemplos de Gráficos & Insights

| Gráfico                                                        | Insight resumido                                                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| ![Boxplot Churn vs. Cobrança Total](reports/churn_boxplot.png) | **Clientes que cancelam** pagam, em média, R\$ 38 a mais por mês do que os que permanecem.         |
| ![Histograma Cobrança Total](reports/cobranca_hist.png)        | Distribuição assimétrica sugere **segmento premium** com maior risco de churn.                     |
| ![Heatmap de Correlação](reports/corr_heatmap.png)             | Forte correlação `Cobranca_Mensal` × `Cobranca_Total`; fraca correlação tempo de contrato × churn. |

### Descobertas-chave

* Tarifas altas ampliam churn em até **24 p.p.** no primeiro ano.
* Clientes **sem combo (internet + TV)** têm **2×** mais chance de cancelar.
* Programas de fidelidade reduzem churn em **15 %** após o 6.º mês.

---

## 6. Como Executar

1. **Clone o repositório**

   ```bash
   git clone https://github.com/MRCahu/TelecomX-Churn-Analysis.git
   cd TelecomX-Churn-Analysis
   ```

2. **Crie o ambiente virtual**

   ```bash
   python -m venv .venv
   # Linux/macOS
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o pipeline**

   ```bash
   # ETL
   python src/load_telecom_data.py
   # Qualidade
   python src/data_quality_checks.py
   # Limpeza / Transformação
   python src/data_cleaning.py
   python src/data_transformation.py
   # Análise exploratória
   python src/exploratory_analysis.py
   python src/churn_numeric_analysis.py   # opcional
   ```

5. **Abra o notebook**

   ```bash
   jupyter notebook notebooks/TelecomX_Churn_Analysis.ipynb
   ```

> Todos os gráficos são salvos automaticamente em **`reports/`**.

---

## 7. Conclusões & Recomendações

* **Reprecificação inteligente** para clientes sensíveis a preço.
* **Bundles de serviços** (TV + Internet) reduzem a probabilidade de churn.
* **Programas de fidelidade** após 6 meses diminuem cancelamentos em 15 %.
* **Monitoramento contínuo** com métricas de satisfação (NPS) no próximo ciclo.

---

## 8. Licença

Distribuído sob a licença **MIT** — consulte [`LICENSE`](LICENSE) para detalhes.

---

## 9. Contato

| Campo        | Informação                                                                                |
| ------------ | ----------------------------------------------------------------------------------------- |
| **Autor**    | **Mauro Roberto Barbosa Cahu**                                                            |
| **E-mail**   | [maurocahu@gmail.com](mailto:maurocahu@gmail.com)                                         |
| **Telefone** | +55 (81) 99292-2415                                                                       |
| **LinkedIn** | [linkedin.com/in/mauro-cahu-159a05273](https://www.linkedin.com/in/mauro-cahu-159a05273/) |
| **GitHub**   | [github.com/MRCahu](https://github.com/MRCahu)                                            |
| **Cidade**   | Recife / PE – Brasil                                                                      |

Feedbacks e *pull requests* são muito bem-vindos — vamos aprimorar a análise de churn juntos 🚀

```
```
