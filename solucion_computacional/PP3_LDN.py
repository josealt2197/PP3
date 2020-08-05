#Proyecto Programado 3 - Grupo: 01 
#Lógica de Negocio para el programa de Gestión de un Bingo.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import os
import sys
import csv
import random
from random import randint
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageDraw, ImageFont

cartonesCompletos = []
cartonesBinarios = []
cartonesAsignados = []
numerosCantados=[]
jugadores=0

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Admin. de Cartones
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista de matrices (cartones) requerida para generar otra lista.
Salidas: Una lista con sublistas de 2 campos, el primero con el codigo único al final de la matriz (identifi-
		 cador de cada cartón) y el otro campo con un 0. 
Restricciones: No valida restricciones.
'''
def generarAsignados(listaCartones):
	global cartonesAsignados
	cartonesAsignados=[]
	try:
		for i in range(0,len(listaCartones)):
			asignacion=[listaCartones[i][5],0]
			cartonesAsignados.append(asignacion)
		return 1	
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista de matrices (cartones) requerida para generar otra lista.
Salidas: Una lista con matrices de 5x5 con ceros como los valores de todos sus campos.
Restricciones: No valida restricciones.
'''
def generarBinario(listaCartones):
	global cartonesBinarios
	cartonesBinarios=[]
	try:
		for i in range(0,len(listaCartones)):
			asignacion=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],listaCartones[i][5]]
			cartonesBinarios.append(asignacion)
		return 1	
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un numero entero entre 1 y 75 generado por la función cantarNumero.
Salidas: 1 si no se produce ningun error en revision de los cartones, caso contrario -1.
Restricciones: No valida restricciones.
'''
def marcarNumeroCantado(numero):
	global cartonesCompletos
	global cartonesBinarios
	cartonPivote=[]
	cartonPorRevisar=[]
	try:
		for carton in range(0,len(cartonesCompletos)):
			cartonPorRevisar=cartonesCompletos[carton]
			for fila in range(0,len(cartonPorRevisar)-1):
				for columna in range(0,len(cartonPorRevisar[0])):
					if(cartonPorRevisar[fila][columna]==numero):
						cartonPivote=cartonesBinarios[carton]
						cartonPivote[fila][columna]=1
						cartonesBinarios[carton]=cartonPivote
		return 1
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Un número aleatorio entre 0 y 75.
Restricciones: No valida restricciones.
'''
def cantarNumero():
	global numerosCantados
	sys.setrecursionlimit(10000)
	try:
		if(len(numerosCantados)>=75):
			return -2
		numero = randint(1,75)
		if(numero in numerosCantados):
			return cantarNumero()
		else:
			numerosCantados.append(numero)
			if(marcarNumeroCantado(numero)==1):
				return numero 				
			else:
				return -1
	except Exception as e:
		print(e)
		return - 1 

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Eliminar los valores de las variables globales, e invocar a la función para eliminar las imágenes de 
		 los cartones generados. 
Restricciones: No valida restricciones.
'''
def eliminarCartones():
	global cartonesCompletos 
	global cartonesBinarios 
	global cartonesAsignados 
	global jugadores

	try:
		cartonesCompletos = []
		cartonesBinarios = []
		cartonesAsignados = []
		jugadores = 0
		eliminarPNGCartones()
		return 1
	except Exception as e:
		return -1


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un número entero para inicio y otro para fin, para obtener números aleatorios dentro de ese intervalo.
Salidas: Una lista de 5 espacios con números diferentes en cada espacio, dentro del intervalo genrado por las
		 entradas.
Restricciones: No valida restricciones
'''
def crearFila(inicio,fin):

	indiceFila=0
	fila=[]
	while(indiceFila!=5):
		num=randint(inicio,fin)
		if(num not in fila):
			fila.append(num)
			indiceFila+=1
	return fila	

