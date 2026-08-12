import json
import os
import sys
from typing import Any


def obter_caminho_dados() -> str:
    if getattr(sys, "frozen", False):
        pasta = os.path.dirname(sys.executable)
    else:
        pasta = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    pasta_dados = os.path.join(pasta, "data")

    os.makedirs(pasta_dados, exist_ok=True)

    return os.path.join(pasta_dados, "dados.json")


CAMINHO_ARQUIVO = obter_caminho_dados()


def carregar_dados() -> dict[str, Any]:
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {"semestres": []}

    with open(
        CAMINHO_ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:
        return json.load(arquivo)


def salvar_dados(dados: dict[str, Any]) -> None:
    with open(
        CAMINHO_ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )