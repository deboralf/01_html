import os

#Funções 

def calcMacas():
    quantidade = int (input ("Digite a quantidade de maçãs: "))

    if (quantidade >= 12):
        valor = 1

    else:
        valor = 1.3

    valor_total= quantidade * valor
    
    print (f"O valor total da compra é: {valor_total:.2f}€")
        
    
# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")