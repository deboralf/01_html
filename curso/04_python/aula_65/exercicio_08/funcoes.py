import os

#Funções 

def calcOrdemCrescente():
    numero_1 = float (input ("Digite um número: "))
    numero_2 = float (input ("Digite outro número: "))

    if (numero_1 == numero_2):
        print ("Não serão lidos valores iguais")

    else:
        if (numero_1 < numero_2):
            print (f"{numero_1},{numero_2}")

        else:
            print (f"{numero_2},{numero_1}")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")