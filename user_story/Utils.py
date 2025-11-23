cantidad_total = 0
precio_total = 0.0
def MenuHU3():
    print("___________________________________")
    print("_______________MENU________________")
    print("1: Agregar")
    print("2: Mostrar")
    print("3: Buscar")
    print("4: Actualizar")
    print("5: Eliminar")
    print("6: Estadísticas")
    print("7: Guardar CSV")
    print("8: Cargar CSV")
    print("9: Salir")
    print("___________________________________")
    print("")
def Inventario_interactivo(inventario_globalHU3):
    for i,producto in enumerate(inventario_globalHU3):
        print(f"Item: {i+1}   | Nombre: '{producto['name_product']}' | Cantidad: {producto['quantity']} | Precio: {producto['price']:.2f} |")
            

def agregar_productoHU3():
    global cantidad_total,precio_total
    respuesta=1
    productos=[]
    count_p=1
    while respuesta!=0:
        print(f"Producto {count_p}:")
        count_p+=1
        nombre_producto=input("Ingresa el nombre del producto: ")
#Agregamos un ciclo while para pedir al usuario multiples veces la información correcta, en caso de no hacerlo.
        while True:
            #Validamos que las emtrdas sean numéricas
            try:
                cantidad_del_producto = int(input("Ingresa la cantidad: "))
                #Validamos que cantidad sea positivo
                if cantidad_del_producto>=0:
                    cantidad_total +=cantidad_del_producto
                    break
                else:
                    print("** Ingresa un numero positivo **")
            except ValueError:
                print("Dato inválido, ingresa la cantidad nuevamente")
        while True:
            #Validamos que las entradas sean numéricas
            try:
                precio_del_producto = float(input("Ingresa el  precio: "))
                #Validamos que precio sea positivo
                if precio_del_producto>=0:
                    precio_total += (precio_del_producto*cantidad_del_producto)
                    break
                else:
                    print("**** Ingresa un numero positivo ****")
            except ValueError:
                print("Dato inválido, ingresa el precio nuevamente")
    #Se crea un nuevo producto
        producto={
            "name_product": nombre_producto,
            "quantity":cantidad_del_producto,
            "price":precio_del_producto
        }
    #Se agrega el nuevo producto a la lista
        productos.append(producto)
        respuesta =input("Presione (S) para agregar o presione cualquier cosa para ir a Menú: ").lower()
        if respuesta =="s":
            continue
        else:
            respuesta =0
    return productos

#Creo una lista para mostrar los productos creados:

def mostrar_productoHU3(inventario_globalHU3):
    #product = input("Ingrese ")
    if not inventario_globalHU3:
        print("No hay productos en el inventario!")
    else:
        Inventario_interactivo(inventario_globalHU3)
        print("")
#Esta función se encarga de buscar, en este caso, un producto, en la lista de productos
#  
def buscar_productoHU3(inventario_globalHU3):
    if not inventario_globalHU3:
        print("El inventario está vacío!")
    else:
        #Inventario_interactivo(inventario_globalHU3)
        buscar = input("Que producto quieres buscar: ")
        print("")
        for producto in inventario_globalHU3:
            if buscar ==producto["name_product"]:
                print(f"| Producto: '{buscar}' | Estado: Encontrado | Unidades: {producto["quantity"]} | Precio: {producto['price']} |")
                return
        print("")
        print(f"| Producto: '{buscar}' | Estado: No encontrado |")

#Esta funcion se encarga de actualizar un producto del inventario existente
def actualizar_productoHU3(inventario_globalHU3):
    global cantidad_total,precio_total
    if not inventario_globalHU3:
        print("No hay productos en el inventario!")
    else:
        Inventario_interactivo(inventario_globalHU3)
        print("")
        #Con el while verificamos la validéz de lo que el usuario ingrese
        while True:
            try:
                item_seleccionado = int(input("Ingresa el item a actualizar: "))
                if item_seleccionado>0 and item_seleccionado<=len(inventario_globalHU3):
                    break
                else:print("** Item fuera de rango **")
            except:
                print("** Entradas inválidas **")
        producto_verificado=inventario_globalHU3[item_seleccionado-1]
        #Con el while verificamos la validéz de lo que el usuario ingrese
        precio_viejo   = producto_verificado['price']
        while True:
            try:
                nuevo_precio=int(input(f"Igresa el nuevo precio de '{producto_verificado['name_product']}' : "))
                #Con el if verificamos que los datos no sean negativos
                if nuevo_precio >=0:
                    break
                else:
                    print("** No se aceptan valores negativos **")
            except:print("** Entradas inválidas **")

        cantidad_vieja = producto_verificado['quantity']
        while True:
            try:
                nueva_cantidad=int(input(f"Igresa la nueva cantidad de '{producto_verificado['name_product']}' : "))
                #Con el if verificamos que los datos no sean negativos
                if nueva_cantidad >=0:
                    break
                else:
                    print("** No se aceptan valores negativos **")
            except:print("** Entradas inválidas **")
        cantidad_total -= cantidad_vieja
        precio_total   -= cantidad_vieja * precio_viejo
        producto_verificado['price']    = nuevo_precio
        producto_verificado['quantity'] = nueva_cantidad
        #Actualizamos el inventario
        cantidad_total += nueva_cantidad
        precio_total   += (nueva_cantidad * nuevo_precio)

 


#Con esta función eliminamos completamente un producto de nuestro inventario de productos

def eliminar_productoHU3(inventario_globalHU3):
    global precio_total,cantidad_total
    if not inventario_globalHU3:
        print("** Inventario vacío **")
    else:
        Inventario_interactivo(inventario_globalHU3)
        print("")
        #Verificamos que las entradas del usuario sean válidas
        while True:
            try:
                item_seleccionado = int(input("Ingresa el item a eliminar: "))
                print("")
                #Con  
                if item_seleccionado>0 and item_seleccionado<=len(inventario_globalHU3):
                    break
                else:print("** Item fuera de rango **")
            except:
                print("** Entradas inválidas **")            
    item_verificado=inventario_globalHU3[item_seleccionado-1]
    #Si el usuario elimina un producto, actualizamos las estadiscticas totales del inventario
    cantidad_total -= item_verificado['quantity']
    precio_total   -= item_verificado['quantity'] * item_verificado['price']

    inventario_globalHU3.pop(item_seleccionado-1)
    print(f"'{item_verificado['name_product']}' : Eliminado")
    

def estadisticas():
    global cantidad_total,precio_total
    print(f"La cantidad total del invetario es de: {cantidad_total} productos")
    print(f"El precio total es de: ${precio_total}")
    

















def validacion_item():
    print("")
def MenuHU2():
    print("_______________________")
    print("        MENU           ")
    print("_______________________")
    print("1: Agrear producto     ")
    print("2: Mostrar producto    ")
    print("3: Calcular estadística")
    print("4: Salir               ")
    print("_______________________")
    print("")
