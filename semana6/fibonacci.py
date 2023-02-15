def fibonacci(n):
    if n < 0:
        print("El numero ingreado es incorrecto")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
numero=int(input("Ingrese un numero: "))
print("La suma total del numero ingresado es:  ",fibonacci(numero))

