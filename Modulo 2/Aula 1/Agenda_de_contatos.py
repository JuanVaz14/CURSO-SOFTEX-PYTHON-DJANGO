#Agenda de Contatos: Crie um sistema simples de agenda que use um dicionário. Use um loop while para mostrar um menu com opções de "adicionar contato", "buscar contato" e "sair".

agenda = {}

while True:
    opcao = input("Digite: 1(Adicionar contato). 2(Buscar, 3(Sair) ")

    # Adicionar contato
    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso!")

    # Buscar contato
    elif opcao == "2":
        nome = input("Nome do contato para buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    # Sair
    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")