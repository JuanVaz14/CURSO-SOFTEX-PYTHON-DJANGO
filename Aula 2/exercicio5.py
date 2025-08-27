# MAIOR DE DOIS NUMEROS
# Peça ao usuário para digitar dois números inteiros.
# Use if-else para descobrir qual dos dois é maior e imprima o resultado.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O {num1} é maior")
elif num2 < num1:
    print(f"O {num2}é o maior") 
else:
    print("Os dois números são iguais.")