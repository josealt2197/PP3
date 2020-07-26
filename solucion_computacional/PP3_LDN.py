#Proyecto Programado 3 - Grupo: 01 
#Lógica de Negocio para el programa de Gestión de un Bingo.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import csv
import random
import smtplib, ssl
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageDraw, ImageFont

cartonesCompletos = []
cartonesBinarios = []
cartonesAsignados = []

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cantidad de matrices a meter en una lista.
Salidas: Una lista Con matrices de 5x5 con un codigo único al final de la matriz.
Restricciones: No valida restricciones.
'''
def generarAsignados(listaCartones):
	global cartonesAsignados
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
Entradas:Un número 
Salidas: Una lista con el numero de entrada
Restricciones: No valida restricciones
''' 
def ListaNumerosCantados(num):
	listaNumerosCantados=[]
	if (num not in listaNumerosCantados):
		return listaNumerosCantados.append(num)
	return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas: Un número random entre 0 y 75
Restricciones:No valida restricciones
'''
def cantarNumero():
	return randint(0,75)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una lista
Salidas: La lista de entrada vacia
Restricciones:No valida restricciones
'''
def eliminarBingos(lista):
	lista=[]
	return lista

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
			cartonesCompletos = totalBingos
			if(generarImagenes()==1):	
				print(cartonesAsignados)		
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

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Envía los cartones seleccionados al usuario recibido 
Restricciones: No valida restricciones.
'''
def enviarCorreo(correo):
    
    correoDeEnvio = "proyecto3bingo@gmail.com"
    correoReceptor = correo
    contrasena = "cursoTEC2020"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Cartón para Juego de Bingo"
    message["From"] = correoDeEnvio
    message["To"] = correoReceptor

    text = """\
    Hola,
    ¿Como estás?
    Te hemos adjuntado tu(s) cartón(es) para el Bingo"""
    html = """\
    <html>
      <body>
        <p>Hola,<br>
           ¿Como estás?<br>
           Te hemos adjuntado tu(s) cartón(es) para el Bingo
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    parte1 = MIMEText(text, "plain")
    parte2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(parte1)
    message.attach(parte2)
    

    # Create secure connection with server and send email
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
def enviarCartones(pCedula):
	listaCedulas = obtenerCedulas()
	listaCorreos = obtenerCorreos()

	for indice in range(0, len(listaCedulas)):
		if(listaCedulas[indice]==pCedula):
			if(enviarCorreo(listaCorreos[indice])==1):
				break
			else:
				return -1

	return 1

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
Entradas: 
Salidas: 
Restricciones: 
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
