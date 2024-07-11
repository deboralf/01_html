import os

#Funções 

def calcMediaAluno():
    n1 = float (input ("Digite sua nota 1: "))
    n2 = float (input ("Digite sua nota 2: "))
    media = (n1 + n2) / 2
    print (f"O(a) aluno(a) obeteve uma média final de ({media:.2f}) valores.")

    if (media >= 6):
        print ("Você foi aprovado!")

    else:
        print ("Você chumbou!")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")