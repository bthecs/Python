import usuarios.usuario as modelo
import notas.acciones  

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cual es tu apellidos?: ")
        email = input("Cual es tu email?: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto usuario registrado: {registro[1].nombre} te has registrado con el mail {registro[1].email}")

        else:
            print("\nNo te has registrado correctamente!!")
    
    def login(self):
        print("Vale!! Identificate en el sistema...")
        
        try:
            email = input("Cual es tu email?: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema: {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir)
        """)

        accion = input("Que deseas hacer?:")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            print(f"\nOk {usuario[1]}, hasta pronto!! :D")
            exit()

        return None


