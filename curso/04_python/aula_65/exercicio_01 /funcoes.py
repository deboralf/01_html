import os

#Funções 

def mediaAluno():
    n1 = float (input ("Digite sua nota da prova 1: "))
    n2 = float (input ("Digite sua nota da prova 2: "))
    n3 = float (input ("Digite sua nota da prova 3: "))
    media_final = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print (f"O(a) aluno(a) obeteve uma média final de ({media_final:.2f}) valores.")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")