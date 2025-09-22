class Contando:
    def __init__(self,numero):
        self.lista_de_numeros=[1,5,2,8,5,3,5]
        self.numero=numero
        self.contador=self.lista_de_numeros.count(self.numero)
        print('O número que você digitou não foi encontrado') if self.contador==0 else print(f'o número {numero} foi encontrado {self.contador} vezes')
a=Contando(int(input('Digite o número que deseja procurar:')))
