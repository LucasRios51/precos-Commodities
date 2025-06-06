# 📊 Projeto de Coleta e Transformação de Dados de Commodities

Este projeto tem como objetivo coletar dados de preços de **commodities financeiras** (como petróleo, ouro, soja, entre outros) utilizando a biblioteca `yfinance` com Python, e realizar transformações analíticas utilizando o **DBT (Data Build Tool)**, estruturando os dados para análise em um Data Warehouse.

---

## 🔍 Visão Geral

### 📈 Coleta com yFinance

A primeira etapa do pipeline consiste na extração dos dados de commodities via **API do Yahoo Finance**, utilizando a biblioteca `yfinance`. Os dados obtidos incluem:

- Preço de abertura, fechamento, máximo e mínimo
- Volume negociado
- Variação percentual

Essas informações são salvas em formato estruturado (CSV ou banco de dados) para posterior transformação.

### 🧱 Transformação com DBT

O projeto utiliza **DBT Core** para organizar e transformar os dados coletados. A arquitetura é dividida em:

- **Staging**: Limpeza e preparação dos dados de commodities e movimentações
- **Datamart**: Criação de modelos analíticos finais para uso em dashboards e relatórios

#### Estrutura Resumida:

```plaintext
├── seeds/
│   └── movimentacao_commodities.csv
├── models/
│   ├── staging/
│   │   ├── stg_commodities.sql
│   │   └── stg_movimentacao_commodities.sql
│   └── datamart/
│       └── dm_commodities.sql