#-----------------------------------------------------------------------------------------------------------#
'''
 Entradas: Una matriz cuadrada 
 Salidas: La matriz ingresada cambiando sus filas por columnas (o viceversa)   
 Restricciones: Ninguna
'''
def trasponerMatriz(matriz):
	traspuesta=[]

	for j in range(0,len(matriz[0])):
		fila = []
		for i in range(0,len(matriz)):
			fila.append(matriz[i][j])
		traspuesta.append(fila)

	return traspuesta

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Un código aleatorio de 6 caracteres, los 3 primeros letras y los ultimos 3 son números entre 0 y 9 
Restricciones: No valida restricciones.
'''
def generarIDCarton():
	idLetras=""
	idNumeros=""
	for i in range(0,3):
		idLetras=idLetras+(chr(random.randrange(97, 97 + 26)))
		idNumeros= idNumeros+str(randint(0,9))

	return idLetras.upper()+idNumeros

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Una matriz cuadrada de 5x5 en la cual las columnas contienen numeros aleatorios y únicos entre sí, 
		 dentro de los intervalos: 1 - 15,  16 - 30, 31 - 45, 46 - 60 y  61 - 75 y al final de la matirz un 
		 alfanumérico codigo único.  
Restricciones: No posee restricciones.
'''
def crearCarton():

	bingo=[[],[],[],[],[]]
	inicio=1
	fin=15

	for linea in range(0,len(bingo)) :
		bingo[linea]=crearFila(inicio,fin)
		inicio,fin=fin+1,fin+15

	bingo=trasponerMatriz(bingo)
	bingo.append(generarIDCarton())

	return bingo

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista de matrices (cartones) y una matriz individual.
Salidas: 1 en el caso de que la matriz individual no se encuentre repetida en la lista de matrices, y -1 si se
		 hallara una matriz que coincida con la recibida.
Restricciones: No valida restricciones.
'''
def validarCarton(listaCartones,carton):

	carton=carton[:-1]	
	for i in range(0, len(listaCartones)):
		cartonEnLista=listaCartones[i]
		if (cartonEnLista[:-1]==carton):
			return -1
	return 1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una valor entero que indica la cantidad de matrices (cartones) por ingresar en una lista.
Salidas: Una lista con matrices de 5x5 con un codigo único al final de la matriz.
Restricciones: No valida restricciones.
'''
def generarBingos(cantidad, totalBingos=[]):
	global cartonesCompletos
	global cartonesAsignados

	try:
		if(cantidad==0):
			generarAsignados(totalBingos)
			generarBinario(totalBingos)
			cartonesCompletos = totalBingos
			if(generarImagenes()==1):	
				return 1
			else:
				cartonesAsignados=[]
				cartonesCompletos=[]
				return -1
		else:
			carton=crearCarton()
			if(totalBingos!=[]):
				if(validarCarton(totalBingos,carton)==-1):
					return generarBingos(cantidad, totalBingos)
				else:
					return generarBingos(cantidad-1, totalBingos=totalBingos+[carton])
			else:
				return generarBingos(cantidad-1, totalBingos=totalBingos+[carton])

	except Exception as e:
		print(e)
		return -1		


#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Admin. de Imágenes
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: 1 si no se produce ningun error en el borrado de las imágenes de los cartones dentro de la carpeta 
		 indicada, caso contrario -1.
