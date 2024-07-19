import os
import time

# Funções
def multiplos():
  numero = int(input("- Digite um número inteiro: "))
  x = 0

  animar("Aguarde")

  print (f"--- Múltiplos de ({numero}) entre 0 e 100---")

  print()

  while (numero * x <= 100):
    print (f"{x}")
    x += numero

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