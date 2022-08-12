# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

try:
    n1 = float(input("Digite a nota do 1° bimestre: "))
    n2 = float(input("Digite a nota do 2° bimestre: "))
    n3 = float(input("Digite a nota do 3° bimestre: "))
    n4 = float(input("Digite a nota do 4° bimestre: "))
    m = (n1 + n2 + n3 + n4 ) / 4
    print("Média: ", m)

except:
    print("Entrada inválida.")