Restricciones: No valida restricciones.
'''
def eliminarPNGCartones():
	for imagen in os.listdir('Cartones'): 
		if imagen.endswith('.png'):
			os.remove('Cartones/'+imagen)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una matriz que contiene los valores para uno de los cartones generados.
Salidas: Una imagen en formato png que representa la matriz recibida dentro de un "cartón" de bingo.
Restricciones: No valida restricciones.
'''
def generarImagenCarton(cartonBingo): 
	
	cartonBase = Image.open('Recursos\PlantillaCarton.png')
	draw = ImageDraw.Draw(cartonBase)
	fuenteNumeros = ImageFont.truetype('arial.ttf', size=45)
	fuenteCodigo = ImageFont.truetype('arial.ttf', size=25)
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

	#Anotar el ID al final de la imagen.	
	draw.text((145, 585), "Identificador: "+cartonBingo[5], fill=color, font=fuenteCodigo) 

	cartonBase.save('Cartones\\'+cartonBingo[5]+'.png')

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Invoca la función que crea las imagenes de los cartones, según la cantidad de cartones generados
Restricciones: No valida restricciones.
'''
def generarImagenes():
	global cartonesCompletos

	try:
		for indice in range(0, len(cartonesCompletos)):
			generarImagenCarton(cartonesCompletos[indice])

		return 1
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una cadena de caracteres que corresponde al identificador de uno de los cartones generados.
Salidas: 1 si la cadena recibida corresponde al código de uno de los cartones generados o -1 si el valor 
		 recibido no se encuentra dentro de los cartones generados.
Restricciones: No valida restricciones. 
'''
def obtenerImagenCarton(codigo):
	global cartonesAsignados

	try:
		img = Image.open('Cartones\\'+codigo+'.png')		
		return 1
	except Exception as e:
		# print(e)
		return -1			

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Gestión del Juego
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: La cantidad de elementos o cartones que se encuentran dentro de a lista de cartones generados.
Restricciones: No valida restricciones. 
'''
def contarCartones():
	global cartonesAsignados
	global cartonesCompletos

	if(cartonesCompletos==[]):
		return 0
	else:
		return len(cartonesCompletos)
	

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Una lista de 3 campos: en el primero se incluya la cantidad de jugadores a los que les fue enviado al
		 menos un cartón, en el segundo la catidad de cartones generados y en el tercer campo un 1 si ya han sido 
		 asignados todos los cartones a un jugador y -1 en caso de no todos hayan sido asignados. 
Restricciones: 
'''
def obtenerValoresJuego():
	global cartonesAsignados
	global cartonesCompletos
	global jugadores
	global numerosCantados

	numerosCantados=[]
	cartonEnLista=[]
	datosPorRetornar=[]
	asignados=0

	try:
		datosPorRetornar.append(jugadores)
		datosPorRetornar.append(contarCartones())

		for i in range(0, len(cartonesAsignados)):
			cartonEnLista=cartonesAsignados[i]
			if (cartonEnLista[1]!=0):
				asignados+=1

		if(asignados<len(cartonesAsignados)):
			datosPorRetornar.append(-1)
		else:
			datosPorRetornar.append(1)

		return datosPorRetornar

	except Exception as e:
		print(e)
		return [-1]

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una matriz de 5x5.
Salidas: 1 si en las cuatro esquinas de la matriz hay un valor de "1", sino retorna -1.
Restricciones: No valida restricciones.
'''
def cartonEsquinas(carton):

	if (carton[0][0]==1 and carton[0][4]==1 and carton[4][0]==1 and carton[4][4]==1):
		return 1
	else:
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Los identificadores de los cartones generados que tienen un "1" en las cuatro esquinas.
Restricciones: No valida restricciones.
'''
def juegoCuatroEsquinas():
	global cartonesBinarios

	ganadores=[]

	for i in range(0,len(cartonesBinarios)):
		if (cartonEsquinas(cartonesBinarios[i]) == 1):
			ganadores=ganadores+[cartonesBinarios[i][5]]

	return ganadores

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una matriz de 5x5.
Salidas: 1 si en todos los campos de la matriz hay un valor de "1", sino retorna -1.
Restricciones: No valida restricciones.
'''
def cartonLleno(carton):
	for x in range(0,len(carton)):
		for y in range(0,len(carton[0])):
			if(carton[x][y]==0):
				return -1
	return 1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Los identificadores de los cartones generados que tienen un "1" en todos sus campos.
Restricciones: No valida restricciones.
'''
def juegoCartonLleno():

	global cartonesBinarios

	ganadores=[]

	for i in range(0,len(cartonesBinarios)):
		if (cartonLleno(cartonesBinarios[i]) == 1):
			ganadores=ganadores+[cartonesBinarios[i][5]]

	return ganadores

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: 1 si en las diagonales diagonales principal y secundaria todos los tienen como valor "1", sino -1.
Restricciones: No valida restricciones.
'''
def cartonX(carton):

	for i in range(0,len(carton)):
		for j in range(0,len(carton[0])):
			if(i==j):
				if(carton[i][j]==0):
					return -1

	for i in range(0,len(carton)):
		contador=0
		j=len(carton[0])-1
		while(j>=0):
			if(i==contador):
				if(carton[i][j]==0):
					return -1
			contador+=1
			j-=1

	return 1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna.
Salidas: Los identificadores de los cartones generados que tienen un "1" en los campos de las diagonales 
		 principal y secundaria de la matriz.
Restricciones: No valida restricciones.
'''
def juegoCartonX():

	global cartonesBinarios

	ganadores=[]

	for i in range(0,len(cartonesBinarios)):
		if (cartonX(cartonesBinarios[i]) == 1):
			ganadores=ganadores+[cartonesBinarios[i][5]]

	return ganadores

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna.
Salidas: 1 si en los espacios que forman una Z en la matriz se tiene como valor "1", sino -1
Restricciones: No valida restricciones.
'''
def cartonZ(carton):

	for i in range(0,len(carton)):
		contador=0
		j=len(carton[0])-1
		while(j>=0):
			if(i==contador):
				if(carton[i][j]==0):
					return -1
			contador+=1
			j-=1
	for i in range(0,len(carton[0])):
		if(carton[0][i]==0):
			return -1
	for i in range(0,len(carton[4])):
		if(carton[4][i]==0):
			return -1
	return 1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: Los identificadores de los cartones generados que tienen un "1" en los campos que forman una Z en la 
		 matriz.
Restricciones: No valida restricciones.
'''
def juegoCartonZ():

	global cartonesBinarios

	ganadores=[]

	for i in range(0,len(cartonesBinarios)):
		if (cartonZ(cartonesBinarios[i]) == 1):
			ganadores=ganadores+[cartonesBinarios[i][5]]

	return ganadores

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una cadena de caracteres que indica el tipo de juego seleccionado.
Salidas: Una lista con los identificadores retronados por alguna de las funciones que validan los valores de 
		 los cartones generados para un tipo de juego seleccionado, o -1 si el tipo recibico no correspondiera
