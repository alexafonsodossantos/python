class Carro:
    placa = ""
    marca = ""
    modelo = ""
    ano = 0
    kilometragem = 0
    cor = ""
    preco = 0.0

    def criar_veiculo(self):
        self.placa = input("Digite a placa: ")
        self.marca = input("Digite a marca: ")
        self.modelo = input("Digite o modelo: ")
        self.ano = int(input("Digite o ano: "))
        self.kilometragem = int(input("Digite a kilometragem: "))
        self.cor = input("Digite a cor: ")
        self.preco = float(input("Digite o preço: "))
    
    def mostrar_veiculo(self):
        print("------------------------")
        print("Placa: ", self.placa)
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)
        print("Kilometragem: ", self.kilometragem)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)
