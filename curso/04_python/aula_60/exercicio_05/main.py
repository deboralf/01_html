print ("\n\n")
print ("=== Clínica de Nutrição ===")

print()

#Variáveis
nome = input("Digite o nome do(a) Paciente: ")
peso = float (input ("Digite o peso do paciente (Kg): "))
altura = float (input ("Digite a altura do paciente (m): "))
imc = peso / (altura ** 2)

print ()

#Executar
print (f"O(a) paciente ({nome}) está com um IMC de ({imc:.2f}).")

print ("\n\n")