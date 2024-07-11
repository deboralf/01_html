print ("\n\n")

def calcularIMC():
    nome = input("Digite o nome do paciente: ")
    peso = float (input ("Digite o peso do paciente (Kg): "))
    altura = float (input ("Digite a altura do paciente (m): "))
    imc = peso / (altura ** 2)
    print (f"O IMC do(a) ({nome}) é ({imc:.1f})\n\n")

calcularIMC()
calcularIMC()
calcularIMC()
calcularIMC()
calcularIMC()
calcularIMC()
calcularIMC()

print ("\n\n")