import os

#Funções 

def calcVendas():
    salario = float (input("Digite o valor do salario fixo: "))
    quantidade = float (input("Qual o valor total das vendas(€)? "))
    carros = int (input("Quantos carros foram vendidos? "))
    comissao = float (input("Digite o valor da comissão: "))

    valor_carros = (quantidade * 0.05)
    comissao_final = comissao * carros
    salario_final = valor_carros + salario + comissao_final


    print (f"O salário final do funcionário é ({salario_final} €)\n")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")