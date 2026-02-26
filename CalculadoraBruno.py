#CALCULADORAbruno

import math

d = input("Escolha a operação desejada: \n1-Adição \n2-Subtração \n3-Multiplicação \n4-Divisão \n5-Potênciação \n6-Radiciação\n")
d = int(d)

if d !=4:
	a = input("Entre com o 1º valor: ")
	a = int(a)
else:
	a=0

if (d!=6) and (d!=4) :

	b = input("Entre com o 2º valor: ")
	b = int(b)
else:
	b=0


if d == 1:


	c = a + b
	print("A soma: ", a, "+", b, "=", c)

	input()

elif d == 2:


	c = a - b
	print("A subtração: ", a, "-", b, "=", c)

	input()

elif d == 3:

	
	c = a * b
	print("A multiplicação: ", a, "vezes ", b, "=", c)

	input()

elif d == 4:

	a = input("Entre com o 1º valor: ")
	a = float(a)

	b = input("Entre com o 2º valor: ")
	b = float(b)

	
	c = a / b
	print("A divisão: ", a, "dividido por ", b, "=", c)

	input()

elif d == 5:

	
	c = a ** b
	print("A potênciação: ", a, "elevado a ", b, "=", c)

	input()

elif d == 6:
	
	c = math.sqrt(a)

	print("A raiz de: ", a, "=", c)

	input()

else:
	print("Digitou um que ta errado ai viu parça")
	
	input()




