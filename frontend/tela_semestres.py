import customtkinter as ctk

from models.semestre import Semestre
from services.semestre_service import (
    adicionar_semestre,
    atualizar_semestre,
    remover_semestre
)


class TelaSemestres(ctk.CTkFrame):

    def __init__(
        self,
        master,
        semestres: list[Semestre],
        salvar_callback,
        abrir_semestre_callback,
        voltar_callback
    ):
        super().__init__(master)

        self.semestres = semestres
        self.salvar_callback = salvar_callback
        self.abrir_semestre_callback = abrir_semestre_callback
        self.voltar_callback = voltar_callback

        self.titulo = ctk.CTkLabel(
            self,
            text="Semestres",
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
            text="Adicionar semestre",
            command=self.adicionar
        )
        self.botao_adicionar.pack(pady=10)

        self.botao_voltar = ctk.CTkButton(
            self,
            text="Sair",
            command=self.voltar
        )
        self.botao_voltar.pack(pady=(0, 20))

        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        for indice, semestre in enumerate(self.semestres):
            frame = ctk.CTkFrame(self.lista)
            frame.pack(
                fill="x",
                pady=5
            )

            nome = ctk.CTkLabel(
                frame,
                text=semestre.semestre,
                font=ctk.CTkFont(size=16)
            )
            nome.pack(
                side="left",
                padx=15,
                pady=10
            )

            botao_entrar = ctk.CTkButton(
                frame,
                text="Entrar",
                width=80,
                command=lambda i=indice: self.abrir_semestre(
                    self.semestres[i]
                )
            )
            botao_entrar.pack(
                side="right",
                padx=5,
                pady=10
            )

            botao_remover = ctk.CTkButton(
                frame,
                text="Remover",
                width=90,
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
                width=90,
                command=lambda i=indice: self.editar(i)
            )
            botao_editar.pack(
                side="right",
                padx=5,
                pady=10
            )

    def abrir_semestre(self, semestre: Semestre):
        self.abrir_semestre_callback(semestre)

    def adicionar(self):
        janela = ctk.CTkInputDialog(
            text="Digite o semestre:",
            title="Adicionar semestre"
        )

        nome = janela.get_input()

        if nome:
            adicionar_semestre(
                self.semestres,
                nome
            )

            self.salvar_callback()
            self.atualizar_lista()

    def editar(self, indice: int):
        janela = ctk.CTkInputDialog(
            text="Digite o novo semestre:",
            title="Editar semestre"
        )

        novo_nome = janela.get_input()

        if novo_nome:
            atualizar_semestre(
                self.semestres,
                indice,
                novo_nome
            )

            self.salvar_callback()
            self.atualizar_lista()

    def remover(self, indice: int):
        remover_semestre(
            self.semestres,
            indice
        )

        self.salvar_callback()
        self.atualizar_lista()

    def voltar(self):
        self.voltar_callback()