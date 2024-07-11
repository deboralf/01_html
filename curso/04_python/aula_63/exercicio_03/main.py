#import funcoes

from funcoes import *

limpa()

print("{:=^20}".format("Início") + "\n")

exibirMensagens()
exibirMensagens()
exibirMensagens()

calcDobro()
calcDobro()

calcTriplo(6)
teste = 2
calcTriplo (teste)
calcTriplo (float (input("Digite um número: ")))

descontar10 (66.5)

desconto = descontar10ComRetorno(65) - 5
print (desconto)

print("\n" + "{:=^20}".format("Fim"))
