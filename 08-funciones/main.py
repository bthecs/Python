"""
Funciones:
Conjunto de instrucciones agrupadas bajo un nombre concreto que puede
reutilizarse invocando a la funcion tantas veces como sea necesario

def nombredemifun(parametros):
    #Bloque / conjunto de instrucciones

nombredemifun(parametro)

"""
"""

#ejemplo 1
print("###########Ejemplo1########")
#Definir funcion
def muestra_nombres():
    print("Victor")
    print("Lautaro")
    print("Franco")
    print("Jose")

#invocar funcion
muestra_nombres()

print("###########Ejemplo2########")



def mostrartunom(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Ya eres mayor de edad")

nombre = str(input("ingrese su nombre: "))
edad = int(input("ingrese edad: "))
mostrartunom(nombre, edad)


print("###########Ejemplo3########")

def multi(numero):
    print(f"La tabla del: {numero}")
    for i in range(0,11):
        print(f"{i}x{numero} = {i*numero}")

numero = int(input("Ingrese el numero: "))
multi(numero)


print("###########Ejemplo4########")

#parametros opcionales

def getEmpleado(nombre,dni = False):
    print("EMPLEADO")
    print(f"nombre: {nombre}")
    print(f"DNI: {dni}")

getEmpleado("Lautaro")

print("###########Ejemplo5########")

#Parametros opcionales y return o devolver datos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

saludame("Lautaro Gimenez")
print(saludame("Lautaro Gimenez"))

print("###########Ejemplo6########")

def calculadora(num1, num2, basicas = False):

    sum = num1 + num2
    rest = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    cadena = ""

    if basicas !=False:
        cadena += "Suma: " + str(sum)
        cadena += "\n"
        cadena += "Resta: " + str(rest)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(div)

    return cadena

#print(calculadora(5,25))
print(calculadora(5,25,True))


print("###########Ejemplo7########")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Lautaro","Gimenez"))


#funciones lambda
print("###########Ejemplo8########")

año = lambda year: f"El año es {year}"

print(año(2021))

"""