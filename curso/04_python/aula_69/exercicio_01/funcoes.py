import os
import time

# Funções
def calcNumeros():
    quantidade = int(input("Digite a quantidade de números a serem analisados: "))
    
    loop = 1
    par = 0
    
    print()
    
    while (loop <= quantidade):
        numero = int(input(f"Digite o ({loop}) número: "))
        resto = numero % 2
        if (resto == 0):
            par += 1
        loop += 1
        
    impar = quantidade - par

    print(f"Os números pares são: {par}")
    print(f"Os números ímpares são: {impar}")


# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(tempo): time.sleep(tempo)

def animar(frase):
  tempo = 0.3
  limpa()
  print(frase, end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  limpa()