class personaje:
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
    def atributos(self):
        print(f"nombre: {self.nombre}")
        print("fuerza: ", self.fuerza)
        print("vida: ", self.vida)
        print("inteligencia: ", self.inteligencia)
        print("defensa", self.defensa)
    def esta_vivo(self):
        return self.vida > 0
class guerrero(personaje):
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    
    
    
    
mi_personaje = guerrero("lesu", 10 ,1 ,5, 100, 5)
mi_personaje.atributos()

        