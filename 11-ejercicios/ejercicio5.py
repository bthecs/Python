"""
Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA            DEPORTES
GTA         ASSASINS            FIFA 21
COD         CRASH               PRO 21
PUBG        PRINCE OF PERSIA    MOTO GP 21

Mostrar esta informacion ordenada
"""

juegos = [
    {
        "CATEGORIA": "ACCION",
        "JUEGOS": ["GTA","COD","PUBG"]
    },
    {
        "CATEGORIA": "AVENTURA",
        "JUEGOS": ["ASSASINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "CATEGORIA": "DEPORTE",
        "JUEGOS": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]
for jue in juegos:
    print(f"----------{jue['CATEGORIA']}-----------")
    for i in jue['JUEGOS']:
        print(i)