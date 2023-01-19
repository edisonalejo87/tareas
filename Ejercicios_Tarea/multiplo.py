num1 = int(input("Ingrese el primer Número: "))
num2 = int(input("Ingrese el segundo Número: "))
if num1 % num2 == 0:
    print("El número: " ,num2, ", es múltiplo de",num1)
else:
    print("El número: " ,num2, ", no es múltiplo de: ",num1)