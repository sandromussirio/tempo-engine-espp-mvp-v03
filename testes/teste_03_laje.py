import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid


clean_prefix("TESTE_03_")


create_polyline_solid(
    name="TESTE_03_LAJE",
    points=[
        (-0.1163, -0.0076),
        (0.2787, -0.0076),
        (0.2787, 0.2811),
        (-0.1163, 0.2811),
        (-0.1163, -0.0076)
    ],
    base_z=0.0,
    extrude=-0.10,
    rgb=[185, 185, 183]
)


print("TESTE_03_LAJE_OK")