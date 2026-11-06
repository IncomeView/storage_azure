# Storage Azure - Execution Flow

## Objetivo

Transformar datasets produzidos por projetos analíticos em ativos governados publicados no Azure Data Lake Storage Gen2.

Arquitetura principal:

```text
 Inflation Analytics Brasil
            ↓
        PostgreSQL
            ↓
       storage_azure
            ↓
         Registry
            ↓
         Metadata
            ↓
         Parquet
            ↓
        ADLS Gen2
            ↓
        Power BI
```


<br><br>

============================================================
ETAPA 00 - GOVERNANÇA
============================================================

- Pergunta: Este objeto deve ser publicado?  
Nem toda tabela ou view do PostgreSQL
deve ser enviada ao ADLS.

Critério:

```text
    PostgreSQL
        ↓
    Governança
        ↓
     Registry
        ↓
    Publicação
```

Somente datasets registrados
podem ser publicados.

Exemplos:

✅ ipca_geral  
✅ ipca_grupos  
✅ ipca_itens  
✅ vw_ipca_hierarquia  
✅ vw_ipca_taxonomia  
❌ vw_tmp_import  
❌ vw_validation  
❌ vw_debug  

O Registry representa o catálogo oficial
da plataforma.


<br><br>

------------------------------------------------------------
ETAPA 01 - REGISTRY
------------------------------------------------------------

Arquivo: `datasets/registry.py`

- Responsabilidade: Catálogo oficial dos datasets.

Define:

- schema
- table
- project
- domain
- owner
- container
- layer
- format

Exemplo:

ipca_geral

Sem estar no Registry um dataset não pode ser publicado.


<br><br>

------------------------------------------------------------
ETAPA 02 - CATALOG
------------------------------------------------------------

Arquivo: `datasets/catalog.py`

- Responsabilidade: Descoberta dos datasets registrados.

Funções:

- list_datasets()
- list_projects()
- list_domains()
- describe_dataset()

Objetivo:

Permitir navegação lógica dos datasets sem acessar diretamente o banco ou o Data Lake.


<br><br>

------------------------------------------------------------
ETAPA 03 - POSTGRESQL
------------------------------------------------------------

Arquivo: `database/postgres.py`

- Responsabilidade: Conexão com PostgreSQL.

Funções:

- get_engine()
- list_tables()
- read_table()

Fluxo:

```text
    PostgreSQL
        ↓
    DataFrame
```

<br><br>

------------------------------------------------------------
ETAPA 04 - METADATA
------------------------------------------------------------

Arquivo: `datasets/metadata.py`

- Responsabilidade: Gerar metadados do dataset.

Informações geradas:

- dataset
- schema
- table
- project
- domain
- layer
- rows
- columns
- exported_at

Resultado:

dataset.metadata.json


<br><br>

------------------------------------------------------------
ETAPA 05 - PARQUET
------------------------------------------------------------

Arquivo: `parquet/writer.py`

- Responsabilidade: Persistir DataFrames em formato Parquet.

Resultado:

dataset.parquet


<br><br>

------------------------------------------------------------
ETAPA 06 - EXPORT DATASET
------------------------------------------------------------

Arquivo: `pipelines/export_dataset.py`

- Responsabilidade: Extrair uma tabela específica do PostgreSQL.

Fluxo:

```text
    PostgreSQL
        ↓
    DataFrame
        ↓
    Parquet
```


<br><br>

------------------------------------------------------------
ETAPA 07 - EXPORT SCHEMA
------------------------------------------------------------

Arquivo: `pipelines/export_schema.py`

- Responsabilidade: Exportar todas as tabelas de um schema.

Exemplo:

```text
    schema bcb
        ↓
 todos os datasets
        ↓
     parquet
```


<br><br>

------------------------------------------------------------
ETAPA 08 - PUBLISH DATASET
------------------------------------------------------------

Arquivo: `pipelines/publish_dataset.py`

- Responsabilidade: Publicar um dataset governado.

Fluxo:

```text
     Registry
        ↓
    PostgreSQL
        ↓
     Metadata
        ↓
     Parquet
```

Resultado:

- dataset.parquet
- dataset.metadata.json


<br><br>

------------------------------------------------------------
ETAPA 09 - PUBLISH PROJECT
------------------------------------------------------------

Arquivo: `pipelines/publish_project.py`

- Responsabilidade: Publicar todos os datasets pertencentes a um projeto.

Exemplo:

