#pc precio computador
#cp contador producto
cp = 1  # contador del producto
precio_total = 0  # Acumulador del total de productos
iva=float(1.12)
descuento =float(0.2)
opcion= input("Ingrese que articulo va ingresar, las opciones son: Computadora , Celular , mostrar ").lower()
print(opcion)
if opcion == "computadora":
    cantidad_computadora= int(input("Cuantas Computadoras desea: "))
    while cp <= cantidad_computadora:
        mensaje = "Ingresa el valor del computador número {}: ".format(cp)
        pc = input(mensaje)
        precio = float(pc)
        precio_total = precio_total + precio
        cp = cp + 1
    print("El valor total a pagar por las computadoras es", precio_total*iva)
elif opcion == "celular":
    cantidad_celular= int(input("Cuantos celulares desea: "))
    while cp <= cantidad_celular:
        mensaje = "Ingresa el valor del celular número {}: ".format(cp)
        precio_celular = input(mensaje)
        precio = float(precio_celular)
        precio_total = precio_total + precio
        cp = cp + 1
    precio_total = precio_total - (precio_total * descuento)
    print("El valor total a pagar por los celulares es", precio_total*iva)
elif opcion == "mostrar":
        valor_computador = float(input("Ingresa el valor del computador: "))
        valor_celular = float(input("Ingresa el valor del celular: "))
        precio_total = valor_computador + valor_celular
        print("El valor del computador es: ", valor_computador)
        print("El valor del celular es: ", valor_celular)
        print("El valor total a pagar por los dos productos es", precio_total*iva)
else:
     print("Opción no válida")


