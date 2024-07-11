import os

#Funções 
def exibirMensagens ():
    print ("Mensagem 1")
    print ("Mensagem 2")
    print ("Mensagem 3\n")

def calcDobro ():
    x = float (input("Digite um número: "))
    dobro = x * 2
    print (f"O dobro de ({x}) é ({dobro})\n")

def calcTriplo(valor):
    triplo = valor * 3
    print (f"O triplo de ({valor}) é ({triplo})\n")

def descontar10 (valor):
    resultado = valor * 0.9
    print (f"Valor descontado: ({resultado:.2f} euros )\n")

def descontar10ComRetorno(valor):
    resultado = valor * 0.9 
    return resultado

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")
