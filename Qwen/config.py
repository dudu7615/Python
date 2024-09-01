from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config:
    path: Path
    seed: int = 1234
    cpu_only: bool = False
