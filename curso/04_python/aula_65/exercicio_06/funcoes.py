import os

#Funções 

def calcIdadeEleitor():
    ano_nascimento = int (input ("Qual o ano de nascimento do Eleitor? "))
    ano_atual = int (input ("Qual o ano atual? "))
    resultado = ano_atual - ano_nascimento

    if (resultado >= 16):
        print ("Pode votar")

    else:
        print ("Não pode votar")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")