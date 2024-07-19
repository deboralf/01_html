from funcoes import *

limpa()

frutas = ["uva","maçã","morango","ananás", "banana", "laranja"]
print(frutas)

print()

print("=== Lista de Frutas com For ===\n")

for f in frutas: print(f)
print()

print("=== Lista de Frutas com For + Range() ===\n")

for i in range(len(frutas)): print (f"{i+1} - {frutas[i]}")
print()

print("=== Lista de Frutas com For + Reverse() ===\n")

for f in reversed(frutas): print(f)
print()

print("=== Lista de Frutas com For + Range () Reverso ===\n")

for i in range(len(frutas) -1, -1, -1): print  (f"{i+1} - {frutas[i]}")
print()

print("\n\n")