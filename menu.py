usuarios = []
indice = 0
while True:
    print("*"*50)
    print("******** Bienvenido al SENA ******")  
    print("*"*50)  
    print("Operaciones disponibles!")
    print("1. Listar usuarios")
    print("2. Agregar usuario")
    print("3. Quitar usuario")
    print("4. Cambiar usuario")
    print("5. Salir")
    print("*"*50)
    opcion = int(input("Que operacion deseas hacer hoy? "))
        
    match opcion:
        case 1:
            print("-"*50)
            print("LISTAR USUARIOS: ")
            print("-"*50)
            if len(usuarios) == 0:
                print("no hay usuarios ingresados!")
                continue
            for nom in usuarios:
                print(f"- {nom}")
            print("-"*50)
        case 2:
            print("-"*50)
            print("AGREGAR USUARIO: ")
            print("-"*50)
            nuevo = input("ingresa el nombre del nuevo usuario: ")
            valNew = nuevo.strip()
            usuarios.append(valNew.upper())
            print("Se ha ingresado el usuario correctamente!")
            print(f"Su posicion es {indice}")
            indice +=1
            print("-"*50)
        case 3:
            print("-"*50)
            print("QUITAR USUARIO: ")
            print("-"*50)
            try:
                quitar = input("ingresa el nombre del usuario: ")
                posicion = usuarios.index(quitar)
                usuarios.pop(posicion)
                print("Se ha eliminado el usuario correctamente!")
            except Exception as e:
                print("El usuario no existe!", e)            
            print("-"*50)
        case 4:
            print("-"*50)
            print("CAMBIAR USUARIO: ")
            print("-"*50)
            try:
                cambiar = input("ingresa el nombre del usuario a cambiar: ")
                cambiar = cambiar.strip() 
                posicion = usuarios.index(cambiar.upper())
                
                nuevo = input("ingresa el nombre del nuevo usuario : ")    
                nuevo = nuevo.strip() 
                usuarios[posicion] = nuevo.upper()
                print("Se ha cambiado el usuario correctamente!")
            except Exception as e:
                print("El usuario no existe!", e)            
            print("-"*50)
        case 5:
            print("Adios!")  
            break
        case _:
            print("No ha seleccionado una opcion valida!")  
            
    print("*"*100)