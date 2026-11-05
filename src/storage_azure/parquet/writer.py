# src/publishing/parquet/writer.py

from pathlib import Path
import pandas as pd


def save_parquet(
    dataframe: pd.DataFrame,
    output_path: str | Path,
):

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_parquet(output_path, index=False)

    return output_path