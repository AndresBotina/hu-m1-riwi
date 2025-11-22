#HISTORIA DE USUARIO 1
print("        BIENVENIDO ")
#Solicitamos al usuario el nombre del producto 
product =input("Nombre producto: ")
#Agregamos un ciclo while para pedir al usuario multiples veces la información correcta, en caso de no hacerlo.

while True:
    try:
        precio = int(input("Ingresa el precio: "))
        if precio>=0:
            break
        else:
            print("Ingresa un numero positivo ")
    except ValueError:
        print("Dato inválido, ingresa el precio nuevamente")
while True:
    try:
        cantidad = int(input("Ingresa el la cantidad: "))
        if cantidad>=0:
            break
        else:
            print("Ingresa un numero positivo ")
    except ValueError:
        print("Dato inválido, ingresa la cantidad nuevamente")

costo_total = precio*cantidad
print(f"Producto:{product} | Precio:{precio} | Cantidad:{cantidad} | Total:{costo_total}")























#El programa Solicita al usuario informacion a cerca de un producto y alfinal se calcula el precio o costo total de los productos propuestos