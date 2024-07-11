import os

#Funções 

def calcIdade():
    print ("Diga quantos anos, dias e meses de vida você tem:")
    idade_anos = int (input("Anos: "))
    idade_meses = int (input("Meses: "))
    idade_dias = int (input("Dias: "))

    idade_total = (idade_anos * 365) + (idade_meses * 30) + idade_dias

    print (f"A sua idade somente em dias é ({idade_total})\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")