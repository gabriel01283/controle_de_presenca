from typing import Any
from models.aula import Aula


class Cadeira:

    def __init__(
        self,
        nome: str,
        dia_semana: str,
        limite_faltas: int
    ):
        self.nome: str = nome
        self.dia_semana: str = dia_semana
        self.limite_faltas: int = limite_faltas
        self.aulas: list[Aula] = []

    def para_dict(self) -> dict[str, Any]:
        return {
            "nome": self.nome,
            "dia_semana": self.dia_semana,
            "limite_faltas": self.limite_faltas,
            "aulas": [aula.para_dict() for aula in self.aulas]
        }

    @classmethod
    def de_dict(cls, dados: dict[str, Any]) -> "Cadeira":
        cadeira = cls(
            dados["nome"],
            dados["dia_semana"],
            dados["limite_faltas"]
        )

        cadeira.aulas = [
            Aula.de_dict(aula)
            for aula in dados["aulas"]
        ]

        return cadeira