# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
# em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
# preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

m2 = float(input("Digite a área a ser coberta (em m²): "))

litros = (m2 / 6) * 1.1

qt_18 = litros / 18
qt_36 = litros / 3.6

if qt_18 > int(qt_18):
    qt_18 = int(qt_18 + 1)
elif qt_18 < 0:
    qt_18 = 1

if qt_36 > int(qt_36):
    qt_36 = int(qt_36 + 1)
elif qt_36 < 0:
    qt_36 = 1

v_18 = qt_18 * 80
v_36 = qt_36 * 25


r_36 = (litros % 18) / 3.6

if r_36 > int(r_36):
    r_36 = int(r_36 + 1)

elif r_36 == 0:
    r_36 = 0

elif r_36 < 1:
    r_36 = 1

r_18 = int(litros / 18)

v_r = (r_36 * 25) + (r_18 * 80)


print("Total gasto (18L): ", v_18)
print("Total gasto (3.6L): ", v_36)
print("Total gasto (18 e 3.6L): ", v_r)


