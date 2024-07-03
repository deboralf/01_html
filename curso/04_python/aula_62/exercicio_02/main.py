print ("\n\n")

print ("=== Roupa para passeio ===\n")
resposta = float (input("- Qual a temperatura atual? "))

print ()

if (resposta <= 18):
    print ("Use casaco")

elif (resposta < 28):
     print ("Use roupas normais")

else:
    print ("Use roupas de praia")

print ()

resposta_2 = input ("- Está a chover? ")

print ()

if (resposta_2.lower() == "sim" or resposta_2.lower() == "s" or resposta_2.lower() == "y" or resposta_2.lower() == "yes"):
   print ("Pegar Guarda-chuva") 

print ("Ir Passear")  

print ("\n=== Fim ===")
print ("\n\n")