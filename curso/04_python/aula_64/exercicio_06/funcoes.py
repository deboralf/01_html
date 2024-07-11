import os

#Funções 

def calcCarro():
    fabrica = float (input("Digite o custo de fábrica do carro: "))
    imposto = fabrica * 0.73
    custo = imposto + fabrica

    print ()

    print (f"O custo final do carro será ({custo:.2f})\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")