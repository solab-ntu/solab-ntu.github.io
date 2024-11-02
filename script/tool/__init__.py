from pathlib import Path
from .Member import Member
from .People import People
from .Publication import Publication

FILE = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[2]

__all__ = ["Member", "People", "Publication", "FILE", "REPO"]