Restricciones: 
'''
def validarTipoJuego(tipo):

	if (tipo=="Jugar en X"):
		return juegoCartonX()
	elif (tipo=="Cuatro esquinas"):
		return juegoCuatroEsquinas()
	elif (tipo=="Cartón lleno"):
		return juegoCartonLleno()
	elif (tipo=="Jugar en Z"):
		return juegoCartonZ()
	else:
		return [-1]

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Envío de Correos
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
#-----------------------------------------------------------------------------------------------------------#

'''
Entradas: Una cadena con el correo al cual deben enviarse los cartones, y una lista con losidentificadores de
		  los cartones que deben adjuntarse al mensaje. 
Salidas: Envía los cartones recibidos al correo del usuario recibido. 
Restricciones: No valida restricciones.
'''
def enviarCorreo(correo, cartonesPorAsignar):

	global jugadores

	emisor = 'proyecto3bingo@gmail.com'
	receptor = correo

	mensaje = MIMEMultipart('related')
	mensaje['Subject'] = 'Invitación para Juego de Bingo'
	mensaje['From'] = emisor
	mensaje['To'] = receptor
	mensaje.preamble = 'Carton(es) para Juego de Bingo'
	
	msgAlternative = MIMEMultipart('alternative')
	mensaje.attach(msgAlternative)

	textoAlternativo = """¡Hola!
	Parece que has sido invitado a participar en un juego de BINGO
	Junto a este correo se han adjuntado los cartones para que puedas participar
	¡Buena Suerte!"""
	msgText = MIMEText(textoAlternativo)
	msgAlternative.attach(msgText)

	msgText = MIMEText('<img src="cid:image1">', 'html')
	msgAlternative.attach(msgText)

	archivoImagen = open('Recursos\imagenCorreoCartones.png', 'rb')
	msgImage = MIMEImage(archivoImagen.read())
	archivoImagen.close()

	msgImage.add_header('Content-ID', '<image1>')
	mensaje.attach(msgImage)

	for i in range(0,len(cartonesPorAsignar)): 
		filename = cartonesPorAsignar[i]+".png"		
		attachment = open('Cartones/'+cartonesPorAsignar[i]+'.png', "rb")
  
		cartonesAdjuntos = MIMEBase('application', 'octet-stream') 
		cartonesAdjuntos.set_payload((attachment).read()) 
		encoders.encode_base64(cartonesAdjuntos) 	   
		cartonesAdjuntos.add_header('Content-Disposition', "attachment; filename= %s" % filename) 	  
		mensaje.attach(cartonesAdjuntos)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		    server.login('proyecto3bingo@gmail.com', 'cursoTEC2020')
		    server.sendmail(emisor, receptor, mensaje.as_string())
		jugadores+=1	
		return 1
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Cadena de caracteres con el valor de la cedula de un jugador y lista de cartones por asignar
Salidas: 1 si la cedula recibida se encuentra dentro de las de los jugadores registrados o -1 si se encontrara
Restricciones: No valida restricciones.
'''
def enviarCartones(pCedula, cartonesPorAsignar):
	listaCedulas = obtenerCedulas()
	listaCorreos = obtenerCorreos()

	for indice in range(0, len(listaCedulas)):
		if(listaCedulas[indice]==pCedula):
			if(enviarCorreo(listaCorreos[indice],cartonesPorAsignar)==1):
				break
			else:
				return -1

	return 1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una cadena con el correo al cual debe enviarse la notificación del ganador.
