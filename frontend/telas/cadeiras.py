import customtkinter as ctk

from models.semestre import Semestre


class TelaCadeiras:

    def __init__(self, parent, semestre: Semestre):
        self.frame = ctk.CTkFrame(
            parent,
            corner_radius=0
        )

        self.semestre = semestre

        self.titulo = ctk.CTkLabel(
            self.frame,
            text=semestre.semestre,
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        self.titulo.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )

        self.lista = ctk.CTkScrollableFrame(
            self.frame
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 40)
        )

        self.atualizar()

    def atualizar(self) -> None:
        for widget in self.lista.winfo_children():
            widget.destroy()

        if not self.semestre.cadeiras:
            texto = ctk.CTkLabel(
                self.lista,
                text="Nenhuma cadeira cadastrada."
            )

            texto.pack(
                pady=20
            )

            return

        for cadeira in self.semestre.cadeiras:
            botao = ctk.CTkButton(
                self.lista,
                text=cadeira.nome
            )

            botao.pack(
                fill="x",
                pady=5
            )

    def mostrar(self) -> None:
        self.frame.pack(
            fill="both",
            expand=True
        )

    def esconder(self) -> None:
        self.frame.pack_forget()