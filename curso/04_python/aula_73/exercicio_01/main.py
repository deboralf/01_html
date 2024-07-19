from funcoes import *
import globais

limpa()

p1 = "Fabricio"
p2 = "Debora"
p3 = "Maria"

# Criar um array
pessoas = ["Fabricio", "Debora", "Maria"]
print (pessoas)

print (pessoas [1])

# Editar uma posição específica
pessoas [2] = "João"
print (pessoas [2])

# Adicionar um novo elemento no final do Array
pessoas.append ("Bruno")
pessoas.append ("Ana")
print (pessoas)

# Adicionar um novo elemento em uma posição específica
pessoas.insert (0,"Alice")
pessoas.insert (2,"Felipe")
print (pessoas)

# Apagar um elemento no final do Array 
pessoas.pop()
pessoas.pop()
print (pessoas)

# Apagar um elemento em uma posição específica
pessoas.pop(0)
pessoas.pop(2)
print (pessoas)

# Apagar um elemento específico
pessoas.remove("Fabricio")
print (pessoas)

#for p in pessoas: print (p)

print("\n\n")