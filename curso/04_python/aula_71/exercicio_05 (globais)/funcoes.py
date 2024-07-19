import os
import time
import globais

# Funções
def menu():
  print ("\n1-Depósitos\n")
  print ("2-Levantamentos\n")
  print ("3-Pagamentos\n")
  print ("\n0-Sair\n")

def depositar():
  valor = float (input("Digite o valor que será depositado: "))
  if (valor > 0 ):
    globais.saldo += valor
    print ("\n=== Sucesso! ===\n")
  else: print ("valor inválido")

def levantar():
  valor = float (input("Digite o valor que será levantado: "))
  if (valor > 0 and valor <= globais.saldo): 
    globais.saldo -= valor
    print ("\n=== Sucesso! ===\n")
  else: print ("valor inválido")

def pagar():
  descricao = (input("Descrição do pagamento: "))
  valor = float (input("Digite o valor do pagamento: "))
  if (valor > 0 and valor <= globais.saldo): 
    globais.saldo -= valor
    print ("\n=== Sucesso! ===\n")
  else: print ("valor inválido")

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

def carregueEnter():
  input ("Carregue <enter> para continuar")