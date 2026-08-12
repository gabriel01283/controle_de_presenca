from models.aula import Aula
from models.cadeira import Cadeira
from models.semestre import Semestre

from services.semestre_service import (
    adicionar_semestre,
    listar_semestres,
    atualizar_semestre,
    remover_semestre
)

from services.cadeira_service import (
    adicionar_cadeira,
    listar_cadeiras,
    atualizar_cadeira,
    remover_cadeira
)

from services.aula_service import (
    adicionar_aula,
    listar_aulas,
    atualizar_aula,
    remover_aula
)

from utils.json_manager import carregar_dados, salvar_dados


def salvar_todos_dados(semestres: list[Semestre]):
    dados = {
        "semestres": [
            semestre.para_dict()
            for semestre in semestres
        ]
    }

    salvar_dados(dados)


def mostrar_aula(aula: Aula, indice: int):
    if aula.presente:
        presenca = "Presente"
    else:
        presenca = "Falta"

    print(f"{indice + 1}. {aula.data} - {presenca}")


def mostrar_cadeira(cadeira: Cadeira, indice: int):
    faltas = sum(
        1
        for aula in cadeira.aulas
        if not aula.presente
    )

    faltas_restantes = cadeira.limite_faltas - faltas

    print(f"\n{indice + 1}. {cadeira.nome}")
    print(f"   Dia da semana: {cadeira.dia_semana}")
    print(f"   Limite de faltas: {cadeira.limite_faltas}")
    print(f"   Faltas: {faltas}")
    print(f"   Faltas restantes: {faltas_restantes}")


