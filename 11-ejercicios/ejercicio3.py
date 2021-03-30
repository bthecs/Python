"""
Programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minuscula y mostrarlo en mayuscula
"""

variable = ""

if not variable:
    print("La variable esta vacia :(")
    variable = str(input("Ingrese texto en minuscula: "))
    print(variable.upper())
else:
    print("variable contiene elementos")