import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tempo_engine import clean_prefix
from tempo_engine import create_polyline_solid
from tempo_engine import resolve_instruction


INSTRUCOES = {
    "1LAJENIVEL01": {
        "base_z": 2.40,
        "extrude": 0.10,
        "color": [152, 152, 152]
    },
    "1ALVPEDRA": {
        "base_z": 0.00,
        "extrude": 2.40,
        "color": [173, 90, 68]
    }
}


clean_prefix("TESTE_02_")


objects = [
    {
        "name": "TESTE_02_LAJE_POR_LAYER",
        "layer": "1-LAJE-NIVEL01",
        "points": [
            (0.00, 0.00),
            (1.00, 0.00),
            (1.00, 0.70),
            (0.00, 0.70),
            (0.00, 0.00)
        ]
    },
    {
        "name": "TESTE_02_ALVENARIA_POR_LAYER",
        "layer": "1-ALV-PEDRA",
        "points": [
            (1.20, 0.00),
            (1.60, 0.00),
            (1.60, 0.70),
            (1.20, 0.70),
            (1.20, 0.00)
        ]
    }
]


for item in objects:
    regra, key = resolve_instruction(item["layer"], INSTRUCOES)

    if regra is None:
        print("SEM_INSTRUCAO:", item["name"], item["layer"], key)
        continue

    create_polyline_solid(
        name=item["name"],
        points=item["points"],
        base_z=regra["base_z"],
        extrude=regra["extrude"],
        rgb=regra["color"]
    )


print("TESTE_02_LAYER_INSTRUCOES_OK")