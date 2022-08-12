# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.
# Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.

try:
    C = float(input("Digite a temperatura (em °C): "))
    F = C * 1.8 + 32 
    print("Temperatura (em °F): ", F)
except:
    print("Entrada inválida. ")


