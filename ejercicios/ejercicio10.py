"""
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""
import random

aprobados = 0
desaprobados = 0

for alumno in range(1,16):
    nota = random.randint(0,10)
    if nota >= 6:
        aprobados = aprobados + 1
        print(f"El alumno: {alumno} = {nota} / Aprobado ")
    else:
        desaprobados = desaprobados + 1
        print(f"El alumno: {alumno} = {nota} / Desaprobado ")

print(f"Cant de aprobados: {aprobados} / Cant de alumnos desaprobados: {desaprobados}")