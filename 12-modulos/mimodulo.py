
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

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