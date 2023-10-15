from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    rootDir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path