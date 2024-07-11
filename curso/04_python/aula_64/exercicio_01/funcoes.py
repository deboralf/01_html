import os

#Funções 

def antecessor():
    valor = int (input("Digite um valor: "))
    antecessor = valor - 1
    print (f"O antecessor de ({valor}), é ({antecessor})\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")