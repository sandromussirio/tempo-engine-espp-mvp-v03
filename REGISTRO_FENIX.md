# REGISTRO FÊNIX — Tempo Engine / ESPP MVP

## Repositório

tempo-engine-espp-mvp

## Status

Estrutura MVP inicial.

---

## VALIDATED

### 01_SOLIDO_SIMPLES_VALIDATED_V01

POLYLINE 2D + base_z + extrude + color = sólido.

CIRCLE + center + radius + base_z + extrude + color = cilindro.

---

### 02_LAYER_INSTRUCOES_VALIDATED_V01

POLYLINE 2D + layer normalizado + INSTRUCOES = sólido 3D.

O layer manda.  
Se o layer não existir em INSTRUCOES, não inventar regra.

---

### 03_PISO_LAJE_VALIDATED_V01

POLYLINE 2D + base_z + extrude negativo + color = piso/laje.

---

### 04_MATERIAL_RGB_VALIDATED_V01

RGB explícito gera material aplicado ao objeto.

---

### 05_TRANSPARENCIA_MATERIAL_VALIDATED_V01

RGB + alpha + blend_method BLEND = transparência visível no Blender.

Não usar:

```python
mat.shadow_method = "NONE"