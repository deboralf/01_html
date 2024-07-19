from funcoes import *

limpa()

print ("=== Gerador de números inteiros===\n")

numero_inicial = int (input ("Digite o valor incial da sua lista numérica: "))
numero_final = int (input ("Digite o valor final da sua lista numérica: "))
quantidade = int (input ("Quantas vezes você deseja exibir essa lista numérica? "))

print()

for i in range (quantidade):
    if (numero_inicial <= numero_final):
        for loop in range (numero_inicial , numero_final +1): print (loop)

    else:
        for loop in range (numero_inicial, numero_final -1 , -1): print (loop)

print("\n\n")