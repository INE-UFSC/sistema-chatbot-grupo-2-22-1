from abc import ABC,abstractmethod
class Bot(ABC):
    @abstractmethod
    def __init__(self, nome: str, comandos: dict):
        pass
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #Analisar se o ultimo metodo esta correto
    @abstractmethod
    def mostra_comandos(self):
        return str
