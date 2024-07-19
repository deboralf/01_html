from funcoes import *

limpa()

print ("=== Break no while ===\n")

tentativas = 1

while (tentativas <= 5):
    resposta = input(f"Você deseja encerrar o loop WHILE na tentativa ({tentativas}/5): ")
    
    if (resposta.lower() == "sim"):
        print("Você não ultrapassou o número de tentativas")
        break
    
    tentativas += 1

    print ()

else:
    print("\nVocê atingiu o limite de 5 tentativas.\n")

print()

print ("=== Break no for ===")

print ()

for tentativas in range(1, 6): 
    resposta = input(f"Você deseja encerrar o loop WHILE na tentativa ({tentativas}/5): ")
    
    if (resposta.lower() == "sim"):
        print("Você não ultrapassou o número de tentativas")
        break
    tentativas +=1

    print ()

else:
    print ("Você atingiu o limite de 5 tentativas.")

print("\n\n")