#CALCULADORA DE DESCONTO
# Solicita o preço original do produto ao usuário
preco_original = float(input("Digite o preço original do produto (Folar): R$ "))

# Verifica se o preço é maior que R$100,00
if preco_original > 100:
    # Calcula o valor do desconto (10%)
    desconto = preco_original * 0.10
    # Subtrai o desconto do preço original
    novo_preco = preco_original - desconto
    print(f"Desconto de 10% aplicado. Novo preço: R$ {novo_preco:.2f}")
else:
    print(f"Preço não sofreu desconto. Preço final: R$ {preco_original:.2f}")