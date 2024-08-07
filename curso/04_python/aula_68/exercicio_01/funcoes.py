import os
import time

# Funções
def tabuada():
  numero = int(input("- Digite um número para obter a sua tabuada: "))
  x = 1

  animar("Aguarde")

  while (x <= 10):
    resultado = numero * x
    print (f"{numero:>2} x {x} = {resultado}")
    x += 1

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