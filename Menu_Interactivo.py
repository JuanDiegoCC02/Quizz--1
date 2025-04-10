Lista = ["Jose", "Diego", "Pedro", "Luis"]

def Menu_Interactivo ():
    while True:
        print("Bienvenida")
        print("Lista_Nombres")
        print("Salir")
        Select = input ("Seleccione una opcion")
        if Select == "Bienvenida":
            print("Bienvenido a este Menu Interactivo")

        elif Select == "Lista_Nombres":
            print("Lista de Nombres:", Lista)

        elif Select == "Salir":
            print("Gracias por visitarnos")
            break
        else:
            print("Opcion invalida")
            


Menu_Interactivo()
