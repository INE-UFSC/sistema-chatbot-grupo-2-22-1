#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Furioso Bot"), BotFeliz("Namaste Bot")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
