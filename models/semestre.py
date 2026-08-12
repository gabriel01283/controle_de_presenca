from typing import Any
from models.cadeira import Cadeira


class Semestre:

    def __init__(self, semestre: str):
        self.semestre: str = semestre
        self.cadeiras: list[Cadeira] = []

    def para_dict(self) -> dict[str, Any]:
        return {
            "semestre": self.semestre,
            "cadeiras": [cadeira.para_dict() for cadeira in self.cadeiras]
        }

    @classmethod
    def de_dict(cls, dados: dict[str, Any]) -> "Semestre":
        semestre = cls(dados["semestre"])

        semestre.cadeiras = [
            Cadeira.de_dict(cadeira)
            for cadeira in dados["cadeiras"]
        ]

        return semestre