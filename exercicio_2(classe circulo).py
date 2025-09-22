#Objetivo: Usar um setter para validar dados numéricos e ter métodos que usam a property.
"""● Requisitos:
1. Crie uma classe Circulo com um atributo protegido _raio.
2. Crie uma @property para raio.
3. Crie um @raio.setter que valide se o valor do raio é um número positivo.
4. Crie um método calcular"""

from math import pi
#forma alternativa = import math -> use math.py

class circulo:
    def _init_(self, raio:int):
        self.raio = raio

@property
def raio(self) -> int:
    return self._raio

@raio.setter
def raio(self, novo_raio:int) -> None:
    if novo_raio > 0 and isinstance(novo_raio, int):
        self._raio = novo_raio
    else:
        print("Erro! O novo raio deve ser positivo e inteiro. ")

    def calcular_area(self) -> float:
        area = pi * self.raio ** 2
        print(area)
    
roda = circulo(2)
print(roda.raio)
roda.raio = 3
roda.calcular_area()