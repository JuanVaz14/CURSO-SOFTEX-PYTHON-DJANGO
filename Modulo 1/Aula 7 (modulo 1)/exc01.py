# Simulação de pedido na Lanchonete
 #Crie um programa que simula um sistema de pedido em uma lanchonete.
#1. Defina o preço de um hamburger
#2. Defina um código de cupom de desconto.
#3. O Programador deve pedir ao cliente o nome do produto repetidamente até que o produito correto seja digitado.
#4. Após a escolha, o programa deve perguntar se o cliente tem um cupom de desconto.
#5. se o cliente digitar o cupom correspondente, aplique o desconto.
#6. Calcular o preço final do produto e exiba o total a pagar.
#7. O Programa deve encerrar após o pedido ser finalizado.

preco_hamburger = 20.0
codigo_cupom = "DESCONTO10"

while True:
    produto = input("Digite o nome do produto (Hamburger): ")
    if produto.lower() == "hamburger":
        break
    tentativas_produto += 1
    print("Produto inválido. Tente novamente.")
    if tentativas_produto >= 3:
        print("Número máximo de tentativas para o produto atingido. Encerrando o programa.")
        exit()

tem_cupom = input("Você tem um cupom de desconto? (s/n): ")
valor_final = preco_hamburger
cupom = ""
if tem_cupom.lower() == "s":
    tentativas_cupom = 0
    while True:
        cupom = input("Digite o código do cupom: ")
        if cupom == codigo_cupom:
            valor_final = preco_hamburger * 0.90  # Aplica 10% de desconto
            break
        else:
            tentativas_cupom += 1
            print("Código do cupom incorreto. Tente novamente.")
            if tentativas_cupom >= 3:
                print("Número máximo de tentativas para o cupom atingido. Encerrando o programa.")
                exit()

print(f"O valor original do produto é: R$ {preco_hamburger:.2f}")
if tem_cupom.lower() == "s" and cupom == codigo_cupom:
    print(f"O valor com desconto de 10% é: R$ {valor_final:.2f}")
else:
    print(f"Total a pagar: R$ {valor_final:.2f}")


