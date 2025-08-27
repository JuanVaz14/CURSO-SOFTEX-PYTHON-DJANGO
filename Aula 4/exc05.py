#Peça uma frase e uma palavra a substituir.

frase = input("Por favor, digite uma frase: ")
palavra_original = input("Digite a palavra que você quer substituir: ")
palavra_substituir = input("Digite a palavra para substituir por: ")
    
frase_modificada = frase.replace(palavra_original, palavra_substituir)
print("Frase modificada:")
print(frase_modificada)