Salidas: Envía el correo de notificación al jugador que haya resultado ganador.  
Restricciones: No valida restricciones.
'''
def enviarCorreoGanador(correo):

	emisor = 'proyecto3bingo@gmail.com'
	receptor = correo

	mensaje = MIMEMultipart('related')
	mensaje['Subject'] = 'Ganador del Bingo'
	mensaje['From'] = emisor
	mensaje['To'] = receptor
	mensaje.preamble = 'Ganador del Bingo'
	
	msgAlternative = MIMEMultipart('alternative')
	mensaje.attach(msgAlternative)

	textoAlternativo = """¡Muchas Felicidades!</h1>
    Parece que has resultado ganador del juego de Bingo
    Responde a este correo para conocer la forma en que recibirás tu premio."""
	msgText = MIMEText(textoAlternativo)
	msgAlternative.attach(msgText)

	msgText = MIMEText('<img src="cid:image1">', 'html')
	msgAlternative.attach(msgText)

	archivoImagen = open('Recursos\imagenCorreoGanador.png', 'rb')
	msgImage = MIMEImage(archivoImagen.read())
	archivoImagen.close()

	msgImage.add_header('Content-ID', '<image1>')
	mensaje.attach(msgImage)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		    server.login('proyecto3bingo@gmail.com', 'cursoTEC2020')
		    server.sendmail(emisor, receptor, mensaje.as_string())	
		return 1
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con elementos de un mismo tipo
Salidas:La lista ingresada como parametro, omitiendo los valores que estuvieran repetidos dentro de esta.
Restricciones:Ninguna
'''
def eliminarDuplicados(lista,nuevaLista=[]):
    if (lista==[]):
        return nuevaLista
    else:
        if (buscarElemento(nuevaLista,lista[0])==-1):
            return eliminarDuplicados(lista[1:],nuevaLista+[lista[0]])
        else:
            return eliminarDuplicados(lista[1:],nuevaLista)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Lista de identificadores de los cartones ganadores
