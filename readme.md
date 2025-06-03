# Telecom Churn Analysis 🚀

> **Projeto Profissional de Análise de Churn (Evasão de Clientes) para a Telecom X**  
>
> **Autor:** Mauro Roberto Barbosa Cahu  
> **E-mail:** maurocahu@gmail.com  
> **LinkedIn:** [mauro-cahu](https://www.linkedin.com/in/mauro-cahu-159a05273/)  
> **Data:** Junho 2025  

---

## 🔎 Visão Geral

O **Telecom Churn Analysis** é um projeto completo que visa entender, de forma profunda e orientada a dados, os fatores que levam clientes a cancelarem seus serviços na Telecom X. Com base em técnicas de ETL, limpeza de dados, análise exploratória (EDA) e geração de insights, fornecemos um pipeline robusto que auxilia equipes de marketing, retenção e produto a tomar decisões estratégicas para reduzir significativamente a taxa de churn.

### Principais Objetivos

1. **Extrair e preparar** os dados brutos de clientes (informações demográficas, tipos de serviço, histórico de faturamento).  
2. **Limpar e transformar** os dados para garantir coerência, correção de inconsistências e seleção de features relevantes.  
3. **Analisar exploratoriamente** a distribuição de churn em variáveis demográficas, econômicas e comportamentais.  
4. **Gerar visualizações** (gráficos, tabelas de frequência, heatmaps, boxplots, histogramas) que evidenciem padrões de evasão.  
5. **Fornecer insights** e recomendações práticas para a estratégia de retenção de clientes.  

---

## 📌 Tecnologias Utilizadas

- **Linguagem de Programação**: Python 3.11  
- **Bibliotecas de Análise de Dados**:
  - `pandas` (manipulação e tratamento de DataFrames)  
  - `numpy` (operações numéricas)  
  - `python-dateutil`, `pytz` (manipulação de datas)  
- **Visualização**:
  - `matplotlib` (gráficos estáticos)  
  - `seaborn` (visualizações estatísticas avançadas)  
- **Comunicação com a Web**:
  - `requests` (extração de dados via API/JSON)  
- **Ambiente Virtual**:
  - `venv` (isolamento de dependências)  
- **Notebook Interativo**:
  - Jupyter Notebook (relatório final estruturado)  

---

## 🎯 Funcionalidades

1. **ETL Completo**  
   - Download e normalização de dados JSON diretamente do repositório oficial da Telecom X.  
   - Conversão para DataFrame Pandas e exportação inicial para CSV.  

2. **Data Quality Checks**  
   - Identificação e tratamento de valores ausentes (missing values).  
   - Remoção de registros duplicados.  
   - Verificação de tipos de dados e consistência de formatos.  

3. **Data Cleaning & Feature Engineering**  
   - Padronização de strings (strip, lower) em colunas categóricas.  
   - Correção de valores inconsistentes (mapeamento “yes/no” → 1/0).  
   - Criação de colunas derivadas, como **Cobranca_Diaria** (faturamento mensal dividido por 30).  
   - Filtragem e seleção de colunas mais relevantes para churn.  

4. **Data Transformation & Tradução**  
   - Renomeação de colunas para português (ex.: `customerID` → `ID_Cliente`, `Churn` → `Evasao`).  
   - Conversão de valores binários (Sim/Não) para 1/0.  
   - Tradução de categorias técnicas (ex.: “fiber optic” → “Fibra Óptica”) para facilitar o entendimento de stakeholders.  

5. **Análise Exploratória de Dados (EDA)**  
   - **Distribuição Geral de Churn**: gráficos de barras e pizza para quantificar porcentagens de evasão.  
   - **Churn por Variáveis Categóricas**: countplots e tabelas de crosstab para categorias como Gênero, Idoso, Tipo_Contrato, Método_Pagamento, Tipo_Internet, entre outras.  
   - **Análise Numérica de Churn**: boxplots e histogramas comparativos de `Cobranca_Total` e `Meses_Contratado` entre clientes que permaneceram (Evasao=0) e os que saíram (Evasao=1), incluindo visualizações com **zoom no 95º percentil** e **escala logarítmica**.  
   - **Heatmap de Correlação**: mapa de calor das correlações entre variáveis numéricas para identificar relações lineares.  

6. **Relatório Interativo em Notebook**  
   - Integração de texto descritivo, código e figuras no **`TelecomX_Churn_Analysis.ipynb`**, facilitando a reprodução dos resultados e a comunicação com times de negócio.  
   - Seções bem estruturadas: Introdução, Metodologia, Resultados, Insights e Recomendações.  

7. **Recomendações de Ação**  
   - Identificação de perfis de risco (clientes até 12 meses de contrato, gastos no 75º percentil, etc.).  
   - Sugestões de campanhas de retenção (descontos em planos anuais, incentivos a pagamento automático, melhoria de suporte técnico para Fibra Óptica).  
   - Criação de “Escala de Risco de Churn” e plano de monitoramento contínuo (painel de indicadores em BI).  

---

## 🗂 Estrutura de Pastas

