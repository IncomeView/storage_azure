# ☁️ storage_azure

### Datast Publishing Platform for Azure Data Lake Storage Gen2

![Python](https://img.shields.io/badge/Python-3.12+-yellow)
![Azure](https://img.shields.io/badge/Azure-ADLS_Gen2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<br><Br>

## 🎯 Objetivo

O **storage_azure** é uma plataforma de publicação de datasets analíticos projetada para transformar bases relacionais em ativos governados e distribuíveis.

O projeto desacopla a produção dos dados da sua distribuição, permitindo que aplicações analíticas publiquem datasets padronizados em:

- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Parquet
- Power BI
- Ferramentas analíticas futuras

<br><Br>

## 🏗️ Filosofia

O storage_azure não coleta dados.

A responsabilidade de coleta, transformação e modelagem permanece nos projetos de domínio.

Exemplo:

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
         Registry
            │
            ▼
         Metadata
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

<br><Br>

## 📦 Conceitos Principais

### Dataset

Unidade de publicação da plataforma.

Exemplo:

```python
publish_dataset(
    "ipca_geral"
)
```

<br>

### Projeto

Conjunto de datasets.

Exemplo:

```python
publish_project(
    "inflation_bcb"
)
```

<br>

### Registry

Catálogo oficial dos datasets.

Exemplo:

```python
DATASETS = {
    "ipca_geral": {
        "schema": "bcb",
        "table": "ipca_geral",
        "project": "inflation_bcb",
        "domain": "economics",
        "owner": "IncomeView",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    }
}
```

<br>

### Metadata

Todo dataset publicado possui:

```text
dataset
schema
table
project
domain
owner
container
layer
rows
columns
exported_at
```

<br><Br>

## 🔄 Dataset Lifecycle

```text
    Registry
        │
        ▼
    Metadata
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

<br><Br>

## 📂 Arquitetura

```text
src.
    storage_azure
    │
    ├── azure
    │   ├── auth.py
    │   ├── adls.py
    │   ├── containers.py
    │   ├── contracts.py
    │   ├── upload.py
    │   └── upload_project.py
    │
    ├── database
    │   └── postgres.py
    │
    ├── datasets
    │   ├── registry.py
    │   ├── catalog.py
    │   ├── metadata.py
    │   └── path_builder.py
    │
    ├── parquet
    │   └── writer.py
    │
    ├── pipelines
    │   ├── export_dataset.py
    │   ├── export_schema.py
    │   ├── publish_dataset.py
    │   └── publish_project.py
    │
    └── settings.py
```

<br><Br>

## ☁️ Azure

Tecnologias utilizadas:

- Azure Entra ID
- Azure Identity
- Azure Storage SDK
- Azure Data Lake Storage Gen2

Estrutura padrão:

```text
economics
└── gold
    └── inflation_bcb
        ├── ipca_geral.parquet
        ├── ipca_geral.metadata.json
        ├── ipca_grupos.parquet
        ├── ipca_grupos.metadata.json
        └── ...
```

<br><Br>

## 📊 Casos de Uso

### Publicar Dataset

```python
publish_dataset(
    "ipca_geral"
)
```

<br>

### Publicar Projeto

```python
publish_project(
    "inflation_bcb"
)
```

<br>

### Upload Dataset

```python
upload_dataset(
    "ipca_geral"
)
```

<br>

### Upload Projeto

```python
upload_project(
    "inflation_bcb"
)
```

<br><Br>

## ✅ Funcionalidades Implementadas

### Governança

- Dataset Registry
- Metadata Catalog
- Dataset Contracts
- Dataset Ownership
- Layer Classification

### Engenharia de Dados

- PostgreSQL Integration
- Dataset Export
- Schema Export
- Parquet Generation

### Cloud

- Azure Authentication
- Azure RBAC
- ADLS Gen2
- Dataset Upload
- Project Upload

<br><Br>

## 🔧 Tecnologias

### Dados

- PostgreSQL
- Parquet
- Pandas
- PyArrow

### Cloud

- Azure Entra ID
- Azure Identity
- ADLS Gen2

### Engenharia

- Python
- Git
- GitHub
- Pipelines

<br><Br>

## 🚀 Roadmap

### ✅ V1 - Dataset Publishing Platform

- [x] PostgreSQL integration
- [x] Dataset Registry
- [x] Metadata Catalog
- [x] Dataset Governance
- [x] Parquet Generation
- [x] Publish Dataset
- [x] Publish Project
- [x] Azure Authentication
- [x] ADLS Gen2 Integration
- [x] Upload Dataset
- [x] Upload Project

### 🔄 V1.1 - Data Governance

- [ ] Dataset Lineage
- [ ] Dataset Versioning
- [ ] Dataset Validation
- [ ] Data Quality Checks
- [ ] Dataset Statistics

### 🔄 V2 - Analytics Delivery

- [ ] Power BI Integration
- [ ] Incremental Publishing
- [ ] Dataset Monitoring
- [ ] Observability
- [ ] CLI Commands

### 🔮 V3 - Enterprise Data Platform

- [ ] Multi-project Support
- [ ] Data Contracts
- [ ] OpenMetadata Integration
- [ ] Automated Knowledge Base

<br><Br>

## 🔗 Projetos Relacionados

### Inflation Analytics Brasil

Plataforma analítica de inflação e política monetária responsável pela produção dos datasets econômicos.

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
         ADLS Gen2
            │
            ▼
         Power BI
```

<br><Br>

## 👤 Autor

Moacir Magalhães Faria

Data Engineering • Data Governance • Analytics • Econometrics • Machine Learning