- inflation_bcb

Resultado:

- ipca_geral
- ipca_grupos
- ipca_itens
- ipca_subgrupos
- ipca_subitens


<br><br>

------------------------------------------------------------
ETAPA 09.1 - OPERATIONAL SCRIPTS
------------------------------------------------------------

Diretório: `scripts/`

- Responsabilidade: Operar a plataforma.

Arquivos:

- `publish_dataset.py`
- `publish_project.py`
- `publish_all_projects.py`
- `upload_dataset.py`
- `upload_project.py`
- `upload_all_projects.py`
- `generate_project_knowledge_base.py`


<br><br>

------------------------------------------------------------
ETAPA 10 - AZURE AUTHENTICATION
------------------------------------------------------------

Arquivo: `azure/auth.py`

- Responsabilidade: Autenticação no Azure.

Utiliza:

- Service Principal
- Azure Entra ID

Resultado:

- Credential


<br><br>

------------------------------------------------------------
ETAPA 11 - ADLS CLIENT
------------------------------------------------------------

Arquivo: `azure/adls.py`

- Responsabilidade: Conectar ao Azure Data Lake Storage Gen2.

Resultado:

- DataLakeServiceClient


<br><br>

------------------------------------------------------------
ETAPA 12 - DATA LAKE DISCOVERY
------------------------------------------------------------

Arquivo: `azure/containers.py`

- Responsabilidade: Explorar o Data Lake.

Funções:

- list_containers()
- list_paths()
- list_project_files()
- dataset_exists()

Objetivo:

- Descobrir datasets já publicados.


<br><br>

------------------------------------------------------------
ETAPA 12.1 - DISCOVERY
------------------------------------------------------------

- Responsabilidade: Descobrir e validar datasets já publicados.

Funções:
- `list_containers()`
- `list_paths()`
- `list_project_files()`
- `dataset_exists()`

Objetivo: Permitir navegação e auditoria do Data Lake.


<br><br>

------------------------------------------------------------
ETAPA 13 - UPLOAD DATASET
------------------------------------------------------------

Arquivo: `azure/upload_dataset.py`

- Responsabilidade: Enviar um dataset para o Data Lake.

Fluxo:

```text
     Parquet
        ↓
      ADLS
```

Resultado:

- dataset.parquet
- dataset.metadata.json

publicados no Azure.


<br><br>

------------------------------------------------------------
ETAPA 14 - UPLOAD PROJECT
------------------------------------------------------------

Arquivo: `azure/upload_project.py`

- Responsabilidade: Enviar todos os datasets de um projeto.

Exemplo:

```python
upload_project(
    "inflation_bcb"
)
```

Resultado:

- Todos os datasets do projeto publicados.


<br><br>


============================================================
EXECUÇÃO OPERACIONAL
============================================================

DATASET
- make publish-dataset DATASET=ipca_geral
- make upload-dataset DATASET=ipca_geral

PROJETO
- make publish-project PROJECT=inflation_bcb
- make upload-project PROJECT=inflation_bcb

PLATAFORMA
- make publish-all
- make upload-all

DISCOVERY
- make discover

DOCUMENTAÇÃO
- make knowledge

EXECUÇÃO COMPLETA
- make all

<br><br>

------------------------------------------------------------
ESTRUTURA ADLS
------------------------------------------------------------

Container: `economics`

Estrutura:

```text
economics/
└── gold/
    └── inflation_bcb/
        │
        ├── ipca_geral.parquet
        ├── ipca_geral.metadata.json
        │
        ├── ipca_grupos.parquet
        ├── ipca_grupos.metadata.json
        │
        ├── ipca_itens.parquet
        ├── ipca_itens.metadata.json
        │
        ├── ipca_subgrupos.parquet
        ├── ipca_subgrupos.metadata.json
        │
        └── ipca_subitens.parquet
        └── ipca_subitens.metadata.json
```



<br><br>

------------------------------------------------------------
EXECUÇÃO COMPLETA
------------------------------------------------------------

```text
     Inflation Analytics Brasil
                ↓
            PostgreSQL
                ↓
             Registry
                ↓
         Publish Dataset
                ↓
         Publish Project
                ↓
        Publish All Projects
                ↓
             Metadata
                ↓
             Parquet
                ↓
          Upload Dataset
                ↓
          Upload Project
                ↓
        Upload All Projects
                ↓
            ADLS Gen2
                ↓
            Power BI
```