print ("\n\n")

def calcK(c):
    k = c + 275.15
    print (f"({c:.2f} c ) = ({k:.2f} k )")

def calcF(c):
    f = c * 1.8 + 32
    print (f"({c:.2f} c ) = ({f:.2f} k )")

c = float (input("Digite uma temperatura em Celsius: "))
print ()
escala = input ("Você deseja converter para Kelvin ou Fahrenheit?")

if (escala.lower() == "k"): calcK(c)
elif (escala.lower() == "f"): calcF(c)
else: print ("Opção inv")

print ("\n\n")