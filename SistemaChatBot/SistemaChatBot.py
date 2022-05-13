from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Ola, esse é o sistema de chatbots do Grupo 2\n')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('temos 2 bots disponiveis: o brabo e o goodvibes')
        aux = int(input('digite:\n 0 para o brabo \n1 para o goodvibes: ')
        while aux not in :
           aux = int(input('input fora do escopo, digite 0 para o brabo ou 1 para o goodvibes: ')
        escolhe_bot(aux)
        pass
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):

        pass
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
