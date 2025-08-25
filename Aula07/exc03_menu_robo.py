# Exercicio 3: Menu de comandos para um robô
#Crie um programa que simula o controle de um robô simples com um menu de comandos.
#1 O Robô pode estar em uma posição inicial(você pode usar uma variável para isso, por explemplo, a posição 0).
#2. O programa deve exibir um menu com as seguintes posições: 1 - Avançar, 2 - recuar, 3 - Status, 4 - desligar.
#3. Peça ao usuário para escolher um comando.
#4. Com vase na escolha, execute a ação correspondente:
    #Avançar: Adicione um valor a posição do robô
    #Recuar: Subtraia um valor a posição do robô
    #Status: Mostre a posição atual do robô.
    #Desligar: Encerre o programa


posicao = 0


while True:
    print("\nMenu de comandos para o robô:")
    print("1 - Avançar")
    print("2 - Recuar")
    print("3 - Status")
    print("4 - Desligar")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        valor = input("Quanto deseja avançar? ")
        if valor.isdigit():
            posicao += int(valor)
            print("O robô avançou", valor, "unidades.")
        else:
            print("Digite apenas números!")
    elif escolha == '2':
        valor = input("Quanto deseja recuar? ")
        if valor.isdigit():
            posicao -= int(valor)
            print("O robô recuou", valor, "unidades.")
        else:
            print("Digite apenas números!")
    elif escolha == '3':
        print("Posição atual do robô:", posicao)
    elif escolha == '4':
        print("Desligando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
