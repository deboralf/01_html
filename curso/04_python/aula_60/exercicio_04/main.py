print ("\n\n")
print ("=== Média Escolar ===")

print()

#Variáveis
nome = input("Digite o nome do aluno(a): ")
nota_1 = float (input ("Digite sua nota da prova 1: "))
nota_2 = float (input ("Digite sua nota da prova 2: "))
nota_3 = float (input ("Digite sua nota do trabalho de casa: "))
media = (nota_1 + nota_2 + nota_3) / 3

print ()

#Executar
print (f"O(a) aluno(a) ({nome}) obeteve uma média final de ({media:.2f}) valores.")

print ("\n\n")