from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=[lista_bots]
        self.__bot = None
    
    def boas_vindas(self):
        print('Ola, esse é o sistema de chatbots do Grupo 2\n')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('temos 2 bots disponiveis: o brabo e o goodvibes')
        print('digite:\n 1 - Brabo \n2 - Goodvibes ')

        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self,aux):
        aux = input()
        while aux not in ['1', '2']:
           aux = input('input fora do escopo, digite 0 para o brabo ou 1 para o goodvibes: ')
       ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        while True:
            oper = {
                1: apresentacao,
                2: boas_vindas,
                3: executa_comando,
                4: despedida

            }   
            print('1 - apresentacao\n 2 - boas vindas\n 3 - executa comando\n 4 - despedida')
        
    def le_envia_comando(self):
    
    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
