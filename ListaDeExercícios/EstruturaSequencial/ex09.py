# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

try:
    F = float(input("Digite a temperatura (em °F): "))
    C = 5 * ((F-32) / 9)
    print("Temperatura (em °C): ", C)
except:
    print("Entrada inválida.")

