# ☁️ storage_azure

### Publishing Layer for Analytical Datasets on zure Data Lake Storage Gen2

![Python](https://img.shields.io/badge/Python-3.12+-yellow)
![Azure](https://img.shields.io/badge/Azure-ADLS_Gen2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<br><br>

## 🎯 Objetivo

O **storage_azure** é uma camada reutilizável de engenharia de dados responsável por publicar datasets analíticos em ambientes Azure.

O projeto foi criado para desacoplar a geração de dados da sua distribuição e armazenamento, permitindo que projetos analíticos utilizem uma infraestrutura única para publicação em:

- Azure Data Lake Storage Gen2 (ADLS)
- Parquet
- Power BI
- Ferramentas analíticas futuras

<br><Br>

## 🏗️ Filosofia

O objetivo do projeto não é coletar dados.  
A coleta e transformação permanecem nos projetos de domínio.

Por exemplo:

```text
Inflation Analytics Brasil
            │
            ▼
        PostgreSQL
            │
            ▼
      storage_azure
            │
            ▼
         Parquet
            │
            ▼
        ADLS Gen2
            │
            ▼
        Power BI
```

Dessa forma:

- inflation_bcb produz conhecimento
- storage_azure distribui dados

<br><br>


## 📦 Casos de Uso

- **Exportar uma tabela PostgreSQL**

```python
export_table(
    schema="bcb",
    table="ipca_geral"
)
```

- **Gerar arquivo Parquet**

```python
save_parquet(df)
```

<br>

- **Publicar dataset no ADLS**

```python
upload_parquet(
    local_file,
    container="economics"
)
```

<br>

- **Exportar um schema inteiro**

```python
export_schema("bcb")
```

<br><br>

## 📂 Arquitetura

```text
.src
    publishing
    │
    ├── azure
    │   ├── auth.py
    │   ├── adls.py
    │   └── containers.py
    │
    ├── database
    │   └── postgres.py
    │
    ├── datasets
    │   ├── registry.py
    │   └── metadata.py
    │
    ├── parquet
    │   └── writer.py
    │
    ├── pipelines
    │   └── export_dataset.py
    │
    └── cli.py
```

<Br><br>

## 🔄 Fluxo de Dados

```text
    PostgreSQL
        │
        ▼
    DataFrame
        │
        ▼
     Parquet
        │
        ▼
    ADLS Gen2
        │
        ▼
     Power BI
```

<br><br>

## ☁️ Azure

O projeto utiliza:

- Azure Data Lake Storage Gen2
- Azure Identity
- Azure Entra ID
- Service Principal ou DefaultAzureCredential

Suporta:

- Local Development
- GitHub Actions
- Azure Cloud


<br><br>

## 📁 Organização dos Dados

Estrutura sugerida:

```text
    economics/
    │
    ├── ipca/
    ├── selic/
    ├── expectations/
    └── features/
```

ou

```text
    bronze/
    silver/
    gold/
```

dependendo da estratégia adotada.

<br><br>

## 🔧 Tecnologias

- Python
- Pandas
- PyArrow
- PostgreSQL
- Azure SDK
- ADLS Gen2
- GitHub Actions

<br><Br>

## 🚀 Roadmap

### V1

- [ ] Exportar tabela PostgreSQL
- [ ] Gerar Parquet
- [ ] Upload para ADLS
- [ ] Configuração por .env

### V1.1

- [ ] Exportar schema completo
- [ ] Registro de datasets
- [ ] Metadata catalog

### V2

- [ ] Versionamento de datasets
- [ ] Data Lineage
- [ ] Qualidade de dados
- [ ] Integração automática com Power BI

<br><Br>

## 🔗 Projetos Relacionados

### Inflation Analytics Brasil

Projeto de analytics, econometria e machine learning responsável pela produção dos datasets econômicos.

Fluxo:

```text
 Inflation Analytics Brasil
            │
            ▼
        PostgreSQL
            │
            ▼
      storage_azure
            │
            ▼
          ADLS
            │
            ▼
        Power BI
```

<br><br>

## 👤 Autor

Moacir Magalhães Faria

Data Engineering • Analytics • Econometrics • Machine Learning