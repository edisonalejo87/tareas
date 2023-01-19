num1 = int(input("Ingrese el año: "))
if not num1 % 4:
	if not num1 % 100:     # divisible entre 4 y 100
		if not num1 % 400:  # divisible entre 4, 100 y 400
			print("El año: ",num1,", si es bisiesto")
		else:              # divisible entre 4 y 100 y no entre 400
			print("El año: ",num1,", no es bisiesto")
	else:                 # divisible  entre 4 y no entre 100
		print("El año: ",num1,", si es bisiesto")
else:                    # no divisible entre 4
	print("El año: ",num1,", no es bisiesto")