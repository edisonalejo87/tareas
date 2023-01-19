num1 = int(input("Ingrese el primer Número: "))
num2 = int(input("Ingrese el segundo Número: "))
num3 = int(input("Ingrese el tercer Número: "))
if(num1 > num2 and num1 > num3):
 print("El número mayor ingresado es ", num1)
else:
 if(num2 > num1 and num2 > num3):
  print("El número mayor ingresado es ", num2)
 else:
  print("El número mayor ingresado es ", num3)