def menu_aulas(
    cadeira: Cadeira,
    semestres: list[Semestre]
):
    while True:
        print(f"\n{cadeira.nome}")

        print(f"\nDia da semana: {cadeira.dia_semana}")
        print(f"Limite de faltas: {cadeira.limite_faltas}")

        faltas = sum(
            1
            for aula in cadeira.aulas
            if not aula.presente
        )

        faltas_restantes = cadeira.limite_faltas - faltas

        print(f"Faltas: {faltas}")
        print(f"Faltas restantes: {faltas_restantes}")

        print("\nAulas:")

        aulas = listar_aulas(cadeira)

        if not aulas:
            print("Nenhuma aula cadastrada.")
        else:
            for indice, aula in enumerate(aulas):
                mostrar_aula(aula, indice)

        print("\n1. Adicionar aula")
        print("2. Editar aula")
        print("3. Remover aula")
        print("4. Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            data = input("\nDigite a data da aula: ")

            resposta = input(
                "Você esteve presente? (s/n): "
            ).lower()

            presente = resposta == "s"

            adicionar_aula(
                cadeira,
                data,
                presente
            )

            salvar_todos_dados(semestres)

            print("\nAula adicionada com sucesso!")

        elif opcao == "2":
            aulas = listar_aulas(cadeira)

            if not aulas:
                print("\nNenhuma aula cadastrada.")
                continue

            try:
                indice = int(
                    input("\nDigite o número da aula: ")
                ) - 1

                nova_data = input(
                    "Digite a nova data: "
                )

                resposta = input(
                    "Você esteve presente? (s/n): "
                ).lower()

                nova_presenca = resposta == "s"

                atualizar_aula(
                    cadeira,
                    indice,
                    nova_data,
                    nova_presenca
                )

                salvar_todos_dados(semestres)

                print("\nAula atualizada com sucesso!")

            except (ValueError, IndexError):
                print("\nAula inválida.")

        elif opcao == "3":
            aulas = listar_aulas(cadeira)

            if not aulas:
                print("\nNenhuma aula cadastrada.")
                continue

            try:
                indice = int(
                    input("\nDigite o número da aula: ")
                ) - 1

                remover_aula(cadeira, indice)

                salvar_todos_dados(semestres)

                print("\nAula removida com sucesso!")

            except (ValueError, IndexError):
                print("\nAula inválida.")

        elif opcao == "4":
            break

        else:
            print("\nOpção inválida.")


def menu_cadeiras(
    semestre: Semestre,
    semestres: list[Semestre]
):
    while True:
        print(f"\nSEMESTRE: {semestre.semestre}")

        cadeiras = listar_cadeiras(semestre)

        print("\nCadeiras:")

        if not cadeiras:
            print("Nenhuma cadeira cadastrada.")
        else:
            for indice, cadeira in enumerate(cadeiras):
                mostrar_cadeira(cadeira, indice)

        print("\n1. Adicionar cadeira")
        print("2. Editar cadeira")
        print("3. Remover cadeira")
        print("4. Entrar em uma cadeira")
        print("5. Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nNome da cadeira: ")
            dia_semana = input("Dia da semana: ")

            try:
                limite_faltas = int(
                    input("Limite de faltas: ")
                )
                
                adicionar_cadeira(
                    semestre,
                    nome,
                    dia_semana,
                    limite_faltas
                )

                salvar_todos_dados(semestres)

                print("\nCadeira adicionada com sucesso!")

            except ValueError:
                print("\nO limite de faltas precisa ser um número.")

        elif opcao == "2":
            cadeiras = listar_cadeiras(semestre)

            if not cadeiras:
                print("\nNenhuma cadeira cadastrada.")
                continue

            try:
                indice = int(
                    input("\nDigite o número da cadeira: ")
                ) - 1

                novo_nome = input("Novo nome: ")
                novo_dia = input("Novo dia da semana: ")

                novo_limite = int(
                    input("Novo limite de faltas: ")
                )

                atualizar_cadeira(
                    semestre,
                    indice,
                    novo_nome,
                    novo_dia,
                    novo_limite
                )

                salvar_todos_dados(semestres)

                print("\nCadeira atualizada com sucesso!")

            except (ValueError, IndexError):
                print("\nCadeira inválida.")

        elif opcao == "3":
            cadeiras = listar_cadeiras(semestre)

            if not cadeiras:
                print("\nNenhuma cadeira cadastrada.")
                continue

            try:
                indice = int(
                    input("\nDigite o número da cadeira: ")
                ) - 1

                cadeira_removida = cadeiras[indice]

                remover_cadeira(
                    semestre,
                    indice
                )

                salvar_todos_dados(semestres)

                print(
                    f"\nCadeira '{cadeira_removida.nome}' "
                    "removida com sucesso!"
                )

            except (ValueError, IndexError):
                print("\nCadeira inválida.")

        elif opcao == "4":
            cadeiras = listar_cadeiras(semestre)

            if not cadeiras:
                print("\nNenhuma cadeira cadastrada.")
                continue

            try:
                indice = int(
                    input("\nDigite o número da cadeira: ")
                ) - 1

                cadeira = cadeiras[indice]

                menu_aulas(
                    cadeira,
                    semestres
                )

            except (ValueError, IndexError):
                print("\nCadeira inválida.")

        elif opcao == "5":
            break

        else:
            print("\nOpção inválida.")


def menu_semestres(semestres: list[Semestre]):
    while True:
        print("\nSEMESTRES")

        lista_semestres = listar_semestres(semestres)

        if not lista_semestres:
            print("\nNenhum semestre cadastrado.")
        else:
            for indice, semestre in enumerate(lista_semestres):
                print(
                    f"\n{indice + 1}. {semestre.semestre}"
                    f" - {len(semestre.cadeiras)} cadeira(s)"
                )

        print("\n1. Adicionar semestre")
        print("2. Editar semestre")
        print("3. Remover semestre")
        print("4. Entrar em um semestre")
        print("5. Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input(
                "\nDigite o semestre (ex: 2026.2): "
            )

            adicionar_semestre(
                semestres,
                nome
            )

            salvar_todos_dados(semestres)

            print("\nSemestre adicionado com sucesso!")

        elif opcao == "2":
            if not lista_semestres:
                print("\nNenhum semestre cadastrado.")
                continue

            try:
                indice = int(
                    input("\nDigite o número do semestre: ")
                ) - 1

                novo_nome = input(
                    "Digite o novo semestre: "
                )

                atualizar_semestre(
                    semestres,
                    indice,
                    novo_nome
                )

                salvar_todos_dados(semestres)

                print("\nSemestre atualizado com sucesso!")

            except (ValueError, IndexError):
                print("\nSemestre inválido.")

        elif opcao == "3":
            if not lista_semestres:
                print("\nNenhum semestre cadastrado.")
                continue

            try:
                indice = int(
                    input("\nDigite o número do semestre: ")
                ) - 1

                semestre_removido = lista_semestres[indice]

                remover_semestre(
                    semestres,
                    indice
                )

                salvar_todos_dados(semestres)

                print(
                    f"\nSemestre '{semestre_removido.semestre}' "
                    "removido com sucesso!"
                )

            except (ValueError, IndexError):
                print("\nSemestre inválido.")

        elif opcao == "4":
            if not lista_semestres:
                print("\nNenhum semestre cadastrado.")
                continue

            try:
                indice = int(
                    input("\nDigite o número do semestre: ")
                ) - 1

                semestre = lista_semestres[indice]

                menu_cadeiras(
                    semestre,
                    semestres
                )

            except (ValueError, IndexError):
                print("\nSemestre inválido.")

        elif opcao == "5":
            break

        else:
            print("\nOpção inválida.")


def main():
    dados = carregar_dados()

    semestres: list[Semestre] = [
        Semestre.de_dict(semestre)
        for semestre in dados["semestres"]
    ]

    while True:
        print("\nCONTROLE DE FALTAS")

        print("\n1. Semestres")
        print("2. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_semestres(semestres)

        elif opcao == "2":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()