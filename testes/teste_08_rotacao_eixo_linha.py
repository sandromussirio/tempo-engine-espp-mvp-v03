import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid
from tempo_engine import rotate_around_line
from tempo_engine import get_min_max_z


ROT_ANGLE = 90


clean_prefix("TESTE_08_")


# LINE "LINHA DE ROTACAO" = eixo de rotacao
# Nao modelar a linha
p1 = (0.1939, 0.2011, 0.0)
p2 = (1.0565, 0.2011, 0.0)


roof = create_polyline_solid(
    name="TESTE_08_TELHADO",
    points=[
        (0.8120, 0.2042),
        (0.8158, 0.2135),
        (0.4776, 0.3552),
        (0.3316, 0.2081),
        (0.3387, 0.2011),
        (0.4799, 0.3433),
        (0.8120, 0.2042)
    ],
    base_z=0.50,
    extrude=1.00,
    rgb=[127, 0, 0]
)


rotate_around_line(
    obj=roof,
    p1=p1,
    p2=p2,
    angle_deg=ROT_ANGLE
)


min_z, max_z = get_min_max_z(roof)


print("TESTE_08_ROTACAO_EIXO_LINHA_OK")
print("ANGLE:", ROT_ANGLE)
print("MIN_Z:", round(min_z, 4))
print("MAX_Z:", round(max_z, 4))