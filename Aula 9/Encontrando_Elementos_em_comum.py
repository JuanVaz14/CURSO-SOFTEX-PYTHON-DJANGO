class Igual:
    def __init__(self):
        self.lista1=['vermelho','azul','verde','amarelo','verde']
        self.lista2=['verde','roxo','azul','preto','verde']
        self.lista_nova=[]
        self.contar=0
    def encontrar(self):
        for i in self.lista1:
            if i in self.lista2:
                    self.lista_nova.append(i)
            self.contar+=1
        print(self.lista_nova)
a=Igual()
a.encontrar()
