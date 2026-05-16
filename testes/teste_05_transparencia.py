import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid
from tempo_engine import material_transparente


clean_prefix("TESTE_05_")


mat = material_transparente(
    rgb=[0, 255, 0],
    alpha=0.28
)


obj1 = create_polyline_solid(
    name="TESTE_05_VIDRO_1",
    points=[
        (-0.0926, 0.0272),
        (-0.0869, 0.0247),
        (0.0099, 0.2448),
        (0.0042, 0.2473),
        (-0.0926, 0.0272)
    ],
    base_z=0.0,
    extrude=1.20,
    material=mat
)


obj2 = create_polyline_solid(
    name="TESTE_05_VIDRO_2",
    points=[
        (-0.0896, 0.0139),
        (0.2592, 0.0406),
        (0.2587, 0.0468),
        (-0.0900, 0.0202),
        (-0.0896, 0.0139)
    ],
    base_z=0.0,
    extrude=1.20,
    material=mat
)


obj1.show_transparent = True
obj2.show_transparent = True
obj1.display_type = "TEXTURED"
obj2.display_type = "TEXTURED"


print("TESTE_05_TRANSPARENCIA_OK")