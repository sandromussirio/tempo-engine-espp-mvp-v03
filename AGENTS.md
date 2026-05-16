# AGENTS.md — Tempo Engine / ESPP MVP

Este repositório é um MVP local do Tempo Engine / ESPP para testes no Blender.

## Estrutura atual

- tempo_engine.py é o núcleo comum.
- testes/ contém scripts de validação para rodar no Blender.
- REGISTRO_FENIX.md contém o histórico técnico e o status das regras.
- README.md explica o uso humano do projeto.

## Regra principal

Não reestruture o projeto sem pedido explícito.

Não transforme tempo_engine.py em pacote tempo_engine/ ainda.

## Módulos validados

- teste_01_solido_simples.py
- teste_02_layer_instrucoes.py
- teste_03_laje.py
- teste_05_transparencia.py
- teste_07_boolean_cut.py

## Módulos experimentais

- teste_08_rotacao_eixo_linha.py
- teste_09_rotacao_eixo_dedicado.py

Rotação ainda não é regra validada.

## Ao editar testes

Se um teste dentro de testes/ precisar importar tempo_engine.py, usar:

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import tempo_engine

## Proibições

Não adicionar:
- cloud
- interface HTML
- parser de AutoCAD LIST
- add-on Blender
- pacote Python complexo
- rotação como regra validada
- módulos novos sem pedido explícito

Não alterar schema validado sem pedido explícito.

Não misturar pisos, lajes, boolean, transparência, rotação e peças de eucalipto em um único módulo.

## Como trabalhar

Cada tarefa deve ser pequena.

Preferir:
- corrigir import
- organizar função
- preservar comportamento validado
- explicar diff

Evitar:
- reescrever tudo
- inventar arquitetura nova
- criar MVP completo