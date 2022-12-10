from identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero
        super.__init_subclass__(Identificador)

    @staticmethod
    def validarNumero(numero) -> bool:
        case = numero
        verificacao = case
        if verificacao == True:
            print('O número digitado foi {}'.format(case))
            return True
        elif verificacao == False:
            print('Digite apenas numeros!')
            return False

    def getIdentificador(self) -> Identificador:
        if self.identificador == 'Casa':
            return Identificador.CASA
        elif self.identificador == 'Trabalho':
            return Identificador.TRABALHO
        elif self.identificador == 'Celular':
            return Identificador.CELULAR

    def getNumero(self) -> str:
     return self.numero
