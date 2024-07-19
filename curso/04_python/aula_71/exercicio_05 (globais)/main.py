from funcoes import *
import globais

limpa()

while (True):
    print ("=== Multibanco Python ===\n")
    print (f"Bem-vindo(a) {globais.nome}\n")
    print (f"Saldo = {globais.saldo}")

    menu()

    opcao = int(input("-Opção: "))

    limpa()

    animar("Aguarde")

    if (opcao == 1): depositar()
    elif (opcao == 2): levantar()
    elif (opcao == 3): pagar()
    elif (opcao == 0):
        animar("Saindo")
        aguarde (2)
        break

    else: print ("\n=== Opção inválida ===\n")
    input ("Carregue <enter> para continuar")
    limpa()

print("\n\n")