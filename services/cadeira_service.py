from models.cadeira import Cadeira
from models.semestre import Semestre


#Create
def adicionar_cadeira(
    semestre: Semestre,
    nome: str,
    dia_semana: str,
    limite_faltas: int
) -> None:
    cadeira = Cadeira(nome, dia_semana, limite_faltas)
    semestre.cadeiras.append(cadeira)


#Read
def listar_cadeiras(
    semestre: Semestre
) -> list[Cadeira]:
    return semestre.cadeiras


#Update
def atualizar_cadeira(
    semestre: Semestre,
    indice: int,
    novo_nome: str,
    novo_dia_semana: str,
    novo_limite_faltas: int
) -> None:
    cadeira = semestre.cadeiras[indice]

    cadeira.nome = novo_nome
    cadeira.dia_semana = novo_dia_semana
    cadeira.limite_faltas = novo_limite_faltas


#Delete
def remover_cadeira(
    semestre: Semestre,
    indice: int
) -> None:
    semestre.cadeiras.pop(indice)