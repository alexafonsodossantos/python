# Faça um Programa que peça um número e então mostre a mensagem 
# O número informado foi [número].

try:
    n = int(input("Digite um número: "))
    print("O número digitado foi: ", n)
except:
    print("Entrada inválida.")

