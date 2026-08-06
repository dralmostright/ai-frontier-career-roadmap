"""Put this lab's ``src/`` and ``evals/`` on the import path.

``evals/`` is included because the Week 44 benchmark generator lives there
rather than in ``src/`` — it is test infrastructure, not product code.
"""

import sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
for subdir in ("src", "evals"):
    path = LAB / subdir
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
