import random 
from random import randint

def eliminarBingos(lista):
	lista=[]
	return lista


def cantidadBingos(cantidad, totalBingos=[]):
	if(cantidad==0):
		return totalBingos
	else:
		return cantidadBingos(cantidad-1, totalBingos=totalBingos+crearBingo())

def crearFila(inicio,fin):

	indiceFila=0
	fila=[]
	while(indiceFila!=5):
		num=randint(inicio,fin)
		if(num not in fila):
			fila.append(num)
			indiceFila+=1
	return fila	

def matrizTraspuesta(matriz):
	traspuesta=[]

	for j in range(0,len(matriz[0])):
		fila = []
		for i in range(0,len(matriz)):
			fila.append(matriz[i][j])
		traspuesta.append(fila)

	return traspuesta

def generarIDCarton():
	idLetras=""
	idNumeros=""
	for i in range(0,3):
		idLetras=idLetras+(chr(random.randrange(97, 97 + 26)))
		idNumeros= idNumeros+str(randint(0,9))

	return idLetras.upper()+idNumeros

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













