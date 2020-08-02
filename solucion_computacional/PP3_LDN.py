#Proyecto Programado 3 - Grupo: 01 
#Lógica de Negocio para el programa de Gestión de un Bingo.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import os
import sys
import csv
import random
import smtplib, ssl
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders
from PIL import Image, ImageDraw, ImageFont

cartonesCompletos = []
cartonesBinarios = []
cartonesAsignados = []
numerosCantados= []

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Admin. de Cartones
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cantidad de matrices a meter en una lista.
Salidas: Una lista Con matrices de 5x5 con ceros en su interior.
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
Entradas:El numero generado por la función cantarNumero
Salidas:1 si no se produce ningun error en  revision de los cartones, y caso contrario -1
Restricciones: No hay
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
Entradas:Una cantidad de matrices a meter en una lista.
Salidas: Una lista Con matrices de 5x5 con un codigo único al final de la matriz.
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
Entradas:Ninguna
Salidas: Un número random entre 0 y 75
Restricciones:No valida restricciones
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
Entradas: Ninguna
Salidas: Eliminar los valores de las listas
Restricciones:No valida restricciones
'''
def eliminarCartones():
	global cartonesCompletos 
	global cartonesBinarios 
	global cartonesAsignados 

	try:
		cartonesCompletos = []
		cartonesBinarios = []
		cartonesAsignados = []
		return 1
	except Exception as e:
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un número de inicio y otro de fin para sacar números random entre ese intervalo.
Salidas: Una lista de 5 espacios con números diferentes en cada espacio, entre los intervalos 
         de entrada.
Restricciones:No valida restricciones
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
 Salidas: La matriz ingresada cambiando sus filas por columnas 
          (o viceversa)   
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
Entradas: Ninguna
Salidas: Genera codigos random de 6 caracteres, los primeros 3 son letras
         y los ultimos 3 son numeros 
Restricciones: No valida restricciones
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
Entradas:Ninguna.
Salidas: Una lista con matricez cuadradas de 5x5 en las cuales
         la primer columna tiene numeros ramdom entre 1 y 15, 
         la sengunda del 16 al 30, la tercera del 31 al 45, la 
         cuarta 46 al 60, la quinta del 61 al 75 y al final de la matirz un codigo único.  
Restricciones: No posee restricciones.
'''
def crearBingo():

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
Entradas: Una lista grande de listas y una lista sola
Salidas: 
         1 en el caso de que la lista pequeña no se encuentre en la lista grande 
         -1 en el caso de que la lista pequeña se encuentre en la lista grande
