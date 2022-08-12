# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

try:
    s = float(input("Digite o seu ganho por hora: "))
    h = float(input("Digite a quantidade de horas trabalhadas: "))
    sal = s * h
    print("Salário: ", sal)
except:
    print("Entrada inválida.")