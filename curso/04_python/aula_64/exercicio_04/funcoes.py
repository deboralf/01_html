import os

#Funções 

def calcEleitores():
    eleitores = int (input("Digite o total de eleitores : "))
    brancos = int (input("Digite o total de votos brancos : "))
    nulos = int (input("Digite o total de votos nulos : "))
    validos = int (input("Digite o total de votos válidos : "))

    percentual_brancos = (brancos / eleitores) * 100
    percentual_nulos = (nulos / eleitores) * 100
    percentual_validos = (validos / eleitores) * 100

    print ()

    print (f" Porcentagem de votos brancos ({percentual_brancos:.2f}) %\n")
    print (f" Porcentagem de votos nulos ({percentual_nulos:.2f}) %\n")
    print (f" Porcentagem de votos validos ({percentual_validos:.2f}) %\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")