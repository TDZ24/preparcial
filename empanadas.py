option = 1

vitrina = []

while option != 0:
    print("******Empanadas el Canibal**********")
    print("****1. Ingrese una empanada:********")
    print("*2. Muestre todas las empanadas: ***")
    print("*3. buscar las empanadas por id: ***")
    print("*4. Editar las empanadas por id: ***")
    print("*5. Eliminar las empanadas por id: *")
    print("********Presiona 0 para salir ******")

    option = int(input("Escoja una opcion: "))
    
    if(option == 1):
        empanada = {}
        empanada ["id"] = int(input("Digite un id para la empanada: "))
        empanada ["nombre"] = input("Digite un el nombre para la empanada: ")
        empanada ["precio"] = float(input("Digite el precio para la empanada: "))
        empanada ["popularidad"] = int(input("Digite la popularidad para la empanada: "))
        empanada ["fv"] = input("Digite la fecha de vencimiento de la empanada: ")
        vitrina.append(empanada)
        print("Empanada registrada correctamente...")

    elif(option == 2):
        for empanada in vitrina:
            print(empanada)

    elif(option == 3):
        empanaBuscar = int(input("Ingrese el id a buscar: "))
        for empanada in vitrina:
            if(empanada["id"]!=empanaBuscar):
                print("Empanada inexistente")
            else:
                print(f"Empanada encontada con exito{empanada}")
                
    elif(option == 4):
        empanaBuscar = int(input("Ingrese el id a buscar: "))
        for empanada in vitrina:
            if(empanada["id"]!=empanaBuscar):
                print("Empanada inexistente")
            else:
                print(f"El precio actual de la empanada es:{empanada['precio']}")
                precioNuevo=float(input("Digita el nuevo precio: "))
                empanada["precio"]=precioNuevo
                
    elif(option == 5):
        pass
    elif(option == 0):
        pass
    else:
        print("Opcion invalida")