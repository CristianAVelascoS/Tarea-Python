import unittest

class Motor(unittest.TestCase):
    def __init__(self, volumen_litros):
        self.volumen_litros = volumen_litros
    
    def __str__(self):
        return f"Motor: {self.volumen_litros} litros"


class Chasis (unittest.TestCase):
    class TipoChasis:
        Independiente = "Independiente"
        Monocasco = "Monocasco"
    
    def __init__(self, tipo):
        self.tipo = tipo
    
    def __str__(self):
        return f"Chasis: {self.tipo}"


class Carroceria (unittest.TestCase):
    class TipoCarroceria:
        Independiente = "Independiente"
        Autoportante = "Autoportante"
        Tubular = "Tubular"
    
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color
    
    def __str__(self):
        return f"Carrocería: {self.tipo}, Color: {self.color}"


class Llanta (unittest.TestCase):
    def __init__(self, marca, diametro_rin, altura, anchura):
        self.marca = marca
        self.diametro_rin = diametro_rin
        self.altura = altura
        self.anchura = anchura
    
    def __str__(self):
        return f"Llanta: Marca: {self.marca}, Rin: {self.diametro_rin}\", Altura: {self.altura}, Anchura: {self.anchura}"


class Asiento (unittest.TestCase):
    def __init__(self, material, tiene_funda):
        self.material = material
        self.tiene_funda = tiene_funda
    
    def __str__(self):
        funda = "con funda" if self.tiene_funda else "sin funda"
        return f"Asiento: Material: {self.material}, Estado: {funda}"


class Carro (unittest.TestCase):
    def __init__(self, motor, chasis, carroceria, llantas):
        self.motor = motor
        self.chasis = chasis
        self.carroceria = carroceria
        self.llantas = llantas
    
    def __str__(self):
        return f"{self.motor}\n{self.chasis}\n{self.carroceria}\n{', '.join(str(llanta) for llanta in self.llantas)}"


def main():
    # Crear componentes del carro
    motor = Motor(2)
    chasis = Chasis(Chasis.TipoChasis.Monocasco)
    carroceria = Carroceria(Carroceria.TipoCarroceria.Tubular, "rojo")
    llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]
    
    # Crear carro
    carro = Carro(motor, chasis, carroceria, llantas)
    
    # Mostrar detalles del carro
    print(carro)


if __name__ == "__main__":
    main()