import customtkinter as ctk


class TelaSemestres:

    def __init__(self, parent):
        self.frame = ctk.CTkFrame(
            parent,
            corner_radius=0
        )

        self.titulo = ctk.CTkLabel(
            self.frame,
            text="Semestres",
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

        self.texto = ctk.CTkLabel(
            self.frame,
            text="Nenhum semestre carregado."
        )

        self.texto.pack(
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