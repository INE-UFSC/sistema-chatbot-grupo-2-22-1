##implemente as seguintes classes

from abc import ABC, abstractmethod

#cmd: comando, desc: descricao
class Bot(ABC):

    def __init__(self, nome: str, comandos: dict):
        self.__nome = nome
        self.__cmd = str(comandos.keys())
        self.__desc = str(comandos.value())

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def mostra_comandos(self):
        for i in range(0,len(self.__cmd)):
            print()
            print(--------------------------------)
            print(f'{self.__cmd[i]}: {self.__desc[i]}')

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass