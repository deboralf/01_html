print ("\n\n")

print ("=== Início ===\n")

pergunta = input ("- Está a chover? ")

print ()

if (pergunta.lower() == "sim"):
   
   pergunta_2 = input ("- Você quer sair de casa? ")

   if (pergunta_2.lower() == "sim"):
      print ("Ir ao cinema")
   else:
      print ("Pedir um Glovo")

else:
 print ("Ir ao Parque")  

print ("\n=== Fim ===")
print ("\n\n")