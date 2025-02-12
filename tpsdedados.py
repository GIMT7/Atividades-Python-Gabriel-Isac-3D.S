#Exercício 1

#pes = int(input("Qual o seu peso ? "))
#alt = float(input("Qual a sua altura em metros ? "))
#imc = pes/(alt*alt)
#print(f'O seu IMC é igual a {imc}')

#Exercício 2

#cel = float(input("Qual é a temperatura em Celsius  ? "))
#fah = ((cel*9)/5)+ 32
#print(f'A temperatura em fahrenheit é igual a {fah}')

#Exercício 3

#rai = float(input("Qual é o raio do círculo ? "))
#are = ((rai*rai)*3.14)
#print(f'A área do círculo é igual a {are}')

#Exercício 4

#dis = float(input("Qual a distância em KM do trajeto  ? "))
#vel = float(input("Qual é a velocidade média do veículo durante o percurso em km/h ? "))
#temp = dis/vel
#print(f'O tempo de viagem é igual a {temp} horas')

#Exercício 5

ini = int(input("Qual o seu saldo inicial da conta ? "))
opc = int(input(" 1- REALIZAR SAQUE             2- REALIZAR DEPÓSITO  "))
if opc == 1:
    saq= float(input("Qual o valor do saque a ser realizado ? "))
    fin = ini - saq
    print(f'O seu saldo é igual a {fin}')

if opc == 2:
    dep = float(input("Qual o valor do depósito a ser realizado ? "))
    fini = ini+dep
    print(f'O seu saldo é igual a {fini}')
 
   

