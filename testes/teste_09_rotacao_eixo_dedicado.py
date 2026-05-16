import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_circle_solid
from tempo_engine import create_ellipse_solid
from tempo_engine import rotate_around_line


clean_prefix("TESTE_09_")


# EIXO ROTACAO 1 = gira DISCO
eixo1_p1 = (0.7744, 0.1781, 0.0)
eixo1_p2 = (0.7744, -0.0159, 0.0)

# EIXO ROTACAO 2 = gira PILAR REDONDO
eixo2_p1 = (0.3633, 0.0885, 0.0)
eixo2_p2 = (0.5657, 0.0885, 0.0)


disco = create_ellipse_solid(
    name="TESTE_09_DISCO",
    center=(0.6805, 0.1059),
    semi_x=0.0751,
    semi_y=0.0272,
    base_z=0.40,
    extrude=2.50,
    rgb=[0, 0, 0]
)


pilar = create_circle_solid(
    name="TESTE_09_PILAR_REDONDO",
    center=(0.4661, 0.0885, 0.0),
    radius=0.0534,
    base_z=0.90,
    extrude=2.50,
    rgb=[255, 255, 255]
)


rotate_around_line(
    obj=disco,
    p1=eixo1_p1,
    p2=eixo1_p2,
    angle_deg=90
)


rotate_around_line(
    obj=pilar,
    p1=eixo2_p1,
    p2=eixo2_p2,
    angle_deg=30
)


print("TESTE_09_ROTACAO_EIXO_DEDICADO_OK")