# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

try: 
    r = float(input("Digite o raio: "))
    pi = 3.141592
    A = pi * (r * r)
    print("Área do círculo: ", A)
except:
    print("Entrada inválida.")