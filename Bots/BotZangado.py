from Bot import Bot

class BotZangado(Bot):

    def apresentacao(self):
        print('Não te interessa quem eu sou não, infeliz.')
    
    def executa_comando(self,cmd: str):
        try:
            print(self.comandos[cmd])
        except KeyError:
            print('FALA DIREITO AI ALIENIGENA')
            

    def boas_vindas(self):
        print('Eae, OTÁRIO')

    def despedida(self):
        print('Já era tarde, o desgraçado')