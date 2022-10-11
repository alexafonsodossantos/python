import os
from classes import Carro
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="pass",
  database="concessionaria"
)

carros = []
mycursor = mydb.cursor()
bd_list = []
mycursor.execute("SELECT * FROM tb_veiculos")
myresult = mycursor.fetchall()
for x in myresult:
  lista = list(x)
  bd_list.append(lista)

for a in bd_list:
  carro = Carro()
  carro.placa = a[1]
  carro.marca = a[2]
  carro.modelo = a[3]
  carro.ano = a[4]
  carro.kilometragem = a[5]
  carro.cor = a[6]
  carro.preco = a[7]
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
        carro.criar_veiculo()
        carros.append(carro)
        mycursor = mydb.cursor()
        sql = """INSERT INTO tb_veiculos (
            placa, 
            marca, 
            modelo, 
            ano, 
            cor, 
            kilometragem, 
            preco
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        val = (
            carro.placa, 
            carro.marca, 
            carro.modelo, 
            carro.ano, 
            carro.cor, 
            carro.kilometragem, 
            carro.preco
            )
        mycursor.execute(sql, val)
        mydb.commit()

        print("Veículo cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        os.system('cls')

    elif escolha == 2:
        for carro in carros:
            carro.mostrar_veiculo()
        input("Pressione qualquer tecla para continuar.")
        os.system('cls')
    
    elif escolha == 3:
        placa = input("Digite a placa: ")
        for carro in carros:
            if carro.placa == placa:
                carro.mostrar_veiculo()
                input("Pressione qualquer tecla para continuar.")
                os.system('cls')

    elif escolha == 4:
        placa = input("Digite a placa: ")
        for carro in carros:
            if carro.placa == placa:
                carros.remove(carro)
                mycursor = mydb.cursor()
                sql = "DELETE FROM tb_veiculos WHERE placa = '"+placa+"'"
                mycursor.execute(sql)
                mydb.commit()
                print("Veículo removido.")
                input("Pressione qualquer tecla para continuar.")
                os.system('cls')

    elif escolha == 5:
        print("Até a próxima!")
        break
