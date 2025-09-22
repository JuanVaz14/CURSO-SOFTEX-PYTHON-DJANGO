class Dados:
    def __init__(self):
        lista=[]
        while True:
            self.verificar=input('Digite o valor(-1 para parar):')
            if self.verificar=='-1':
                break
            else:
                if not self.verificar.isdigit() or self.verificar>100 or self.verificar<0:
                    print('Seu dado não é um núnero ou é maior que 100 ou menor que zero')
                else:
                    lista.append(self.verificar)
        soma=0
        for i in lista:
            soma+=i
        print(lista)
        print(soma)
                
a=Dados()