Restricciones: No valida restricciones
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
Entradas:Una cantidad de matrices a meter en una lista.
Salidas: Una lista Con matrices de 5x5 con un codigo único al final de la matriz.
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
			carton=crearBingo()
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
Entradas:Ninguna
Salidas:1 si no se produce ningun error en el borrado de las imágenes de los cartones, y caso contrario -1
Restricciones: No hay
'''
def eliminarPNGCartones():
	for imagen in os.listdir('Cartones'): 
		if imagen.endswith('.png'):
			os.remove('Cartones/'+imagen)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una matriz conteniendo los valores para uno delos cartones generados
Salidas: Una imagen en formato png que contiene una representación de la matriz recibida dentro de un "cartón" de
	     bingo.
Restricciones: No valida restricciones.
'''
def generarImagenCarton(cartonBingo): 
	
	cartonBase = Image.open('Recursos\PlantillaCarton.png')
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

	#Anotar el ID al final de la imagen.	
	draw.text((215, 585), cartonBingo[5], fill=color, font=fuenteCodigo) 

	cartonBase.save('Cartones\\'+cartonBingo[5]+'.png')

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: creacion de las imagenes en formato png para los "cartones" del bingo.
Restricciones: Ninguna
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
Entradas: Ninguna
Salidas: 
Restricciones: 
'''
def obtenerImagenCarton(codigo):
	global cartonesAsignados

	try:
		for i in range(0, len(cartonesAsignados)):
			cartonEnLista=cartonesAsignados[i]
			if (cartonEnLista[0]==codigo):
				return 1

	except Exception as e:
		print(e)
		return -1			

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Gestión del Juego
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: 
Restricciones: 
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
Salidas: 
Restricciones: 
'''
def obtenerValoresJuego():
	global cartonesAsignados
	global cartonesCompletos

	cartonEnLista=[]
	datosPorRetornar=[]
	jugadores=0

	try:
		for i in range(0, len(cartonesAsignados)):
			cartonEnLista=cartonesAsignados[i]
			if (cartonEnLista[1]!=0):
				jugadores+=1

		datosPorRetornar.append(jugadores)
		datosPorRetornar.append(contarCartones())

		return datosPorRetornar

	except Exception as e:
		print(e)
		return [-1]

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una matriz de 5x5.
Salidas: Valida si en las cuatro esquijas de la matriz hay un uno retorna 1 si no retorna -1.
Restricciones: No valida restricciones.
'''
def cartonEsquinas(carton):

	if (carton[0][0]==1 and carton[0][4]==1 and carton[4][0]==1 and carton[4][4]==1):
		return 1
	else:
		return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna.
Salidas: Las matrices de la variable global que tienen un 1 en las cuatro esquinas.
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
Entradas:Una matriz de 5x5.
Salidas: Valida si todos los elementos de la matriz son uno retorna 1 si no retorna -1.
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
Entradas:Ninguna.
Salidas: Las matrices de la variable global cartonesBinarios que todos los elementos en ella sean 1.
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
Entradas:Ninguna.
Salidas: Las matrices de la variable global cartonesBinarios que todos los elementos en ella sean 1.
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
Salidas: Las matrices de la variable global cartonesBinarios que tengan una un uno en los espacios que forman una x en la matriz.
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
Salidas: Las matrices de la variable global cartonesBinarios que tengan una un uno en los espacios que forman una x en la matriz.
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
Entradas:Ninguna.
Salidas: Las matrices de la variable global cartonesBinarios que tengan una un uno en los espacios que forman una Z en la matriz.
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
Entradas:
Salidas:
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
Entradas: Ninguna
Salidas: Envía los cartones seleccionados al usuario recibido 
Restricciones: No valida restricciones.
'''
def enviarCorreo(correo, cartonesPorAsignar):

	correoDeEnvio = "proyecto3bingo@gmail.com"
	correoReceptor = correo
	contrasena = "cursoTEC2020"

	message = MIMEMultipart("alternative")
	message["Subject"] = "Cartón para Juego de Bingo"
	message["From"] = correoDeEnvio
	message["To"] = correoReceptor

	text = """\¡Hola!</h1>
	Parece que has sido invitado a participar en un juego de BINGO
	Junto a este correo se han adjuntado los cartones para que puedas participar
	¡Buena Suerte!"""

	textoHTML = open("Recursos\plantillaCorreo.html","r", encoding='utf-8')
	html = textoHTML.read()
	textoHTML.close()

	parte1 = MIMEText(text, "plain")
	parte2 = MIMEText(html, "html")

	message.attach(parte1)
	message.attach(parte2)

	# for imagen in os.listdir('Cartones'): 
	# 	if imagen.endswith('.png'):
	for i in range(0,len(cartonesPorAsignar)): 
		filename = cartonesPorAsignar[i]+".png"
		
		attachment = open('Cartones/'+cartonesPorAsignar[i]+'.png', "rb")
  
		adjunto = MIMEBase('application', 'octet-stream') 

		adjunto.set_payload((attachment).read()) 

		encoders.encode_base64(adjunto) 
		   
		adjunto.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
		  
		message.attach(adjunto)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(correoDeEnvio, contrasena)
			server.sendmail(
			correoDeEnvio, correoReceptor, message.as_string()
		)

		return 1
	except Exception as e:
		print(e)
		return -1

'''
Entradas: Ninguna
Salidas: Envía el correo de notificación a los jugadores que resutaron ganadores  
Restricciones: No valida restricciones.
'''
def enviarCorreoGanador(correo):

	correoDeEnvio = "proyecto3bingo@gmail.com"
	correoReceptor = correo
	contrasena = "cursoTEC2020"

	message = MIMEMultipart("alternative")
	message["Subject"] = "Ganador del Bingo"
	message["From"] = correoDeEnvio
	message["To"] = correoReceptor

	text = """\¡Muchas Felicidades!</h1>
    Parece que has resultado ganador del juego de Bingo
    Responde a este correo para conocer la forma en que recibirás tu premio."""

	textoHTML = open("Recursos\plantillaGanador.html","r", encoding='utf-8')
	html = textoHTML.read()
	textoHTML.close()

	parte1 = MIMEText(text, "plain")
	parte2 = MIMEText(html, "html")

	message.attach(parte1)
	message.attach(parte2)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(correoDeEnvio, contrasena)
			server.sendmail(
			correoDeEnvio, correoReceptor, message.as_string()
		)

		return 1
	except Exception as e:
		print(e)
		return -1
 
#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Cadena de caracteres con el valor de la cedula de un jugador
Salidas: 
		-> 1 si la cedula recibida se encuentra dentro de las de los jugadores registrados
		-> -1 si la cedula recibida NO se encuentra dentro de las de los jugadores registrados
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
Entradas:
Salidas:
Restricciones: 
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
Entradas:
Salidas:
Restricciones: 
'''
def validarDisponibles():
	global cartonesAsignados

	cantidad=0

	for i in range(0,len(cartonesAsignados)):
		if(cartonesAsignados[i][1]==0):
			cantidad+=1				
	return cantidad	

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:
Salidas:
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

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# Funciones para Admin. de CSV
#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

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
Salidas: Lista de CORREOS de los jugadores dentro del archivo CSV 
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
Salidas: Lista de CEDULAS de los jugadores dentro del archivo CSV 
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
Entradas: Cadena de caracteres con el valor de la cedula de un jugador
Salidas: 
		-> 1 si la cedula recibida se encuentra dentro de las de los jugadores registrados
		-> -1 si la cedula recibida NO se encuentra dentro de las de los jugadores registrados
Restricciones: No valida restricciones.
'''
def validarCedula(pCedula):
	listaCedulas = obtenerCedulas()
	
	for cedula in listaCedulas:
		if(cedula==pCedula):
			return 1

	return -1
