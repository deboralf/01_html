from funcoes import *

limpa()

frutas = ["laranja", "maçã" , "morango" , "clementina" , "uva"]

total_posicoes = len(frutas)
print (frutas[total_posicoes-1])

#método global
print (frutas [len(frutas)-1])

#específico para o python
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

#Sublistas em python
print (frutas[0:3])
print (frutas[3:5])

print("\n\n")