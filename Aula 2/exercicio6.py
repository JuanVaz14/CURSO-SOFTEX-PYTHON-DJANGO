# VERIFICADOR DE PAR OU IMPAR
#Peça ao usuário um número inteiro
#use o operarador de modulo (%) e uma estrutura if - else para determinar e imprimir se o número é par ou impar

numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
   print(f"O numero {numero} é o impar.")
             