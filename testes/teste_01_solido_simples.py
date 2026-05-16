import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid
from tempo_engine import create_circle_solid


clean_prefix("TESTE_01_")


create_polyline_solid(
    name="TESTE_01_BASE",
    points=[
        (0.0381, 0.1230),
        (0.1283, 0.1230),
        (0.1283, 0.0476),
        (0.0381, 0.0476),
        (0.0381, 0.1230)
    ],
    base_z=0.0,
    extrude=0.90,
    rgb=[127, 191, 255]
)


create_circle_solid(
    name="TESTE_01_CURVA",
    center=(0.1546, 0.1851, 0.0),
    radius=0.0632,
    base_z=0.50,
    extrude=1.00,
    rgb=[251, 132, 245]
)


print("TESTE_01_SOLIDO_SIMPLES_OK")