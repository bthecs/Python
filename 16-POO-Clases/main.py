#Programacion orientada a objetos

#Definir una clase (molde para crear mas objetos de ese tipo
# (coche) con caracteristicas similares)

class Coche:

    #Atributos o propiedades
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos = 500
    plazas = 2

    #Metodos, son acciones que hace el objeto (coche)(funciones)

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color
        
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad


# Fin definicion clase

# Crear objetos / instanciar la clase
print("-----------------Coche 1----------------------")
coche = Coche()

coche.setColor("Verde")
coche.setModelo("Enzo")


print(coche.marca,coche.getModelo(), coche.getColor())
print("Velocidad actual: ",coche.getVelocidad())
        
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
coche.frenar()
print("Velocidad actual: ",coche.getVelocidad())

print("-----------------Coche 2----------------------")

#Crear mas objetos
coche2 = Coche()
coche2.setColor("Naranja")
coche2.setModelo("Murcielago")
print(coche.marca,coche2.getModelo(), coche2.getColor())