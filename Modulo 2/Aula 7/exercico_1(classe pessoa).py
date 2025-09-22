# Objetivo
#Crie uma classe com validações simples no setters para tipo o valor
#Crie uma classe Pessoa com os atributos protegidos _nome e _idade.
#Crie uma @property para nome.
#Crie um @nome.setter que valide se o valor é uma string e não está vazio.
#Crie uma @property para a idade.
#Crie uma @idade.setter que valide se a idade é um número inteiro positivo.
#No _int_, use os setters para atribuir os valores iniciais (ex: self.nome = nome).
#Instancie um projeito de Pessoas com dados válidos e depois tentar alterar nome para um vazio e idade para um valor negativo para testar as validações,

""""""

class Pessoa:
    def _init_(self, nome,idade):
        self.nome = nome
        self.idade = idade

@property
def nome(self):
        return sel._nome

@none.setter
def nome(self, novo_nome: str):
    if isistance(novo_nome, str) and novo_nome:
          self.nome = novo_nome
    else:
        print("Erro! O novo nome deve ser uma string não vazia")
        