# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

try: 
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    n3 = float(input("Digite um número real: "))
    r1 = (n1 * 2) * (n2 / 2)
    r2 = (n1 * 3) + n3
    r3 = n3 ** 3
    print("O produto do dobro do primeiro com a metade do segundo é: ", n1)
    print("A soma do triplo do primeiro com o terceiro é: ", r2)
    print("O terceiro elevado ao cubo é: ", r3)
except:
    print("Entrada inválida. ")