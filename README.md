# Análise Selic e Crédito PF

## 1. Sobre o projeto
Este projeto investiga a relação entre a **Taxa Selic** e o **crédito concedido a pessoas físicas (PF)** no Brasil, no período de 2015 a 2024.  
Inclui análises estatísticas, regressões lineares, gráficos de dispersão, séries temporais e destaque de períodos críticos, como recessão de 2015–2016 e pandemia de 2020.

O projeto foi consolidado em um artigo publicado no **Medium**, detalhando todas as análises e interpretações.

---

## 2. Estrutura do projeto
```
Projeto/
├─ Data/
│ ├─ Raw/ 
│ │ ├─ concessoes_pf_20633.csv
│ │ ├─ selic_4189.csv
│ │ └─ taxa_juros_pf_20716.csv
│ └─ Processed/ 
│   └─ dados_processados.csv
├─ Notebooks/
│ ├─ analise.ipynb 
│ └─ etl_Notebook.ipynb
├─ src/
│ └─ etl.py 
└─ README.md
```

> **Observação:** os notebooks podem ser abertos no **Jupyter Notebook**, **VS Code** ou **Google Colab**.

---

## 3. Bibliotecas utilizadas
- `pandas` → manipulação de dados  
- `numpy` → cálculos numéricos  
- `matplotlib` e `seaborn` → visualizações gráficas  
- `statsmodels` → análise estatística e regressões  

Instalação rápida:
```bash
pip install pandas numpy matplotlib seaborn statsmodels  
``` 
---

## 4. Como usar
1. Instale as bibliotecas necessárias:
```bash
pip install pandas matplotlib seaborn statsmodels numpy
```
2. Abra os notebooks na pasta Notebooks/ ou carregue-os no Google Colab.

---

## 5. Conteúdo
- etl.ipynb / etl.py → Tratamento e organização dos dados.
- Analise.ipynb → Criação de gráficos e análises estatísticas.
- data/raw/ → Arquivos originais do Banco Central: Selic, Concessões PF, Juros PF.
- data/processed/ → Dados tratados prontos para análise.

## 6. Artigo
O projeto foi consolidado em um artigo no Medium:

🔗[https://medium.com/@lbisewski11/da-selic-ao-crédito-pessoal-uma-análise-do-impacto-da-taxa-básica-de-juros-0d4fd097ce4f]
