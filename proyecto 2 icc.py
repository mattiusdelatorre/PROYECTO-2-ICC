import os

 

def menu():
	os.system('cls') # WINDOW = cls , LINUX = clear

	print ("Selecciona una opción")
	print ("\t1. Agregar una linea")
	print ("\t2. Agregar una elipse o circulo")
	print ("\t3. Agregar un rectangulo o cuadrado")
	print ("\t4. Agregar un triangulo")
	print ("\t5. Mostrar un dibujo")
	print ("\t6. Borrar dibujo actual")
	print()
	print()
	print ("\t0. Salir del programa")
 
tabla = []
for i in range(42):
	a = [" "]*82
	tabla.append(a)
for i in range(42):
	for j in range(82): 
		if(i == 0 or j == 0 or i ==41 or j == 81): 
			tabla[i][j]='.'


def BresenhamLine(x0,y0,x1,y1):
    # algoritmo de trazado de lineas
	dx=x1-x0
	dy=y1-y0
	if dy<0:
		dy=-dy
		pasoy=-1
	else:
		pasoy=1
	if dx<0:
		dx=-dx
		pasox=-1
	else:
		pasox=1
	x=x0
	y=y0
	tabla[y][x]='X'
	if dx>dy:
		p = 2*dy - dx
		incrementoE = 2*dy
		incrementoNE = 2*(dy-dx)
		while x!=x1:
			x = x + pasox
			if p<0:
				p = p + incrementoE
			else:
				y = y + pasoy
				p = p + incrementoNE
			tabla[y][x]='X'
	else:
		p = 2*dx - dy
		incE = 2*dx
		incNE = 2*(dx-dy)
		while y!=y1:
			y = y + pasoy
			if p<0:
				p = p + incE
			else:
				x = x + pasox
				p = p + incNE
			tabla[y][x]='X'

while True:
	menu()
	opcionMenu = input()
	if opcionMenu=="1":
		# LINEA
		print("Ingrese coordenadas del primer punto")
		b =  int(input()) 
		a =  int(input()) 
		print("Ingrese coordenadas del segundo punto")
		d =  int(input()) 
		c =  int(input()) 
		if a>=41 or b>=81 or c>=41 or d>=81 :
			print("")
			print("Entrada incorrecta")
			input("Pulsa una tecla para continuar\n")
			print("")
		else:
			BresenhamLine(b,a,d,c)


	elif opcionMenu=="2":
		# CIRCULO
		print("Ingrese coordenadas del centro")
		b =  int(input()) 
		a =  int(input()) 
		print("Ingrese longitud del radio en el eje X")
		rx =  int(input()) 
		print("Ingrese longitud del radio en el eje Y")
		ry =  int(input()) 
		if (a<1 or b<1  or rx<1 or ry<1 or a+ry>=41 or a<=ry or b+rx>=81 or b<=rx):
			print("")
			print("Entrada incorrecta")
			input("Pulsa una tecla para continuar\n")
			print("")
		else:
			x = 0
			y = ry
			rx2=rx*rx
			ry2=ry*ry
			tabla[a+ry][b]='X'
			tabla[a-ry][b]='X'
			p1=ry2-(rx2*ry)+(0.25*rx2)
			while (ry2*x)<(rx2*y):
				if(p1<0):
					x=x+1
					p1=p1+(2*ry2*x)+ry2
				else:
					x=x+1 
					y=y-1
					p1=p1+(2*ry2*x)-(2*rx2*y)+ry2
				tabla[a+y][b+x]='X'
				tabla[a-y][b+x]='X'
				tabla[a-y][b-x]='X'
				tabla[a+y][b-x]='X'
				p2=(ry2)*pow((x+0.5),2)+(rx2)*pow((y-1),2)-(rx2*ry2)
			while(y>0):
				if p2>0:
					y=y-1
					p2=p2-(2*rx2*y)+rx2
				else:
					x=x+1
					y=y-1
					p2=p2 +(2*ry2*x)-(2*rx2*y)+rx2
				tabla[a+y][b+x]='X'
				tabla[a-y][b+x]='X'
				tabla[a-y][b-x]='X'
				tabla[a+y][b-x]='X'	    
				
	elif opcionMenu=="3":
		# RECTANGULO
		print("Ingrese el vertice inferior izquierdo")
		b =  int(input()) 
		a =  int(input()) 
		print("Ingrese la longitud de la base")
		base =  int(input()) 
		print("Ingrese la longitud de la altura")
		altura =  int(input()) 
		if a+altura >=41 or b+base>=81 or a<1 or b<1 or base<=0 or altura <=0:
			print("")
			print("Entrada incorrecta")
			input("Pulsa una tecla para continuar\n")
			print("")
		else:
			tabla[a][b]='X'
			for i in range(altura+1):
				tabla[a+i][b]=tabla[a+i][b+base]='X'
			for i in range(base+1):
				tabla[a][b+i]=tabla[a+altura][b+i]='X'

	elif opcionMenu=="4":
		# TRIANGULO
		print("Ingrese el vertice inferior izquierdo")
		b =  int(input()) 
		a =  int(input()) 
		print("Ingrese la longitud de la base")
		base =  int(input()) 
		print("Ingrese la longitud de la altura") 
		altura =  int(input()) 
		if a>=41 or b>=81  or base<1 or b+base>=81 or a+altura>=41:
			print("")
			print("Entrada incorrecta")
			input("Pulsa una tecla para continuar\n")
			print("")
		else:
			for i in range(base+1):
				tabla[int(a)][int(b+i)]='X'
			if base%2==0:
				BresenhamLine(b,a,b+int(base/2),a+altura)
				BresenhamLine(b+base,a,b+int(base/2),a+altura)
			else: 
				base=int((base-1)/2)
				BresenhamLine(b,a,b+base,a+altura)
				BresenhamLine(b+base*2+1,a,b+base+1,a+altura)
	elif opcionMenu=="5":
		#MOSTRAR EL DIBUJO
		for i in range(41,-1,-1):
			for j in range(82): 
				print(tabla[i][j], end='')
			print()
		print("")
		input("Pulsa una tecla para continuar\n")
		print("")	
	
	elif opcionMenu=="6":
		# BORRAR
		for i in range(42):
			for j in range(82): 
				if(i == 0 or j == 0 or i ==41 or j == 81): 
					tabla[i][j]='.'
				else: 
					tabla[i][j]=' '

	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
		print("")