from fone import Fone

class Contato:

    def __init__(self, nome):
        self.nome = nome
        super.__init_subclass__()
    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        tel = 0
        for tel in self.getQuantidadeFones():
            print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
            tel =+ 1
        return tel

    def getFones(self) -> list:
        return self.getNumero

    def adicionarFone(self, fone: Fone) -> bool:
        QTDFONE = 0
        Fone = fone
        if Fone != 0:
         QTDFONE =+ 1
         print(QTDFONE)
         return QTDFONE
        else:
            return False

    def removerFone(self, index: int) -> bool:
        fone = index
        if fone != None:
            del fone
            print("Fone deletado")
            return True
        else:
            print("Fone não encontrado.")
        return False
