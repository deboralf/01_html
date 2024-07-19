import os
import time

# Funções
def calcNumeros():
  print ("=== Contabilizador de Números ===")
  print ()
  quantidade = int(input("- Digite o total de números que serão analisados: "))
  par = []
  impar = []

  x = 0

  animar("Aguarde")

  while ( x <= quantidade):
    numero = int(input (f"Digite o ({x+1}º) número: "))
    quantidade += 1
    x += 1

  if (numero % 2 == 0):
    par = par + (numero)

  else:
    impar = impar + (numero)

  print (f"Total de números PARES ({par:.2f}).")
  print (f"Total de números IMPARES ({impar:.2f}).")

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