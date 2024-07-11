import os

#Funções 

def calcOrdenado():
    ordenado = float (input("Digite o seu ordenado atual: "))
    reajuste = float (input("Qual será o reajuste percentual? "))

    valor_reajuste = ordenado * (reajuste / 100)
    novo_ordenado = ordenado + valor_reajuste

    print (f"O novo ordenado será ({novo_ordenado}€)\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")