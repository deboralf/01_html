import os
import time
import globais

# Funções
def menu():
  print ("\n1-Vender.\n")
  print ("2-Ver Histórico.\n")
  print ("0-Sair.\n")

def vender():
  print ("--- Vender ---")
  descricao = (input("\nDescrição da Venda: "))
  valor = float (input("Valor total da venda: "))
  if (valor > 0 ):
    globais.saldo += valor
    globais.historico += f"Venda de ({descricao}) no valor de ({valor:.2f} €)\n"
    print ("\n=== Sucesso! ===\n")
  else:
    globais.historico += f"Tentativa de venda de ({valor:.2f} €)"
    print ("valor inválido")

def exibirHistorico():
  print ("--- Histórico ---\n")
  print (f"Total de vendas: ({globais.saldo:.2f}€) \n")
  print (globais.historico)

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