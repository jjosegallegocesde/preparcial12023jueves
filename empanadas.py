opcion=100
empanadas=[]
print("***EMPANADAS EL MACHETICO***")
print ("1:Registrar empanada ")
print ("2: Mostrar empanada ")
print ("3:Buscar empanada ")
print ("4:Editar empanada ")
print ("5:Eliminar empanada ")
print ("0: Salir ")

contador=0
while opcion !=0:
    opcion= int(input("Ingresa la opcion deseada: "))
    if opcion == 1:
        #Agregando una empanada al arreglo de empanadas
        empanada={}
        empanada["id"]=int(input("Digita el codigo de la empanada: "))
        empanada["nombre"]=input("Digita el nombre de la empanada: ")
        empanada["precio"]=float(input("Digita el precio de la empanada: "))
        empanada["fechaFabricacion"]=input("Fecha de fabricacion")
        empanada["popularidad"]=int(input("Digite la popularidad: "))
        empanadas.append(empanada)

    elif opcion == 2:
        print(empanadas)
    elif opcion == 3:
        bandera=True
        empanadaABuscar=int(input("Digita el codigo de la empanada a buscar: "))
        for empanadaSeleccionada in empanadas:
            if empanadaSeleccionada["id"] == empanadaABuscar:
                print(empanada)
            else:
                print("No se encontro la empanada")
        
    elif opcion == 4:
        empanadaABuscar=int(input("Digita el codigo de la empanada a buscar: "))
        for empanadaSeleccionada in empanadas:
            if empanadaSeleccionada["id"] == empanadaABuscar:
                empanadaSeleccionada["precio"]=float(input("Digite el nuevo precio: "))
            else:
                print("No se encontro la empanada")
    elif opcion == 5:
        pass
    elif opcion == 0:
        print("Gracias")
    else:
        print ("*** Digita opcion valida ***")
    