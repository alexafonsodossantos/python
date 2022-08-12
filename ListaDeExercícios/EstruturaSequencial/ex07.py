# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.
try:
    l = float(input("Digite o tamanho do lado: "))
    a = l * l
    d = a * 2
    print("Área: ", a)
    print("Dobro da área: ", d)
except:
    print("Entrada inválida.")
