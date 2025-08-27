# Verificar letra na palavra
#1. Peça ao usuário uma palavra e depois uma letra. 
# Informe se a letra está na palavra.

palavra = input("Informe uma palavra:")
letra = input("Informe uma letra:")

if letra in palavra:
    print(f"A letra {letra} está na {palavra}")

else:
    letra in palavra
    print(f"A letra {letra} não possui na palavra {palavra}")