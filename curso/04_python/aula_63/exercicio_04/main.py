#import funcoes

from funcoes import *

limpa()

print("{:=^20}".format("Início") + "\n")

peso = float (input ("Digite seu peso (Kg): "))
altura = float (input ("Digite sua altura (m): "))
imc = peso / (altura ** 2)

print (f"O seu IMC é {imc:.2f}.")

if imc < 18.5:
    print ("Você está abaixo do peso normal")

elif 18.5 <= imc < 25:
    print ("Parabéns! Você está na faixa de peso normal")

elif 25 <= imc < 30:
    print ("Você está em Sobrepeso") 

elif 30 <= imc < 40:
    print ("Você está em Obesidade") 

else:
    print ("Você está em Obesidade Mórbida") 

print("\n" + "{:=^20}".format("Fim"))