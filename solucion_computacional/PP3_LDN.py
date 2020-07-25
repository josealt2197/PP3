#Proyecto Programado 3 - Grupo: 01 
#Lógica de Negocio para el programa de Gestión de un Bingo.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import csv
import random 
from random import randint

cartonesCompletos = []

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
	try:
		if(cantidad==0):
			cartonesCompletos = totalBingos
			print(cartonesCompletos)
			return 1
		else:
			return generarBingos(cantidad-1, totalBingos=totalBingos+[crearBingo()])

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










