import clases

persona = clases.Persona()
persona.setNombre("Lautaro")
persona.setApellidos("Gimenez Gil")
persona.setAltura(1.80)
persona.setEdad(23)

print(f"Nombre: {persona.getNombre()}, Apellidos: {persona.getApellido()}, Altura: {persona.getAltura()}, Edad: {persona.getEdad()}")
print(persona.hablar())

print("---------------------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Lautaro")
informatico.setApellidos("Gimenez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguaje())
print(informatico.caminar())

print("---------------------------------------------------")

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes, tecnico.getLenguaje())

