import customtkinter as ctk

from models.cadeira import Cadeira
from services.aula_service import (
    adicionar_aula,
    atualizar_aula,
    remover_aula
)


class TelaAulas(ctk.CTkFrame):

    def __init__(
        self,
        master,
        cadeira: Cadeira,
        salvar_callback,
        voltar_callback
    ):
        super().__init__(master)

        self.cadeira = cadeira
        self.salvar_callback = salvar_callback
        self.voltar_callback = voltar_callback

        self.titulo = ctk.CTkLabel(
            self,
            text=self.cadeira.nome,
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.titulo.pack(pady=(20, 5))

        self.informacoes = ctk.CTkLabel(
            self,
            text=""
        )
        self.informacoes.pack(pady=5)

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self,
            text="Adicionar aula",
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

        faltas = sum(
            1
            for aula in self.cadeira.aulas
            if not aula.presente
        )

        restantes = self.cadeira.limite_faltas - faltas

        self.informacoes.configure(
            text=(
                f"Dia: {self.cadeira.dia_semana}    "
                f"Faltas: {faltas}    "
                f"Faltas restantes: {restantes}"
            )
        )

        for indice, aula in enumerate(self.cadeira.aulas):
            frame = ctk.CTkFrame(self.lista)
            frame.pack(
                fill="x",
                pady=5
            )

            presenca = (
                "Presente"
                if aula.presente
                else "Falta"
            )

            label = ctk.CTkLabel(
                frame,
                text=f"{aula.data}  |  {presenca}"
            )
            label.pack(
                side="left",
                padx=15,
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
                padx=10,
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

    def adicionar(self):
        data = ctk.CTkInputDialog(
            text="Data da aula:",
            title="Adicionar aula"
        ).get_input()

        if not data:
            return

        resposta = ctk.CTkInputDialog(
            text="Você esteve presente? Digite s ou n:",
            title="Adicionar aula"
        ).get_input()

        if not resposta:
            return

        presente = resposta.lower() == "s"

        adicionar_aula(
            self.cadeira,
            data,
            presente
        )

        self.salvar_callback()
        self.atualizar_lista()

    def editar(self, indice: int):
        nova_data = ctk.CTkInputDialog(
            text="Nova data:",
            title="Editar aula"
        ).get_input()

        if not nova_data:
            return

        resposta = ctk.CTkInputDialog(
            text="Você esteve presente? Digite s ou n:",
            title="Editar aula"
        ).get_input()

        if not resposta:
            return

        nova_presenca = resposta.lower() == "s"

        atualizar_aula(
            self.cadeira,
            indice,
            nova_data,
            nova_presenca
        )

        self.salvar_callback()
        self.atualizar_lista()

    def remover(self, indice: int):
        remover_aula(
            self.cadeira,
            indice
        )

        self.salvar_callback()
        self.atualizar_lista()

    def voltar(self):
        self.voltar_callback()