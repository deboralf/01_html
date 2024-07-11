import os
import time

#Funções 

def fichaCandidatura():
    nome = input ("Digite seu nome: ")
    idade = int (input ("Digite sua idade: "))
    conhecimento = input ("Você tem conhecimentos em progamação? ")

    animar("A analisar")

    print (f"===Ficha de Candidatura===")
    print (f"Nome : {nome}")
    print (f"Nome : {idade}")
    
    if (idade >= 18 and conhecimento.lower() == "sim" or conhecimento.lower() == "s" ):
        return ("Status de Candidatura: ( Aprovado para o estágio )")

    elif (idade >=18 and conhecimento.lower() == "nao" or conhecimento.lower() == "n" ):
        return ("Status de Candidatura: ( Não aprovado para o estágio )")

    elif (idade < 18 and conhecimento.lower() == "sim" or conhecimento.lower() == "s" ):
        return ("Status de Candidatura ( Aprovado para escola de programação )")

    elif (idade < 18 and conhecimento.lower() == "nao" or conhecimento.lower() == "n" ):
        return ("Status de Candidatura: ( Não aprovado para escola de programação )")

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
