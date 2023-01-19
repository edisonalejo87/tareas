num1 = int(input("Ingrese el año: "))
if not num1 % 4:
	if not num1 % 100:     
		if not num1 % 400:  
			print("El año: ",num1,", si es bisiesto")
		else:              
			print("El año: ",num1,", no es bisiesto")
	else:                 
		print("El año: ",num1,", si es bisiesto")
else:                    
	print("El año: ",num1,", no es bisiesto")