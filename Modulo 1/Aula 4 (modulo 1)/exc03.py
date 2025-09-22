#Peça uma palavra a substituir. Depois peça uma nova palavra e use .replace() para fazer a troca.

palavra_original = input("Digite uma palavra: ")
nova_palavra = input("Digite a nova palavra para substituir por: ")
    
texto = f"A palavra original é: {palavra_original}"
texto_modificado = texto.replace(palavra_original, nova_palavra)
print("Texto modificado:")
print(texto_modificado)