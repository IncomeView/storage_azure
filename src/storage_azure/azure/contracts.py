from dataclasses import dataclass


@dataclass
class DatasetLocation:
    container: str
    layer: str
    dataset: str
    format: str = "parquet"