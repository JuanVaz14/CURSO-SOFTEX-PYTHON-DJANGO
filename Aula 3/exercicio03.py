#Peça ao usuário uma frase e verifique se a palavra "bomba" aparece nela

frase = input("Digite uma frase: ")
palavra = "bomba"

if palavra in frase:
    print(f"A palavra '{palavra}' aparece na frase '{frase}'")

else:
    print(f"A palavra '{palavra}' não aparece na frase")