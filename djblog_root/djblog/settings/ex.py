import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

k = BASE_DIR / 'djblogapp' / 'templates'

print(k)
