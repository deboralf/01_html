import os

#Funções 


# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")