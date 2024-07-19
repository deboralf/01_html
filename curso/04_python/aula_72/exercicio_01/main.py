from funcoes import *
import globais

limpa()

while (True):
    print ("=== Padaria do Python ===\n")

    menu()

    opcao = int(input("-Opção: "))

    limpa()

    animar("Aguarde")

    if (opcao == 1): vender()
    elif (opcao == 2): exibirHistorico()
    elif (opcao == 0):
        animar("Saindo")
        aguarde (2)
        break

    else: print ("\n=== Opção inválida ===\n")
    
    carregueEnter()
    limpa()

print("\n\n")