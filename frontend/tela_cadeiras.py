import customtkinter as ctk

from models.semestre import Semestre
from services.cadeira_service import (
    adicionar_cadeira,
    atualizar_cadeira,
    remover_cadeira
)


class TelaCadeiras(ctk.CTkFrame):

    def __init__(
        self,
        master,
        semestre: Semestre,
        salvar_callback,
        abrir_aulas_callback,
        voltar_callback
    ):
        super().__init__(master)

        self.semestre = semestre
        self.salvar_callback = salvar_callback
        self.abrir_aulas_callback = abrir_aulas_callback
        self.voltar_callback = voltar_callback

        self.titulo = ctk.CTkLabel(
            self,
            text=f"Cadeiras - {semestre.semestre}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.titulo.pack(pady=20)

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self,
            text="Adicionar cadeira",
            command=self.adicionar
        )
        self.botao_adicionar.pack(pady=10)

        self.botao_voltar = ctk.CTkButton(
            self,
            text="Voltar",
            command=self.voltar
        )
        self.botao_voltar.pack(pady=(0, 20))

        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        for indice, cadeira in enumerate(self.semestre.cadeiras):
            frame = ctk.CTkFrame(self.lista)
            frame.pack(
                fill="x",
                pady=5
            )

            texto = (
                f"{cadeira.nome}\n"
                f"{cadeira.dia_semana} | "
                f"Limite de faltas: {cadeira.limite_faltas}"
            )

            nome = ctk.CTkLabel(
                frame,
                text=texto,
                justify="left",
                font=ctk.CTkFont(size=15)
            )
            nome.pack(
                side="left",
                padx=15,
                pady=10
            )

            botao_aulas = ctk.CTkButton(
                frame,
                text="Aulas",
                width=80,
                command=lambda i=indice: self.abrir_aulas(
                    self.semestre.cadeiras[i]
                )
            )
            botao_aulas.pack(
                side="right",
                padx=5,
                pady=10
            )

            botao_remover = ctk.CTkButton(
                frame,
                text="Remover",
                width=80,
                command=lambda i=indice: self.remover(i)
            )
            botao_remover.pack(
                side="right",
                padx=5,
                pady=10
            )

            botao_editar = ctk.CTkButton(
                frame,
                text="Editar",
                width=80,
                command=lambda i=indice: self.editar(i)
            )
            botao_editar.pack(
                side="right",
                padx=5,
                pady=10
            )

    def abrir_aulas(self, cadeira):
        self.abrir_aulas_callback(
            cadeira
        )

    def adicionar(self):
        nome = ctk.CTkInputDialog(
            text="Nome da cadeira:",
            title="Adicionar cadeira"
        ).get_input()

        if not nome:
            return

        dia_semana = ctk.CTkInputDialog(
            text="Dia da semana:",
            title="Adicionar cadeira"
        ).get_input()

        if not dia_semana:
            return

        limite = ctk.CTkInputDialog(
            text="Limite de faltas:",
            title="Adicionar cadeira"
        ).get_input()

        if not limite:
            return

        try:
            limite_faltas = int(limite)
        except ValueError:
            return

        adicionar_cadeira(
            self.semestre,
            nome,
            dia_semana,
            limite_faltas
        )

        self.salvar_callback()
        self.atualizar_lista()

    def editar(self, indice: int):
        novo_nome = ctk.CTkInputDialog(
            text="Novo nome:",
            title="Editar cadeira"
        ).get_input()

        if not novo_nome:
            return

        novo_dia = ctk.CTkInputDialog(
            text="Novo dia da semana:",
            title="Editar cadeira"
        ).get_input()

        if not novo_dia:
            return

        novo_limite = ctk.CTkInputDialog(
            text="Novo limite de faltas:",
            title="Editar cadeira"
        ).get_input()

        if not novo_limite:
            return

        try:
            novo_limite_faltas = int(novo_limite)
        except ValueError:
            return

        atualizar_cadeira(
            self.semestre,
            indice,
            novo_nome,
            novo_dia,
            novo_limite_faltas
        )

        self.salvar_callback()
        self.atualizar_lista()

    def remover(self, indice: int):
        remover_cadeira(
            self.semestre,
            indice
        )

        self.salvar_callback()
        self.atualizar_lista()

    def voltar(self):
        self.voltar_callback()