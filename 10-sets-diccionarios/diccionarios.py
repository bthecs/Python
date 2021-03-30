"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor
Es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}
print(persona["apellidos"])

# Lista con diccionario

contactos = [
    {
        "nombre": "Antonio",
        "email": "Antonio@antonio.com"
    },
    {
        "nombre": "Jorge",
        "email": "jorge@jorge.com"
    },
    {
        "nombre":"Lautaro",
        "email": "Lautaro@gmail.com"
    }
]
contactos[0]["nombre"] = "Antoñito"
print(contactos[0]["nombre"])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    
    