import os
import time
import math

#Funções 

def calcArea():
    print ("=== Escolha uma opção===")
    print ("t = triângulo")
    print ("r = retângulo")
    print ("c = círculo")

    opcao = input ("Escolha uma opção: ")

    animar("A analisar")

    if (opcao.lower() == "t"):
        base = float (input ("Digite a base do triângulo: "))
        altura = float (input ("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        return (f"A área do triângulo é: {area:.2f}")
    
    elif (opcao == "r"):
        base = float (input ("Digite a base do retângulo: "))
        altura = float (input ("Digite a altura do retângulo: "))
        area = base * altura
        return (f"A área do retângulo é: {area:.2f}")
    
    elif (opcao == "c"):
        raio = float (input ("Digite o raio do círculo: "))
        area = math.pi * (raio ** 2)
        return (f"A área do círculo é: {area:.2f}")

    else:
        return ("Erro nos dados informados, tente novamente!")

# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")

def aguarde(tempo): time.sleep(tempo)

def animar(frase):
    tempo = 0.5
    limpa()
    print (frase, end="", flush=True)
    aguarde(tempo)
    print (".", end="", flush=True)
    aguarde(tempo)
    print (".", end="", flush=True)
    aguarde(tempo)
    print (".", end="", flush=True)
    limpa()