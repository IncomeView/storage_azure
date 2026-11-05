# Storage Azure Architecture

## Objetivo

Publicar datasets governados produzidos por projetos analíticos.

## Fluxo

```text
Project
    ↓
PostgreSQL
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

## Estrutura ADLS

```text
economics/
└── gold/
    └── inflation_bcb/
```

## Artefatos

Cada dataset possui:

```text
.parquet

.metadata.json
```