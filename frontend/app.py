import customtkinter as ctk

from models.semestre import Semestre
from models.cadeira import Cadeira

from utils.json_manager import (
    carregar_dados,
    salvar_dados
)

from frontend.tela_semestres import TelaSemestres
from frontend.tela_cadeiras import TelaCadeiras
from frontend.tela_aulas import TelaAulas


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Controle de Faltas")
        self.geometry("900x600")

        dados = carregar_dados()

        self.semestres: list[Semestre] = [
            Semestre.de_dict(semestre)
            for semestre in dados["semestres"]
        ]

        self.semestre_atual: Semestre | None = None
        self.cadeira_atual: Cadeira | None = None

        self.mostrar_semestres()

    def salvar(self):
        dados = {
            "semestres": [
                semestre.para_dict()
                for semestre in self.semestres
            ]
        }

        salvar_dados(dados)

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_semestres(self):
        self.semestre_atual = None
        self.cadeira_atual = None

        self.limpar_tela()

        tela = TelaSemestres(
            self,
            self.semestres,
            self.salvar,
            self.mostrar_cadeiras,
            self.fechar_app
        )

        tela.pack(
            fill="both",
            expand=True
        )

    def mostrar_cadeiras(self, semestre: Semestre):
        self.semestre_atual = semestre
        self.cadeira_atual = None

        self.limpar_tela()

        tela = TelaCadeiras(
            self,
            semestre,
            self.salvar,
            self.mostrar_aulas,
            self.mostrar_semestres
        )

        tela.pack(
            fill="both",
            expand=True
        )

    def mostrar_aulas(self, cadeira: Cadeira):
        self.cadeira_atual = cadeira

        self.limpar_tela()

        tela = TelaAulas(
            self,
            cadeira,
            self.salvar,
            self.voltar_para_cadeiras
        )

        tela.pack(
            fill="both",
            expand=True
        )

    def voltar_para_cadeiras(self):
        if self.semestre_atual is not None:
            self.mostrar_cadeiras(
                self.semestre_atual
            )

    def fechar_app(self):
        self.destroy()


def iniciar_app():
    app = App()
    app.mainloop()