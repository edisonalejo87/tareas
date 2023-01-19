# numero = int(input("Ingrese un número: "))
# esprimo = True
# if numero // numero == 1 and numero // 1 == numero and numero%2 != 0 or numero==2:
# 	print("El numero ingresado es primo")
# else:
#    	print("El número ingresado no es primo")
	

numero = int(input("Ingrese un número: "))
primo=True
for n in range(2,numero):
	if numero% n ==0:
		print("El número ingresado no es primo")
		primo=False
		break
if primo:
	print("El numero ingresado es primo")