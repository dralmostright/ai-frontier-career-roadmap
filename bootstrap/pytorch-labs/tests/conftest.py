"""Put this lab's ``src/`` on the import path.

Shared fixtures (``rng``, ``tol``, ``assert_close``, ``database_url``) come from
``bootstrap/conftest.py`` and are available here automatically.
"""

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
