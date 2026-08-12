from models.aula import Aula
from models.cadeira import Cadeira


#Create
def adicionar_aula(
    cadeira: Cadeira,
    data: str,
    presente: bool
) -> None:
    aula = Aula(data, presente)
    cadeira.aulas.append(aula)


#Read
def listar_aulas(cadeira: Cadeira) -> list[Aula]:
    return cadeira.aulas


#Update
def atualizar_aula(
    cadeira: Cadeira,
    indice: int,
    nova_data: str,
    nova_presenca: bool
) -> None:
    aula = cadeira.aulas[indice]
    aula.data = nova_data
    aula.presente = nova_presenca


#Delete
def remover_aula(cadeira: Cadeira, indice: int) -> None:
    cadeira.aulas.pop(indice)