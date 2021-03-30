

class Coche:

    #Atributos o propiedades
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos = 500
    plazas = 2

    soy_publico = "Hola soy un atributo publico"
    __privado = "Hola soy un atributo privado"

    def __init__(self,color,marca,modelo,velocidad,caballos,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos = caballos
        self.plazas = plazas

    #Metodos, son acciones que hace el objeto (coche)(funciones)

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color
        
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):

        info = "----------Informacion del coche-----------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info