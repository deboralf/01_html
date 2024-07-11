import os

#Funções 

def calcValor():
    valor = float (input ("Digite um valor: "))

    if (valor > 10):
        print ("é maior que 10!")

    else:
        print ("Não é maior que 10!")
    

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")