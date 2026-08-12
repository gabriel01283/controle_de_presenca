import customtkinter as ctk


class TelaInicio:

    def __init__(self, parent):
        self.frame = ctk.CTkFrame(
            parent,
            corner_radius=0
        )

        titulo = ctk.CTkLabel(
            self.frame,
            text="Início",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        titulo.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )

        texto = ctk.CTkLabel(
            self.frame,
            text="Bem-vindo ao Controle de Faltas!",
            font=ctk.CTkFont(
                size=18
            )
        )

        texto.pack(
            anchor="w",
            padx=40
        )

    def mostrar(self) -> None:
        self.frame.pack(
            fill="both",
            expand=True
        )

    def esconder(self) -> None:
        self.frame.pack_forget()