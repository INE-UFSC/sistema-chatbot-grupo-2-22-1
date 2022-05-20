##implemente as seguintes classes
from abc import ABC, abstractmethod

#cmd: comando, desc: descricao
class Bot(ABC):
    #usar comandos.itens()
    def __init__(self, nome: str, comandos: dict):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def comandos(self):
        return self.__comandos


    def mostra_comandos(self):
        for i in range(0,len(self.__comandos)):
            print()
            print('--------------------------------')
            print(f'{self.__comandos.items[i][0]}: {self._comandos.items[i][1]}')

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass