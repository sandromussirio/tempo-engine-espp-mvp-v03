import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid
from tempo_engine import apply_boolean_difference


clean_prefix("TESTE_07_")


base = create_polyline_solid(
    name="TESTE_07_ALVENARIA_BASE",
    points=[
        (0.4039, 0.4622),
        (-0.3452, 0.2527),
        (-0.3694, 0.3394),
        (0.3797, 0.5489),
        (0.4039, 0.4622)
    ],
    base_z=0.0,
    extrude=2.00,
    rgb=[0, 46, 61]
)


cut = create_polyline_solid(
    name="TESTE_07_CUT_SUBTRATOR",
    points=[
        (-0.1518, 0.5123),
        (0.0650, 0.5729),
        (0.1307, 0.3383),
        (-0.0862, 0.2777),
        (-0.1518, 0.5123)
    ],
    base_z=0.20,
    extrude=0.90,
    rgb=[255, 0, 0]
)


apply_boolean_difference(base, cut)


print("TESTE_07_BOOLEAN_CUT_OK")