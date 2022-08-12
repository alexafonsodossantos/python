# Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
# 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.

s_h = float(input("Digite o salário hora: "))
q_h = float(input("Digite a quantidade de horas: "))

salario = s_h * q_h
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
liquido = salario - ir - inss - sindicato

print("Salário bruto:  ", salario)
print("Imposto:        ", ir)
print("INSS:           ", inss)
print("Sindicato:      ", sindicato)
print("Salário Líquido:", liquido)

