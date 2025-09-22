#Contador de vogais
#Faça um programa que pede ao usuário para digitar uma palavra. Use o loop for para percorrer a palvra e contar quantas vogais (a,e,i,o,u) ela possui.
#O programa deve se desconciderar maiuscula ou minuscula

palavra = input("Digite uma palavra: ")
contador = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        contador += 1

print(f"A palavra '{palavra} possui {contador} vogais.")