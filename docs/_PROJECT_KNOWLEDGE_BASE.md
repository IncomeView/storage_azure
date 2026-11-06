# STORAGE AZURE KNOWLEDGE BASE

Generated: 2026-11-06 09:29:58

---

## Executive Summary

Storage Azure is a data publishing platform responsible for transforming analytical datasets into governed assets stored in Azure Data Lake Storage Gen2.

- project_name: storage_azure
- datasets: 6
- projects: 1
- domains: 1
- containers: 1
- layers: 1
- python_files: 43
- markdown_files: 3
- files: 49

---

## Project Mission

The platform decouples data production from data distribution.

Projects produce data. Storage Azure publishes data.

---

## Architecture

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

---

## Dataset Lifecycle

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

---

## Project Structure

```text
storage_azure
├── docs
│   ├── architecture.md
│   └── execution_flow.md
├── exports
├── scripts
│   └── generate_project_knowledge_base.py
├── src
│   ├── storage_azure
│   │   ├── azure
│   │   │   ├── __init__.py
│   │   │   ├── adls.py
│   │   │   ├── auth.py
│   │   │   ├── containers.py
│   │   │   ├── contracts.py
│   │   │   ├── upload_dataset.py
│   │   │   └── upload_project.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   └── postgres.py
│   │   ├── datasets
│   │   │   ├── __init__.py
│   │   │   ├── catalog.py
│   │   │   ├── metadata.py
│   │   │   ├── path_builder.py
│   │   │   └── registry.py
│   │   ├── parquet
│   │   │   ├── __init__.py
│   │   │   └── writer.py
│   │   ├── pipelines
│   │   │   ├── __init__.py
│   │   │   ├── export_dataset.py
│   │   │   ├── export_schema.py
│   │   │   ├── publish_dataset.py
│   │   │   └── publish_project.py
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   └── settings.py
│   └── storage_azure.egg-info
├── tests
│   ├── test_azure_connection.py
│   ├── test_catalog.py
│   ├── test_connection.py
│   ├── test_containers.py
│   ├── test_dataset_exists.py
│   ├── test_export_ipca.py
│   ├── test_export_schema.py
│   ├── test_generate_metadata.py
│   ├── test_metadata.py
│   ├── test_metadata_file.py
│   ├── test_paths.py
│   ├── test_pipeline.py
│   ├── test_project_files.py
│   ├── test_publish_dataset.py
│   ├── test_publish_project.py
│   ├── test_upload_dataset.py
│   ├── test_upload_file.py
│   └── test_upload_project.py
├── .gitignore
├── Makefile
├── pyproject.toml
└── README.md
```

---

## Catalog

### Projects

- inflation_bcb

### Domains

- economics

### Containers

- economics

### Layers

- gold

---

## Registered Datasets

### ipca_geral

- schema: bcb
- dataset_type: table
- table: ipca_geral
- description: IPCA geral
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

### ipca_grupos

- schema: bcb
- dataset_type: table
- table: ipca_grupos
- description: IPCA por grupos
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

### ipca_subgrupos

- schema: bcb
- dataset_type: table
- table: ipca_subgrupos
- description: IPCA por subgrupos
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

### ipca_itens

- schema: bcb
- dataset_type: table
- table: ipca_itens
- description: IPCA por itens
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

### ipca_subitens

- schema: bcb
- dataset_type: table
- table: ipca_subitens
- description: IPCA por subitens
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

### ipca_taxonomia

- schema: bcb
- dataset_type: table
- table: ipca_taxonomia
- description: taxonomia ipca por subitens
- project: inflation_bcb
- owner: IncomeView
- domain: economics
- container: economics
- layer: gold
- format: parquet

---

## Pipelines

- **export_dataset**: PostgreSQL → Parquet
- **export_schema**: Schema PostgreSQL → Parquet
- **publish_dataset**: Registry → Metadata → Parquet
- **publish_project**: Projeto → Datasets
- **upload_dataset**: Dataset → ADLS
- **upload_project**: Projeto → ADLS

---

## Azure Architecture

- economics/gold/inflation_bcb

---

## ADLS Layout

```text
economics
└── gold
    └── inflation_bcb
```

---

## Roadmap


### V1
- Dataset Registry
- Metadata Catalog
- Publish Dataset
- Publish Project
- Azure Authentication
- ADLS Integration

### V1.1
- Dataset Versioning
- Dataset Lineage
- Dataset Statistics
- Data Quality Checks
- Automated Knowledge Base

### V2
- Power BI Integration
- Incremental Publishing
- Monitoring
- Observability

### V3
- Multi-project Support
- OpenMetadata Integration
- Data Contracts
