# num = int(input("Ingrese un Número: "))
# if num % 2 == 0:
#     print("El numero ingresado: ",num," Es par")
# else:
#     print("El numero ingresado: ",num," Es impar")


print ("Mayor de 3 Números")
a = int(input("Ingrese el Num1: \n"))
b = int(input("Ingrese el Num2: \n"))
c = int(input("Ingrese el Num3: \n"))
if (a > b):
    mayor = a
else:
    mayor = b

if (c > mayor):
    mayor = c

print ("El Mayor de los 3 números es:", mayor)