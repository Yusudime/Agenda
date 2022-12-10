from contato import Contato
from identificador import Identificador

class Agenda:

    def getContatos(self) -> list:
        Contato = list
        if len(Contato) > self.getContatos():
           sorted(Contato)
        for self.getContatos in len(Contato):
            print(Contato)
        return Contato
    def getQuantidadeDeContatos(self) ->  int:
        cont = 0
        if self.getContatos() >= cont:
            cont =+1
        return cont

    def getContato(self, nome:str) -> Contato:
        Contato = nome
        return Contato

    def adicionarContato(self, contato: Contato) -> bool:
        nome = contato
        if nome != None:
             print('contato adicionado')
             return True
    def removerContato(self, nome: str) -> bool:
        nome = nome
        if nome != None:
            del nome
            print("Contato removido")
            return True
        else:
            print("Contato não encontrado.")
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        nome = nome
        fone = index
        if nome != None and fone != None:
            del fone
            print("Fone deletado")
            return True
        else:
            print("Fone não encontrado.")
        return False
    def getQuantidadeDeFones(self, identificador: Identificador) -> int:

        return 0

    def getQuantidadeDeFones(self) -> int:
        return self.getQuantidadeFones()

    def pesquisar(self, expressao:str) -> list:
        if expressao == self.nome:
            expressao = Contato[expressao]
            print(Contato[expressao])
            return Contato[expressao]
        else:
            print("Não encontrado")
        return None