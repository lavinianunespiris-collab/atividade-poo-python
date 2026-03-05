class Bicicleta: 
    def __init__(self, corDaBicicleta, bicicletaSemRodinha, bicicletaComRodinha):

        self.corDaBicicleta = corDaBicicleta
        self.bicicletaSemRodinha = bicicletaSemRodinha
        self.bicicletaComRodinha = bicicletaComRodinha 

    def andar(self):
        print(f"A bicicleta {self.corDaBicicleta} está sendo pedalada")
    
    def tocarSino(self):
        print(f"A bicicleta {self.corDaBicicleta} está tocando o sininho para liberar passagem")

Bicicleta1 = Bicicleta("Azul", True, False)
Bicicleta2 = Bicicleta("Amarelo", False, True)
Bicicleta3 = Bicicleta("Rosa", False, True)

Bicicleta1.tocarSino()
Bicicleta2.andar()
Bicicleta3.tocarSino()
