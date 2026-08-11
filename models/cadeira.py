class Cadeira:

    def __init__(self, nome: str, dia_semana: str, limite_faltas: int):
        self.nome = nome
        self.dia_semana = dia_semana
        self.limite_faltas = limite_faltas
        self.aulas = []