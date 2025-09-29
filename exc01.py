""" 1. Montando um Carro (Fácil)
● Classes: Motor e Carro.
● Classe Motor:
○ Método: __init__ (sem atributos).
○ Método: ligar() que imprime "O motor ligou.".
● Classe Carro:
○ Atributo (Composição): motor, que deve ser uma instância de Motor.
○ Método: __init__ que inicializa o atributo motor.
○ Método: ligar_carro() que chama o método ligar() do seu objeto motor."""

class Motor:
    # def __init__(self):
    #    pass

    def ligar(self):
        print("O motor ligando...")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.ligar()

carro = Carro()
carro.ligar_carro()