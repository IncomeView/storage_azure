# src/publishing/settings.py

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = ROOT / "exports"

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)