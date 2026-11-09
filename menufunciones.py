usuarios = []
# Funciones
def menu():
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

def validarNombre(nombre):
    newName = nombre.strip()
    return newName.upper()
    
def ingresarUsuario(nombre):
    print("llegando", nombre)
    usuarios.append(nombre)
    print("Se ha ingresado el usuario correctamente!")
def metodo2():
    print("-"*50)
    print("AGREGAR USUARIO: ")
    print("-"*50)
    nuevo = input("ingresa el nombre del nuevo usuario: ")
    nuevo = validarNombre(nuevo)
    print("realiza validacion", nuevo)
    ingresarUsuario(nuevo)
                    
                    
# Programa  

while True:
    try:
        menu()
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
                metodo2()
                
                
    except Exception as e:
        input("Las opciones del menú solo son numéricas!")
    