import random 
from random import randint


'''
Entradas:Un número 
Salidas: Una lista con el numero de entrada
Restricciones: No valida restricciones
''' 
def ListaNumerosCantados(num):
	listaNumerosCantados=[]
	if (num not in listaNumerosCantados)
		return listaNumerosCantados.append(num)
	return -1

'''
Entradas:Ninguna
Salidas: Un número random entre 0 y 75
Restricciones:No valida restricciones
'''
def cantarNumero():
	return randint(0,75)

'''
Entradas:Una lista
Salidas: La lista de entrada vacia
Restricciones:No valida restricciones
'''
def eliminarBingos(lista):
	lista=[]
	return lista

'''
Entradas:Una cantidad de matrices a meter en una lista.
Salidas: Una lista Con matrices de 5x5 con un codigo único al final de la matriz.
Restricciones: No valida restricciones.
'''
def cantidadBingos(cantidad, totalBingos=[]):
	if(cantidad==0):
		return totalBingos
	else:
		return cantidadBingos(cantidad-1, totalBingos=totalBingos+crearBingo())

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

'''
 Entradas: Una matriz cuadrada 
 Salidas: La matriz ingresada cambiando sus filas por columnas 
          (o viceversa)   
 Restricciones: Ninguna
'''
def matrizTraspuesta(matriz):
	traspuesta=[]

	for j in range(0,len(matriz[0])):
		fila = []
		for i in range(0,len(matriz)):
			fila.append(matriz[i][j])
		traspuesta.append(fila)

	return traspuesta

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

	bingo=matrizTraspuesta(bingo)
	bingo.append(generarIDCarton())
	return bingo