Salidas: 1 si la notificación por correo fue enviada correctamente, o -1 si esta no fuere enviada.
Restricciones: No valida restricciones.
'''
def notificarGanadores(ganadores):
	listaJugadores = leerArchivoCSV()
	cartonEnLista=[]
	correos = []

	for i in range(0, len(cartonesAsignados)):
		cartonEnLista=cartonesAsignados[i]
		for j in range(0,len(ganadores)):
			if (cartonEnLista[0]==ganadores[j]):
				for k in range(0,len(listaJugadores)):
					if(listaJugadores[k][1]==cartonEnLista[1]):
						correos.append(listaJugadores[k][2]) 

	correos = eliminarDuplicados(correos)
	for indice in range(0, len(correos)):
		if(enviarCorreoGanador(correos[indice])==1):
			break
		else:
			return -1

	return 1
 
#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un valor entero con la cantidad de cartones por asignar y la cedula del jugador l cual deben asignarse
Salidas: 
		--> la lista de los identificadores de los cartones que se encuentran disponibles para asignar.
		--> -1 si se hubiera producido un error asignar los cartones disponibles a l numero de cedula recibido.
		--> -2 en caso de que la cantidad requerida para asignar sea mayor a la cantidad de cartones disponibles.
Restricciones: No valida restricciones.
'''
def asignarCartones(cantidad, cedula):
	global cartonesAsignados

	cartonesPorEnviar=[]

	if(cantidad>validarDisponibles()):
		return [-2]

	try:
		for i in range(0,len(cartonesAsignados)):
			if(cantidad>0 and cartonesAsignados[i][1]==0):
				cartonesPorEnviar.append(cartonesAsignados[i][0])
				cartonesAsignados[i][1]=cedula
				cantidad-=1				
		return cartonesPorEnviar	
	except Exception as e:
		print(e)
		return [-1]

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna.
Salidas: La cantidad de los cartones generados que no han sido asignados a ningun jugador. 
Restricciones: 
'''
def validarDisponibles():
	global cartonesAsignados

	cantidad=0

	for i in range(0,len(cartonesAsignados)):
		if(cartonesAsignados[i][1]==0):
			cantidad+=1				
	return cantidad	


#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Admin. de CSV
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una cadena decaracteres que contiene la direccion de correo electronica ingresada para un jugador
Salidas: True si la direccion ingresada corresponde a un formato valido para el correo electrónico, False en
		 de que incumpla alguna de las delimitaciones sobre la estructura.
Restricciones: 
'''
def validarCorreo(correo):
    contador=0
    longitud=len(correo)
    punto=correo.find(".")
    arroba=correo.find("@")

    if(punto==-1 or arroba==-1):
    	return False

    for i in range (0,arroba):
        if((correo[i]>='a' and correo[i]<='z') or (correo[i]>='A' and correo[i]<='Z')):
            contador=contador+1
    
    if(contador>0 and arroba>0 and (punto-arroba)>0 and (punto+1)<longitud):
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Crear el archivo jugadores.csv con las columnas necesarias para agregar jugadores 
Restricciones: No valida restricciones.
'''
def crearArchivoCSV():
    with open('Recursos/jugadores.csv', mode='w') as archivoCSV:
        columnas = ['nombre', 'cedula', 'correo']
        writer = csv.DictWriter(archivoCSV, fieldnames=columnas)
        writer.writeheader()

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Tres cadenas de caracteres con los datos de un nuevo jugador
Salidas: Se adiciona una nueva linea al archivo CSV con el nombre, la cedula y el correo del jugador nuevo
Restricciones: No valida restricciones.
'''
def agregarJugadorCSV(nombre, cedula, correo):
	try:
		archivo = open("Recursos/jugadores.csv", mode='r')
		archivo.close()
	except IOError as e:
		print("Creando archivo de Jugadores")
		crearArchivoCSV()

	try:
		with open('Recursos/jugadores.csv', mode='a') as archivoCSV:
			columnas = ['nombre', 'cedula', 'correo']
			writer = csv.DictWriter(archivoCSV, fieldnames=columnas)

			writer.writerow({'nombre': nombre, 'cedula': cedula, 'correo': correo})
	except Exception as e:
		print(e)
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Eliminar los elementos vacíos dentro de una lista. 
Restricciones: No valida restricciones.
'''
def eliminarVacios(lista):
	nuevaLista=[]
	for elemento in lista:
		if(elemento!=[]):
			nuevaLista.append(elemento)
	
	return nuevaLista	

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Lee el archivo jugadores.csv y lista los jugadores contenidos en este. 
Restricciones: No valida restricciones.
'''
def leerArchivoCSV():
	with open('Recursos/jugadores.csv', mode='r') as archivoCSV:
		datosJugadores = csv.reader(archivoCSV)
		listaJugadores = list(datosJugadores)

	listaJugadores = eliminarVacios(listaJugadores)

	return listaJugadores[1:]

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Lista de correos de los jugadores dentro del archivo CSV 
Restricciones: No valida restricciones.
'''
def obtenerCorreos():
	listaJugadores = leerArchivoCSV()
	listaCorreos = []
	
	for jugador in listaJugadores:
		listaCorreos.append(jugador[2]) 

	return listaCorreos

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Lista de cédulas de los jugadores dentro del archivo CSV 
Restricciones: No valida restricciones.
'''
def obtenerCedulas():
	listaJugadores = leerArchivoCSV()
	listaCedulas = []
	
	for jugador in listaJugadores:
		listaCedulas.append(jugador[1]) 

	return listaCedulas

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Cadena de caracteres con el valor de la cédula de un jugador
Salidas: 1 si la cedula recibida se encuentra dentro de las de los jugadores registrados, sino -1 
Restricciones: No valida restricciones.
'''
def validarCedula(pCedula):
	listaCedulas = obtenerCedulas()
	
	for cedula in listaCedulas:
		if(cedula==pCedula):
			return 1

	return -1
