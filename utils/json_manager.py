import json
from typing import Any


CAMINHO_ARQUIVO = "data/dados.json"


def carregar_dados() -> dict[str, Any]:
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