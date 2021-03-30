import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Ingrese titulo de nota: ")
        descripcion = input("Ingrese descripcion de nota: ")

        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto nota guardada {nota.titulo}")

        else:
            print(f"No se a guardado la nota, Lo siento mucho :( {usuario[1]}")

    def mostrar(self,usuario):
        print(f"Okey {usuario[1]}!! Aqui estan tus notas: ")

        nota = modelo.Nota(usuario[0],"","")
        notas = nota.listar()

        for nootas in notas:
            print("_\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print(f"\nTitulo: {nootas[2]}")
            print(f"\nDescripcion: {nootas[3]}")
            print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def borrar(self, usuario):
        print(f"\n Okey {usuario[1]}!! Vamos a borrar notas")

        titulo = input("Ingrese titulo de la nota que desea borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado la nota {nota.titulo}")