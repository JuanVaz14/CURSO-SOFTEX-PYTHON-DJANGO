"""
Comercio Padaria
x 1-O programa tem que rodar em loop infinito até ser parado
x 2-cliente pedir um tipo de pão (frances, doce, forma, australiano)
x 3-cada pao terá uma quantidade
x 4-valor do pao
x 5-pedir forma de pagameno (dinheiro, cartao)
x 6-forma de entrega
x 7-dados do cliente (se for entregar)
x 8-valor do frete por bairro
x 9-nome do atendente
x 10-codigo da entrega
"""

def dados() -> dict:
    """Carregar e retornar os dados de produtos, frete e funcionários"""
    return {
        "Atendente": "Maria",
        "paes": {
            "Frances": {"nome": "Pão Francês", "valor": 5.00, "quantidade": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "quantidade": 18},
        },
        "Bairros": {
            "Barroco": {"nome": "Barroco", "frete": 5.00},
            "São José": {"nome": "São José", "frete": 5.00}
        },
        "codigo_venda_base": 95875,
    }

def obter_dados_do_cliente() -> dict:
    """Solicitar e retornar dados do cliente"""
    nome = input("Informe seu nome: ")
    return {"nome": nome}

def solicitar_forma_de_pagamento() -> str:
    """Solicitar e retornar a forma de pagamento escolhida"""
    
    pagamento = input("Escolha a forma de pagamento (1-Dinheiro, 2-Cartão): ")
    if pagamento == "1":
        return "Dinheiro"
    elif pagamento == "2":
        return "Cartão"
    else:
        print("Forma de pagamento inválida")
        return ""

def gerar_codigo_venda(codigo_base: int) -> int:
    """Gerar e retornar o código de venda"""
    return codigo_base + 1

def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float]:
    """Calcula o valor do frete com base no bairro de entrega"""
    print("Bairros para entrega:")
    for bairro in bairros_disponiveis.values():
        print(f"- {bairro['nome']}")
    
    bairro_entrega_nome = input("Qual o bairro de entrega? ").lower()
    
    bairro_encontrado = ""
    
    for chave, bairro in bairros_disponiveis.items():
        if bairro["nome"].lower() == bairro_entrega_nome:
            bairro_encontrado = chave
            break
    
    if not bairro_encontrado:
        print("Bairro fora da área de entrega")
        return "", 0.0
    
    else:
        frete = bairros_disponiveis[bairro_encontrado]["frete"]
        return bairro_entrega_nome, frete
    
def nome_produto(estoque: dict) -> None:
    """Permite ao atendente cadastrar um novo produto"""
    nome_produto = input("Digite o nome do novo produto (identificador): ").lower().strip()

    if nome_produto in estoque:
        print("Erro! Produto já cadastrado com este identificador!")
        return

    nome_completo = input("Digite o nome completo do produto: ")
    try:
        valor = float(input("Digite o valor do novo produto: "))
        quantidade = int(input("Digite a quantidade inicial do produto: "))
    except ValueError:
        print("Erro! Valor ou quantidade inválidos.")
        return

    if nome_produto and nome_completo and valor > 0 and quantidade > 0:
        estoque[nome_produto] = {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
        print(f"Produto {nome_completo} cadastrado com sucesso!")
    else:
        print("Erro! Dados inválidos.")

def atualizar_produto(estoque: dict) -> None:
    """Permite que o atendente atualize um produto existente"""
    nome_produto = input("Digite o nome do produto para atualizar (identificador): ").lower()

    if nome_produto not in estoque:
        print("Produto não cadastrado")
        return

    print(f"Produto '{estoque[nome_produto]}' selecionado.")
    escolha = input("O que deseja atualizar?\n1 - Valor\n2 - Quantidade\nEscolha: ")

    try:
        if escolha == "1":
            novo_valor = float(input("Digite o novo valor do produto: "))
            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R$ {novo_valor:.2f}")
            else:
                print("Valor inválido.")
        elif escolha == "2":
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            if nova_quantidade >= 0:
                estoque[nome_produto]["quantidade"] = nova_quantidade
                print(f"Quantidade atual de {estoque[nome_produto]['nome']}: {estoque[nome_produto]['quantidade']}")
            else:
                print("Quantidade inválida.")
        else:
            print("Erro! Opção inválida.")
    except ValueError:
        print("Erro! Entrada de dados inválida. Digite apenas números.")