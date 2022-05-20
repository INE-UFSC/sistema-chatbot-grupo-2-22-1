from Bot import Bot

class BotFeliz(Bot):
    
    def apresentacao(self):
        print("Olá, eu sou o bot goodvibes, conhecido como Namaste.")
 
    def executa_comando(self,cmd: str):
        try:
            print(self.comandos[cmd])
        except KeyError:
            print('Não entendi qq cê falo não')
            
        

    def boas_vindas(self):
        print("Bem vindo, meu rei")

    def despedida(self):
        print("Que as boas vibrações do universo estejam com você, Jah Bles!")