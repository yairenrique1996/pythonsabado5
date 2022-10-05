print("***MENU***")
print("1. Agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. SALIR")
opcion=100
#DATOS EMPANADA
#Sabor
#Ingredientes (x3)
#Precio Fabircación
#Precio venta


empanadas=[]

while(opcion!=3):
    empanada={}
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
        empanada['sabor']=input("digite su sabor: ")
        empanada['ingredientes']=[]
        for i in range(3):
            
            empanada['ingredientes'].append(input("Digita el nombre del ingrediente: "))
        
        empanada['precioFabricacion']=input("digite precio de fabricacion: ")
        empanada['precioVenta']=input("digite precio de venta: ")
        empanadas.append(empanada)
        print("agregando empanadas")
    elif(opcion==2):
        
        print(empanadas)
        print("Mostrando empanadas")
    else:
        print("digite una opcion valida")
else:
    print("fin")