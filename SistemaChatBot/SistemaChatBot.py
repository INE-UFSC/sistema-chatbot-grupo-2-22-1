from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, Empresa: str, lista_bots: list):
        self.__empresa = Empresa
        self.__lista_bots = lista_bots
        self.__bot = None

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def lista_bots(self):
        return self.__lista_bots

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    def boas_vindas_sistema(self):
        print(f'Ola, esse é o sistema de chatbots do Grupo {self.__empresa}\n')
        # mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('temos esses bots disponiveis:')
        for ele in enumerate(self.__lista_bots):
            print(f'BOT: {ele}')

    def escolhe_bot(self):
        aux = input('digite o codigo do bot desejado: ')
        while aux not in enumerate(self.__lista_bots):
            aux = input('input fora do escopo')
        # faz a entrada de dadosf do usuário e atribui o objeto ao atributo __bot

    def inicio(self):
        self.boas_vindas_sistema()
        self.mostra_menu()
        self.escolhe_bot()
        # mostra mensagens de boas-vindas do bot escolhido
        # entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        # ao sair mostrar a mensagem de despedida do bot
