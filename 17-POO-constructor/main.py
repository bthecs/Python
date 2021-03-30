from coche import Coche

carro = Coche("Naranja","Gallardo","Ferrari",400,1000,2)
carro1 = Coche("Azul","Clio","Renault",400,1000,2)
carro2 = Coche("Blanco","Argo","Fiat",400,1000,2)
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())

#Detectar tipado
carro1 = "Perro"
if type(carro1) == Coche:
    print("Es un objeto correcto!!!")
else:
    print("No es un objeto coche")

#Visibilidad de atributos
print(carro.soy_publico)
print(carro.__privado)