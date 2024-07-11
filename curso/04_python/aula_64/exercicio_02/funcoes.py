import os

#Funções 

def calcRetangulo():
    base = float (input("Digite a base do retângulo: "))
    altura = float (input("Digite a altura do retângulo: "))
    area = base * altura
    print (f"A área do retângulo é ({area}))\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")