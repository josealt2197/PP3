 
from PIL import Image, ImageDraw, ImageFont

def generarImagenCarton(cartonBingo): 
	
	cartonBase = Image.open('PlantillaCarton.png')
	draw = ImageDraw.Draw(cartonBase)
	fuenteNumeros = ImageFont.truetype('arial.ttf', size=45)
	fuenteCodigo = ImageFont.truetype('arial.ttf', size=35)
	color = 'rgb(0, 0, 0)'
	
	x=30
	y=165
	potencia=1

	matriz=cartonBingo[:-1]

	#Anotar los numeros de la matriz en la imagen.
	for i in range(0,len(matriz[0])):
		for j in range(0,len(matriz)):
			numero=str(cartonBingo[i][j])
			draw.text((x, y), numero, fill=color, font=fuenteNumeros)
			x+=110
		y=165+(85*potencia)-3
		potencia+=1
		x=30

	# draw.text((30, 165), "1", fill=color, font=fuenteNumeros) 
	# draw.text((140, 165), "2", fill=color, font=fuenteNumeros) 
	# draw.text((250, 165), "3", fill=color, font=fuenteNumeros) 
	# draw.text((360, 165), "4", fill=color, font=fuenteNumeros) 
	# draw.text((470, 165), "5", fill=color, font=fuenteNumeros) 
	
	# draw.text((30, 165+(85*1)-3), "6", fill=color, font=fuenteNumeros) 
	# draw.text((30, 165+(85*2)-3), "7", fill=color, font=fuenteNumeros)
	# draw.text((30, 165+(85*3)-3), "8", fill=color, font=fuenteNumeros)  
	# draw.text((30, 165+(85*4)-3), "9", fill=color, font=fuenteNumeros) 

	#Anotar el ID al final de la imagen.	
	draw.text((215, 585), cartonBingo[5], fill=color, font=fuenteCodigo) 

	cartonBase.save(cartonBingo[5]+'.png')

#Coordenadas en X = 30, 140, 250, 360, 470
#Coordenadas en Y = 165, 245, 325, 405, 485


def imprimirMatriz(lista):
	for i in lista:
	    for j in i:
	        print(j, end=" ")
	    print()