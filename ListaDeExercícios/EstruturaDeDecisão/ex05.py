# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))

if n1 > n2 and n1 > n3:
    print(n1)

if n2 > n1 and n2 > n3:
    print(n2)

if n3 > n1 and n3 > n2:
    print(n3)

