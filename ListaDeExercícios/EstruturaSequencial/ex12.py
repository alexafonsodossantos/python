# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
try:
    a = float(input("Digite a altura: "))
    peso_ideal = (72.7 * a) - 58
    print("Peso ideal: ", peso_ideal)
except:
    print("Entrada inválida.")
