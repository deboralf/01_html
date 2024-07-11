import os

#Funções 

def calcHoraXadrez():
    hora_inicio = int (input ("Digite a hora de início do Jogo de Xadrez: "))
    hora_fim = int (input ("Digite a hora do fim do Jogo de Xadrez: "))
    hora_total = hora_fim - hora_inicio

    if (hora_inicio > 24 or hora_fim > 24):
        print ("\nAtenção : O máximo de duração do jogo é de 24 horas!")
        return hora_inicio
    
    else:
        hora_total = (hora_inicio == hora_fim) + 24

    print ()

    print (f"A duração total do jogo é de ({hora_total}) horas.")
# Funções Especiais 
def limpa():
    if (os.name == "nt"): os.system("cls")
    else: os.system ("clear")