# Pede o preço original do produto
preco = float(input("Digite o preço do produto: "))

# Verifica se o preço é maior que 100
if preco > 100:
    desconto = preco * 0.10
    novo_preco = preco - desconto
    print("O novo preço com desconto é:")
    print(novo_preco)
else:
    print("O produto não tem desconto. O preço é:")
    print(preco)