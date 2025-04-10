
dato ={
    "producto" : "Zapatillas Air Max",
    "talla" : 42,
    "color" : "Negro",
    "stock" : 20
}

def  Menu_Opcion ():

    while True:
        print("Editar")
        print("Eliminar")
        Opc = input ("Ingrese una Opción: ")
        if Opc == "Editar":
            keys_Usuario()
        elif  Opc == "Eliminar":
            elimnar_Producto()
        elif Opc == "Salir":
            print("GRACIAS")
            break
        else: 
            print("Opcion Invalida")


def keys_Usuario():
    print(dato)
    acceso_KeysEdit = input ("Clave para editar dato: ")
    dato_Producto= input("nuevo dato")
    dato[acceso_KeysEdit]=dato_Producto
    print(dato)


def elimnar_Producto():
    print(dato)
    aceso_KeysDelete = input ("Clave para eliminar dato: ")
    if aceso_KeysDelete in dato:
     valor_eliminado= dato.pop(aceso_KeysDelete)
     print(f"Se elimino la clave '{aceso_KeysDelete}' con el valor de '{valor_eliminado}'.")
     print(f"Dato Actualizado: {dato}")
    else:
        print(f"La clave de acceso no existe en '{dato}'.")
    


Menu_Opcion()
