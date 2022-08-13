# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
elif n1 == n2:
    print("Números iguais.")


    