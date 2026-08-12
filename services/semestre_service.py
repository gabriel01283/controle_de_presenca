from models.semestre import Semestre


#Create
def adicionar_semestre(
    semestres: list[Semestre],
    nome: str
) -> None:
    semestre = Semestre(nome)
    semestres.append(semestre)


#Read
def listar_semestres(
    semestres: list[Semestre]
) -> list[Semestre]:
    return semestres


#Update
def atualizar_semestre(
    semestres: list[Semestre],
    indice: int,
    novo_nome: str
) -> None:
    semestre = semestres[indice]
    semestre.semestre = novo_nome


#Delete
def remover_semestre(
    semestres: list[Semestre],
    indice: int
) -> None:
    semestres.pop(indice)