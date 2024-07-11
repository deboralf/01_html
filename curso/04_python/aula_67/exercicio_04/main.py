from funcoes import *

limpa()

print("{:=^20}".format("Início") + "\n")

resposta_1 = input("- Deseja tirar a carta de condução? ")

print()

if (resposta_1.lower() == "sim"):

    resposta_2 = ""
    contagem = 1
    while (resposta_2.lower() != "sim"):
        print (f"Estude para o teste ({contagem})")
        print ()
        resposta_2 = input(f"Você passou no teste ({contagem})? ")
        contagem += 1
        print ()

    print ("Parabéns!")
    print (f"Você passou no teste ({contagem-1})!")

elif (resposta_1.lower() == "nao"):
    print ("Então utilize o transporte público")
    
else:
    print ("Erro nos dados informados, tente novamente!")

print("\n" + "{:=^20}".format("Fim"))