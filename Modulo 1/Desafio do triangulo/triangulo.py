#"""
#Desafio de Programação: Validação de Triângulo
#Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

#As Regras do Jogo
#1- Teste se a entrada de dados é um número.
#2- Se for um número teste se é positivo
#3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:
#"""
class Triangulo:
    def verificacao(self, lado_A,lado_B,lado_C):
       if not lado_A.isdigit() or not lado_B.isdigit() or not lado_C.isdigit():
           print('Você não digitou o número de maneira correta.Tente novamente.')
       else:
            self.lado_a=abs(int(lado_A))
            self.lado_b=abs(int(lado_B))
            self.lado_c=abs(int(lado_C))
            if self.lado_a<=0 or  self.lado_b <=0 or  self.lado_c<=0:
                print('Todos os números 0 ou menores que ele não são permitidos.')
            else:
                print('Os números são capazes de ser tornar um triângulo') if  self.lado_a<self.lado_b + self.lado_c and self.lado_b< self.lado_a + self.lado_c and self.lado_c< self.lado_a + self.lado_b and  self.lado_a>self.lado_b - self.lado_c and self.lado_b> self.lado_a - self.lado_c and self.lado_c> self.lado_a - self.lado_b else print('Os números não são capazes de ser tornar um triângulo')

n1=(input('Digite o primeiro número:')) 
n2=(input('Digite o segundo número:'))  
n3=(input('Digite o terceiro número:'))  

numeros=Triangulo()
numeros.verificacao(n1,n2,n3)