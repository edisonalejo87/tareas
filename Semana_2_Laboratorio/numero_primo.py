# numero = int(input("Ingrese un número: "))
# esprimo = True
# if numero // numero == 1 and numero // 1 == numero and numero%2 != 0 or numero==2:
# 	print("El numero ingresado es primo")
# else:
#    	print("El número ingresado no es primo")
numero = int(input("Ingrese un número para verificar si es primo o no: "))
numero_primo=True
for n in range(2,numero):
	if numero% n ==0:
		print("El número ingresado: ",numero, " no es primo")
		numero_primo=False
		break
if numero_primo:
	print("El número ingresado: ",numero, " es primo")