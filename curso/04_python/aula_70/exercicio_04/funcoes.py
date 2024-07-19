import os
import time

# Funções

# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(tempo): time.sleep(tempo)

def animar(frase):
  tempo = 0.5
  limpa()

  print(frase, end="", flush=True)
  for loop in range(3):
    print(".", end="", flush=True)
    aguarde(tempo)

  limpa()

def animar2 (frase):
  tempo = 0.2
  limpa()
  frase += "..."

  for letra in frase:
    print (letra, end ="", flush = True)
    aguarde (tempo)

  limpa()

