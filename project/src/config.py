from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv
_PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_env(dotenv_path: Optional[Path] = None) -> None:
    """
    Load environment variables from a .env file at the project root by default.
    """
    if dotenv_path is None:
        dotenv_path = _PROJECT_ROOT / ".env"
    load_dotenv(dotenv_path)

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get an environment variable by name.
    """
    return os.getenv(name, default)

def data_dir() -> Path:
    """
    Return the absolute path to the project's data directory
    (based on DATA_DIR in .env, defaults to ./data).
    """
    load_env()
    val = get_key("DATA_DIR", "./data")
    return (_PROJECT_ROOT / val).resolve()
