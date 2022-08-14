# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

s = input("Digite M para Masculino e F para Feminino: ")

if s == "m" or s == "M":
    print("M - Masculino")
elif s == "f" or s == "F":
    print("F - Feminino")
else:
    print("Sexo inválido.")