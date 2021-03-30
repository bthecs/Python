"""
Proyecto Python y Mysql:
-Abrir asistente
-Login o registros
-Si elegimo login, identifica al usuario y nos preguntara
-Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones



print("""
Acciones disponibles:
    -registro
    -login
""")

hazEl = acciones.Acciones()
accion = input("Que deseas hacer?: ")

if accion == 'registro':
    hazEl.registro()
    


elif accion == 'login':
    hazEl.login()
    


