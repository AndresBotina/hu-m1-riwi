# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
##import os
##print("Current working directory:", os.getcwd())
from Utils import MenuHU2
#Creo una función Menú
MenuHU2() 
#Solicitamos al usuario lo que desea hacer
menu =0
print("")
#Creo una nueva lista
inventario = []
#contador
cantidad_total = 0
precio_total = 0
costo_total = 0
precio_final = 0

#Creamos un while para iterar sobre la desicion del desición del usuario.
while menu!=4:
    try:
        menu = int(input("¿Que quieres hacer?: "))
        print("")
        print("")

        #Uso un condicional para preguntar al ususario que quiere hacer.
        if menu ==1:
            
            print("----AGREGANDO PRODUCTOS----")


            product_name = input("Ingresa el nombre del producto: ")
            product_amount = int(input("Ingrese la cantidad del producto: "))
        

            product_price = int(input("Ingrese el precio del producto: "))
            


            product = {
                "product_name" :product_name,
                "product_amount": product_amount,
                "product_price" :product_price
            } 
            
            precio_total = product_amount*product["product_price"]
            cantidad_total +=product_amount
            precio_final+=precio_total
            #Almacenamos los productos en una lista, (inventario).

            inventario.append(product)
            print("")

        elif menu==2:
            #Muestro un mensaje si la lista está vacía, sino, muestro la lista de productos creados
            if not inventario:
                print("----La lista está vacía!----")
            else:
                print("LISTA DE PRODUCTOS:")
                for producto in inventario:
                    print(f"| Name: {product_name} | Amount: {product_amount} | Price: {product_price } |")
            print("")
        elif menu==3:
            #Muestro la informacion de los productos creados.
            print("INFORMACION DE LOS PRODUCTOS: ")
            print("")
            print(f"La cantidad de productos registrados es: {cantidad_total}")
            print(f"El precio total es: {precio_final}")
        elif menu==4:
            #Si el usuario preciona (4), el programa se finaliza.
            print("¡Has salido!")
            break
        else:
            #Si algo diferente a 1,2,3,4, muestra un mensaje de error.
            print("**** Has elegido una opción invalida ****")
            print("")
        MenuHU2()
            
        print("") 

    #Capturamos el error con except y volvemos a pedir los datos
    except ValueError:
        print("")
        print("**** Entradas inválidas **** ")
        print("")
        MenuHU2()