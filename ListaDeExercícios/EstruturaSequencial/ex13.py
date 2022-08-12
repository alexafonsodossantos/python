# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
try:
    a = float(input("Digite a altura: "))
    s = input("Digite o sexo (M ou F): ")

    if s == "M" or s == "m":
        peso_ideal = (72.7 * a) - 58    
        print("Peso ideal: ", peso_ideal)

    elif s == "F" or s == "f":
        peso_ideal = (62.1 * a) - 44.7
        print("Peso ideal: ", peso_ideal)
    else:
        print("Entrada inválida, tente novamente.")
except:
    print("Entrada inválida.")


