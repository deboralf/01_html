from funcoes import *

limpa()

print ("=== Gerador de números inteiros===\n")

numero_inicial = int (input ("Digite o valor incial da sua lista numérica: "))
numero_final = int (input ("Digite o valor final da sua lista numérica: "))

print()

if (numero_inicial < numero_final):
    for loop in range(numero_inicial, numero_final +1): print (loop)

else:
    for loop in range(numero_inicial, numero_final -1, -1): print (loop)

print("\n\n")