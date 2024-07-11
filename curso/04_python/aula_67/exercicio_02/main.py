from funcoes import *

limpa()

print("{:=^20}".format("Início") + "\n")

resposta = ""
while(resposta.lower() != "sim"):
    resposta = input ("Você passou no teste?")

print ("\n Parabéns!")

print("\n" + "{:=^20}".format("Fim"))