from typing import Any


class Aula:

    def __init__(self, data: str, presente: bool):
        self.data: str = data
        self.presente: bool = presente

    def para_dict(self) -> dict[str, Any]:
        return {
            "data": self.data,
            "presente": self.presente
        }

    @classmethod
    def de_dict(cls, dados: dict[str, Any]) -> "Aula":
        return cls(dados["data"], dados["presente"])