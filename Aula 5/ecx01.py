#Tabuada simples
#Crie um programa que solicita ao usuário um número inteiro. Em seguida, use um loop for para imprimir a tabuada desse número de 1 a 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")