nome = "Enderson"
peso = 85
altura = 1.95
imc = peso / altura ** 2
print(nome, "tem", altura,'de altura')
print("pesa",peso,'e seu imc é',imc)
print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura, e seu imc é {imc:.4}'
print(linha_1)