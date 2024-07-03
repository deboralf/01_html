print ("\n\n")

resposta = "sim"
saldo = 12.00

condicao_1 = (resposta.lower() == "sim" or resposta.lower() == "s" or resposta.lower() == "y" or resposta.lower() == "yes")

condicao_2 = (resposta.lower() == "sim" or saldo >= 20.00)

condicao_3 = (resposta.lower() == "sim" and saldo >= 20.00)

condicao_4 = (not saldo > 20.00)

condicao_5 = ((resposta.lower == "sim" or resposta.lower == "s") and saldo >= 20.00)

print (f"Condição 1: ({condicao_1})")
print (f"Condição 2: ({condicao_2})")
print (f"Condição 3: ({condicao_3})")
print (f"Condição 4: ({condicao_4})")
print (f"Condição 5: ({condicao_5})")

print ("\n\n")