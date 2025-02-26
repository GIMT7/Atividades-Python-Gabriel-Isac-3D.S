
#Exercicio 2

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        
        dep = int(input(self.titular, ",digite o valor a ser depositado: "))
        self.saldo + dep
        print(self.saldo)
    
    
    def sacar(self):
        int = i
        for i in range(1):
             
        sac = int(input(self.titular, ",digite o valor a ser sacado: "))
    
        if sac > self.saldo:
           print("Esse valor não pode ser sacado por ser maior que o disponível")
           i=-1
    
        else: 
            self.saldo - sac
            print(self.saldo)
        
    def Menu(self): 
        print( self.titular, "Escolha uma opção abaixo: ")
        
        while opc < 1 or opc > 3:
            opc = int(input( "1- REALIZAR DEPÓSITO\n", "2- REALIZAR SAQUE \n" ))
         
        if opc == 1 :
            self.depositar()
        if opc == 2 :
            self.sacar()
        if opc >= 3 or opc <= 0:
            print("Opção inválida...")
        
usu1 = ContaBancaria("Aline", 0)

usu1.Menu()


       ##Exercicio 1

class Carro:
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R${self.valor}")
       
modelo = input("Digite o modelo do carro: ")
cor = input("Digite o cor do carro: ")
ano = input("Digite o ano do carro: ")
valor = input("Digite o valor do carro: ")

car1 = Carro(modelo, cor, ano, valor)

car1.exibir_informacoes()
