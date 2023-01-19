num1 = int(input("Ingrese el primer Número: "))
num2 = int(input("Ingrese el segundo Número: "))
num3 = int(input("Ingrese el tercer Número: "))
if(num1 > num2 and num1 > num3 and num2 > num3):
    print("El orden de los números ingresados son 1  ",num1," - ",num2," - ",num3)
else:
    if(num2 > num1 and num2 > num3 and num1 > num3):  
        print("El orden de los números ingresados son 2  ",num2," - ",num1," - ",num3)
    else:
        if(num3 > num2 and num3 > num1 and num2 > num1):
            print("El orden de los números ingresados son 3  ",num3," - ",num2," - ",num1)
        else:
            print("El orden de los números ingresados son 4  ",num2," - ",num3," - ",num1)
