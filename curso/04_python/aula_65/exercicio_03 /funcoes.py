import os

#Funções 

def calcNumeros():
    valor = float (input ("Digite um valor: "))

    if (valor >= 0):
        print ("Positivo")

    else:
        print ("Negativo")
    

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")