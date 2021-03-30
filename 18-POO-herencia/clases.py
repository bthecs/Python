#Herencia: Es la posibilidad de compartir atributos y metodos
# entre clases. Y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellidos

    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setAltura(self,altura):
        self.altura = altura

    def setEdad(self,edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "ZZZZZZZZZZZZZ"

class Informatico(Persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguaje(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "Ordenador reparado"

    
class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "estoy auditando una red"