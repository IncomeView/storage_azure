#!/usr/bin/env python3
"""
generate_project_knowledge_base.py

Knowledge Base Generator
for storage_azure

Objetivo:
- Preservar arquitetura
- Preservar governança
- Documentar datasets
- Documentar Azure
- Gerar documentação automática

Autor: Moacir Magalhães
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path

import pathspec


# =============================================================================
# CONFIG
# =============================================================================

ROOT = Path(__file__).resolve().parents[1]

OUTPUT = (
    ROOT
    / "docs"
    / "_PROJECT_KNOWLEDGE_BASE.md"
)

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True,
)

ALWAYS_IGNORE = {
    "__pycache__",
    ".git",
    ".venv",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "build",
    "dist",
}

IGNORE_EXTENSIONS = {
    ".pyc",
}

GENERATED_FILES = {
    "_PROJECT_KNOWLEDGE_BASE.md",
}


# =============================================================================
# GITIGNORE
# =============================================================================

def load_gitignore():

    gitignore = ROOT / ".gitignore"

    if not gitignore.exists():
        return None

    patterns = gitignore.read_text(
        encoding="utf-8"
    ).splitlines()

    return pathspec.PathSpec.from_lines(
        pathspec.patterns.GitWildMatchPattern,
        patterns,
    )


GIT_SPEC = load_gitignore()


def is_ignored(path: Path):

    if path.name in GENERATED_FILES:
        return True

    for part in path.parts:

        if part in ALWAYS_IGNORE:
            return True

    if GIT_SPEC is None:
        return False

    try:

        rel = (
            path
            .relative_to(ROOT)
            .as_posix()
        )

        return GIT_SPEC.match_file(rel)

    except Exception:

        return False


# =============================================================================
# DISCOVERY
# =============================================================================

def get_project_files():

    files = []

    for item in ROOT.rglob("*"):

        if not item.is_file():
            continue

        if is_ignored(item):
            continue

        if (
            item.suffix.lower()
            in IGNORE_EXTENSIONS
        ):
            continue

        files.append(item)

    return sorted(files)


def get_python_files():

    return [
        f
        for f in get_project_files()
        if f.suffix.lower() == ".py"
    ]


def get_markdown_files():

    return [
        f
        for f in get_project_files()
        if f.suffix.lower() == ".md"
    ]


# =============================================================================
# HELPERS
# =============================================================================

def relative(path: Path):

    return str(
        path.relative_to(ROOT)
    )


def safe_read(path: Path):

    try:

        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception:

        return ""


# =============================================================================
# TREE
# =============================================================================

def build_tree():

    lines = [ROOT.name]

    def walk(path, prefix=""):

        entries = []

        for item in sorted(
            path.iterdir(),
            key=lambda x: (
                x.is_file(),
                x.name.lower(),
            ),
        ):

            if is_ignored(item):
                continue

            entries.append(item)

        for idx, item in enumerate(entries):

            last = (
                idx
                == len(entries) - 1
            )

            connector = (
                "└── "
                if last
                else "├── "
            )

            lines.append(
                f"{prefix}{connector}{item.name}"
            )

            if item.is_dir():

                extension = (
                    "    "
                    if last
                    else "│   "
                )

                walk(
                    item,
                    prefix + extension,
                )

    walk(ROOT)

    return "\n".join(lines)


# =============================================================================
# FILE STATS
# =============================================================================

def count_files():

    return len(
        get_project_files()
    )


def count_python():

    return len(
        get_python_files()
    )


def count_markdown():

    return len(
        get_markdown_files()
    )

# =============================================================================
# REGISTRY
# =============================================================================

def load_registry():

    try:

        from storage_azure.datasets.registry import (
            DATASETS,
        )

        return DATASETS

    except Exception as exc:

        print(
            f"Erro ao carregar registry: {exc}"
        )

        return {}


# =============================================================================
# CATALOG
# =============================================================================

def load_catalog():

    registry = load_registry()

    projects = set()
    domains = set()
    containers = set()
    layers = set()

    for dataset in registry.values():

        project = dataset.get(
            "project"
        )

        if project:
            projects.add(project)

        domain = dataset.get(
            "domain"
        )

        if domain:
            domains.add(domain)

        container = dataset.get(
            "container"
        )

        if container:
            containers.add(container)

        layer = dataset.get(
            "layer"
        )

        if layer:
            layers.add(layer)

    return {

        "projects": sorted(projects),

        "domains": sorted(domains),

        "containers": sorted(containers),

        "layers": sorted(layers),
    }


# =============================================================================
# DATASETS
# =============================================================================

def list_registered_datasets():

    registry = load_registry()

    return sorted(
        registry.keys()
    )


def dataset_count():

    return len(
        list_registered_datasets()
    )


# =============================================================================
# AZURE STRUCTURE
# =============================================================================

def detect_azure_architecture():

    registry = load_registry()

    paths = []

    for dataset_name, dataset in (

        registry.items()

    ):

        container = dataset.get(
            "container",
            "unknown"
        )

        layer = dataset.get(
            "layer",
            "unknown"
        )

        project = dataset.get(
            "project",
            "unknown"
        )

        paths.append(
            f"{container}/{layer}/{project}"
        )

    return sorted(
        set(paths)
    )


# =============================================================================
# PROJECT SUMMARY
# =============================================================================

def generate_summary():

    catalog = load_catalog()

    return {

        "project_name": ROOT.name,

        "datasets": dataset_count(),

        "projects": len(
            catalog["projects"]
        ),

        "domains": len(
            catalog["domains"]
        ),

        "containers": len(
            catalog["containers"]
        ),

        "layers": len(
            catalog["layers"]
        ),

        "python_files": count_python(),

        "markdown_files": count_markdown(),

        "files": count_files(),
    }


# =============================================================================
# PIPELINES
# =============================================================================

PIPELINES = {

    "export_dataset":
        "PostgreSQL → Parquet",

    "export_schema":
        "Schema PostgreSQL → Parquet",

    "publish_dataset":
        "Registry → Metadata → Parquet",

    "publish_project":
        "Projeto → Datasets",

    "upload_dataset":
        "Dataset → ADLS",

    "upload_project":
        "Projeto → ADLS",
}


def get_pipelines():

    return PIPELINES


# =============================================================================
# ADLS
# =============================================================================

def generate_adls_layout():

    registry = load_registry()

    lines = []

    containers = {}

    for dataset in registry.values():

        container = dataset.get(
            "container"
        )

        layer = dataset.get(
            "layer"
        )

        project = dataset.get(
            "project"
        )

        containers.setdefault(
            container,
            {}
        )

        containers[
            container
        ].setdefault(
            layer,
            set()
        )

        containers[
            container
        ][
            layer
        ].add(project)

    for container, layers in (

        containers.items()

    ):

        lines.append(
            container
        )

        for layer, projects in (

            layers.items()

        ):

            lines.append(
                f"└── {layer}"
            )

            for project in sorted(projects):

                lines.append(
                    f"    └── {project}"
                )

    return "\n".join(lines)

# =============================================================================
# REPORT WRITER
# =============================================================================

def write_report():

    summary = generate_summary()

    catalog = load_catalog()

    registry = load_registry()

    azure_paths = (
        detect_azure_architecture()
    )

    pipelines = get_pipelines()

    adls_layout = (
        generate_adls_layout()
    )

    project_tree = build_tree()

    with open(
        OUTPUT,
        "w",
        encoding="utf-8",
    ) as f:

        # =============================================================
        # HEADER
        # =============================================================

        f.write(
            "# STORAGE AZURE KNOWLEDGE BASE\n\n"
        )

        f.write(
            f"Generated: "
            f"{datetime.now():%Y-%m-%d %H:%M:%S}\n\n"
        )

        # =============================================================
        # EXECUTIVE SUMMARY
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Executive Summary\n\n"
        )

        f.write(
            "Storage Azure is a data publishing platform "
            "responsible for transforming analytical datasets "
            "into governed assets stored in Azure Data Lake "
            "Storage Gen2.\n\n"
        )

        for key, value in summary.items():

            f.write(
                f"- {key}: {value}\n"
            )

        f.write("\n")

        # =============================================================
        # PROJECT MISSION
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Project Mission\n\n"
        )

        f.write(
            "The platform decouples data production from "
            "data distribution.\n\n"
        )

        f.write(
            "Projects produce data. "
            "Storage Azure publishes data.\n\n"
        )

        # =============================================================
        # ARCHITECTURE
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Architecture\n\n"
        )

        f.write("```text\n")

        f.write(
"""Inflation Analytics Brasil
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
"""
        )

        f.write("\n```\n\n")

        # =============================================================
        # DATASET LIFECYCLE
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Dataset Lifecycle\n\n"
        )

        f.write("```text\n")

        f.write(
"""Registry
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
"""
        )

        f.write("\n```\n\n")

        # =============================================================
        # PROJECT TREE
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Project Structure\n\n"
        )

        f.write("```text\n")

        f.write(project_tree)

        f.write("\n```\n\n")

        # =============================================================
        # CATALOG
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Catalog\n\n"
        )

        f.write(
            "### Projects\n\n"
        )

        for item in catalog["projects"]:

            f.write(
                f"- {item}\n"
            )

        f.write("\n")

        f.write(
            "### Domains\n\n"
        )

        for item in catalog["domains"]:

            f.write(
                f"- {item}\n"
            )

        f.write("\n")

        f.write(
            "### Containers\n\n"
        )

        for item in catalog["containers"]:

            f.write(
                f"- {item}\n"
            )

        f.write("\n")

        f.write(
            "### Layers\n\n"
        )

        for item in catalog["layers"]:

            f.write(
                f"- {item}\n"
            )

        f.write("\n")

        # =============================================================
        # DATASETS
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Registered Datasets\n\n"
        )

        for dataset_name, dataset in (

            registry.items()

        ):

            f.write(
                f"### {dataset_name}\n\n"
            )

            for key, value in (

                dataset.items()

            ):

                f.write(
                    f"- {key}: {value}\n"
                )

            f.write("\n")

        # =============================================================
        # PIPELINES
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Pipelines\n\n"
        )

        for pipeline, description in (

            pipelines.items()

        ):

            f.write(
                f"- **{pipeline}**: "
                f"{description}\n"
            )

        f.write("\n")

        # =============================================================
        # AZURE
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Azure Architecture\n\n"
        )

        for item in azure_paths:

            f.write(
                f"- {item}\n"
            )

        f.write("\n")

        # =============================================================
        # ADLS
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## ADLS Layout\n\n"
        )

        f.write("```text\n")

        f.write(adls_layout)

        f.write("\n```\n\n")

        # =============================================================
        # ROADMAP
        # =============================================================

        f.write("---\n\n")

        f.write(
            "## Roadmap\n\n"
        )

        f.write(
"""
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
"""
)

    print(
        f"\nKnowledge Base gerada:\n{OUTPUT}\n"
    )


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    write_report()
