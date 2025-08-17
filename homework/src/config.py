from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv
_PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_env(path: Optional[Path] = None) -> None:
    if path is None:
        path = _PROJECT_ROOT / ".env"
    load_dotenv(path)

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

def data_dir() -> Path:
    load_env()
    val = get_key("Data_direction", "./data")
    return (_PROJECT_ROOT / val).resolve()
