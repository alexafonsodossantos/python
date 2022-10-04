import os

import csv





class Carro:
    placa = ""
    marca = ""
    modelo = ""
    ano = 0
    kilometragem = 0
    cor = ""
    preco = 0.0

carros = []

with open('carros.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        carro = Carro()
        carro.placa = row[0]
        carro.marca = row[1]
        carro.modelo = row[2]
        carro.ano = row[3]
        carro.kilometragem = row[4]
        carro.cor = row[5]
        carro.preco = row[6]
        carros.append(carro)



while True:

    print("--- SISTEMA CONCESSIONÁRIA ---")
    print("1 - Cadastrar veículos")
    print("2 - Visualizar todos os veículos")
    print("3 - Pesquisar veículo")
    print("4 - Remover veículo")
    print("5 - Sair")

    escolha = int(input("Sua escolha: "))

    if escolha == 1:
        carro = Carro()
        carro.placa = input("Digite a placa: ")
        carro.marca = input("Digite a marca: ")
        carro.modelo = input("Digite o modelo: ")
        carro.ano = int(input("Digite o ano: "))
        carro.kilometragem = int(input("Digite a kilometragem: "))
        carro.cor = input("Digite a cor: ")
        carro.preco = float(input("Digite o preço: "))

        carros.append(carro)

        save = open('carros.csv', "a")
        save.write(carro.placa + ";")
        save.write(carro.marca + ";")
        save.write(carro.modelo + ";")
        save.write(str(carro.ano) + ";")
        save.write(str(carro.kilometragem) + ";")
        save.write(carro.cor + ";")
        save.write(str(carro.preco)+ "\n")
        save.close()
        
        print("Veículo cadastrado com sucesso!")
        input("Pressione qualquer tecla para continuar.")
        os.system('cls')

    elif escolha == 2:
        for carro in carros:
            print("------------------------")
            print("Placa: ", carro.placa)
            print("Marca: ", carro.marca)
            print("Modelo: ", carro.modelo)
            print("Ano: ", carro.ano)
            print("Kilometragem: ", carro.kilometragem)
            print("Cor: ", carro.cor)
            print("Preço: ", carro.preco)
        input("Pressione qualquer tecla para continuar.")
        os.system('cls')
    
    elif escolha == 3:
        placa = input("Digite a placa: ")
        for carro in carros:
            if carro.placa == placa:
                print("Placa: ", carro.placa)
                print("Marca: ", carro.marca)
                print("Modelo: ", carro.modelo)
                print("Ano: ", carro.ano)
                print("Kilometragem: ", carro.kilometragem)
                print("Cor: ", carro.cor)
                print("Preço: ", carro.preco)
                input("Pressione qualquer tecla para continuar.")
                os.system('cls')



    elif escolha == 4:
        placa = input("Digite a placa: ")
        for carro in carros:
            if carro.placa == placa:
                carros.remove(carro)
                print("Veículo removido.")
                input("Pressione qualquer tecla para continuar.")
                os.system('cls')

    elif escolha == 5:
        print("Até a próxima!")
        break