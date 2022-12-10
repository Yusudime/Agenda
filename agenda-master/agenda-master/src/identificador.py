from enum import Enum


class Identificador(Enum):
    CELULAR = ("Celular")
    CASA = ("Casa")
    TRABALHO = ("Trabalho")

    def __init__(self, nome:str):
        self.nome = nome

