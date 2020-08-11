#Proyecto Programado 3 - Grupo: 01 
#Interfaz Gráfica para el programa de Gestión de un Bingo.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import PP3_LDN as LDN
from tkinter import *                   
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk

#-----------------------------------------------------------------------------------------------------------#
#Lista de Variables Globales
ventanaGestorBingos=""
cantidadCartones=""
codigoCarton=""
opcionJuego_StringVar=""
premio=""
labelTipo=""
premioJuego=""
txtNumCantados=""
nombreJugador=""
cedulaJugador=""
correoJugador=""
cantidadEnviar=""
cedulaEnviar=""
frameImagen=""
subFrConsultar=""
txtNumCantados=""
numerosCantados=""
labelTotCartones=""
labelTotJugadores=""
tipoJuegoSeleccionado=""
btnCantar=""
btnIniciar=""
labelAsignacion=""

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Un caracter o una cadena de caracteres  
Salidas:True si el caracter es un numero o False si el caracter no es un numero con decimales
Restricciones:No valida restricciones
'''
def esNumero(caracter):
    try:
        resultado = int(caracter)
        return True
    except:
        return False

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un número entero positivo en el espacio de Cantidad. 
Salidas: Genera el número de cartones que se ingresó en el apartado de Generar Cartones del Bingo.
Restricciones: el campo de cantidad debe contener un numero entero positivo.
'''
def comandoGenerarCartones():
	global cantidadCartones

	cantidadStr=cantidadCartones.get()
	cantidadNum=0

	if(cantidadStr==""):
		messagebox.showwarning("Texto Vacío","No se ha ingresado la cantidad requerida")
		
	else:
		if(esNumero(cantidadStr)==True):
			cantidadNum = int(cantidadStr)

			if (cantidadNum>=1 and cantidadNum<=500):			
				resultado=messagebox.askquestion('Generar Cartones','¿Desea generar '+str(cantidadNum)+' cartones? \nEste proceso podría tomar un momento')

				if (resultado=='yes'):

					LDN.eliminarCartones()

					valorRetorno = LDN.generarBingos(cantidadNum)

					if(valorRetorno != -1):
						messagebox.showinfo("Cartones Generados","Todos los cartones han sido generados.")
						cantidadCartones.delete(0,END)					
					else:
						messagebox.showerror("Error al Generar","Se ha producido un error al generar los cartones")	  
			else:
				messagebox.showwarning("Número no valido","La cantidad debe ser un número entre 1 y 500.")
		else:
			messagebox.showwarning("Valor no válido","La cantidad ingresada debe ser un número.")


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: El identificador de algun carton generado por el programa. 
Salidas: Muestra en el apartado de Consultar Cartón, el carton ingresado en el espacio de identificación.
Restricciones: Debe ingresarse una identificación de un carton que se haya creado en el programa abierto. 
'''
def comandoMostrarCarton():
	global codigoCarton
	global frameImagen
	global subFrConsultar
	global ventanaGestorBingos
	global labelAsignacion

	codigo=codigoCarton.get()
	valorRetorno=[]

	if(LDN.contarCartones()!=0):
		if(codigo==""):
			messagebox.showwarning("Texto Vacío","Deben ingresar un código para el identificador.")	
		else:
			
			valorRetorno = LDN.obtenerImagenCarton(codigo)

			if(valorRetorno != [-1]):
				
				if(valorRetorno[0]!=0):
					labelAsignacion.configure(text=str(valorRetorno[1]+" - "+valorRetorno[0]))	
				else:
					labelAsignacion.configure(text="No asignado")

				frameImagen.destroy()
				frameImagen = Frame(subFrConsultar, width=220, height=252)
				frameImagen.grid(row=2, column=1, padx=5, pady=5)
				img = Image.open('Cartones\\'+valorRetorno[2]+'.png')
				img = img.resize((220, 252), Image.BICUBIC)
				tkimage = ImageTk.PhotoImage(img)
				labelImage = Label(frameImagen, image=tkimage, width=220, height=252).pack()
				ventanaGestorBingos.mainloop()

			else:
				messagebox.showerror("Error al Obtener","No se ha podido obtener un cartón para el código ingresado. ")	
	else:
		messagebox.showerror("Error de Bingo","No se han generado los cartones del bingo. ")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Inicia el juego validando cual modo de este es el escogido.
Restricciones: No valida restricciones.
'''
def comandoIniciarJuego():
	global opcionJuego_StringVar
	global premio
	global labelTipo
	global premioJuego
	global labelTotCartones
	global labelTotJugadores
	global tipoJuegoSeleccionado
	global btnCantar
	global btnIniciar

	valoresJuego=[]

	if(LDN.contarCartones()==0):
		messagebox.showerror("Error de Bingo","No se han generado los cartones del bingo. ")	
	else:
		if(opcionJuego_StringVar.get() =="" or premio.get()==""):
			messagebox.showwarning("Texto Vacío","Deben completarse todos los espacios.")
		else:	
			valoresJuego = LDN.obtenerValoresJuego()

			if(valoresJuego!=[-1]):
				if(valoresJuego[0]==0):
					messagebox.showwarning("Error de Juego","No se ha asignado ningún cartón. ")
					return
				elif(valoresJuego[1]==0):
					messagebox.showerror("Error de Juego","No se han generado los cartones del bingo. ")
					return
				elif(valoresJuego[2]==-1):
					resultado=messagebox.askquestion('Iniciar Juego','No se ha asignado todos los cartones. \n¿Desea iniciar el juego?')
					if (resultado=='no'):
						return	
				
				tipoJuegoSeleccionado=opcionJuego_StringVar.get()			
				labelTipo.configure(text="Tipo de juego: "+opcionJuego_StringVar.get())

				premioJuego.config(state="normal") 
				premioJuego.insert(0, premio.get())
				premioJuego.config(state="disabled")

				labelTotCartones.configure(text="Total de Cartones: "+str(valoresJuego[1]))
				labelTotJugadores.configure(text="Total de Jugadores: "+str(valoresJuego[0]))

				premio.delete(0, END)
				btnCantar.config(state="normal")
				btnIniciar.config(state="disabled")


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna 
Salidas: Reiniciar los valores la sección de gestión del juego y habilitar el inicio de un juego nuevo. 
Restricciones: No valida restricciones.  
'''
def comandoTerminarJuego():
	global txtNumCantados
	global labelTipo
	global premioJuego
	global labelTotCartones
	global labelTotJugadores
	global btnCantar
	global btnIniciar
	global numerosCantados

	numerosCantados=""
	txtNumCantados.config(state="normal") 
	txtNumCantados.delete(0.0, END)
	txtNumCantados.config(state="disabled")
	labelTipo.configure(text="Tipo de juego:") 
	premioJuego.config(state="normal") 
	premioJuego.delete(0, END)
	premioJuego.config(state="disabled")
	labelTotCartones.configure(text="Total de Cartones: ")
	labelTotJugadores.configure(text="Total de Jugadores: ")
	btnCantar.config(state="disabled")
	btnIniciar.config(state="normal")


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna 
Salidas: Se actualiza el campo de números en el apartado de los numeros cantados,
         en caso de existir un ganador del modo de juego escogido saltará un anuncio 
         indicando los identificadoeres de los cartones ganadores. 
Restricciones: No valida restricciones 
'''
def comandoCantarNumero():
	global numerosCantados
	
	ganadores=[]
	numeroCantado = LDN.cantarNumero()

	if(numeroCantado == -2):
		messagebox.showwarning("Error al Cantar","Se han cantado todos los números posibles.")
	elif(numeroCantado != -1):
		numerosCantados = numerosCantados + " " +str(numeroCantado)

		txtNumCantados.config(state="normal") 
		txtNumCantados.delete(0.0, END)
		txtNumCantados.insert(END, numerosCantados)
		txtNumCantados.config(state="disabled")

		validarGanadores()

	else:
		messagebox.showerror("Error al Cantar","Se ha producido un error al cantar el número.")


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Valida si alguno de los cartones cumple con las condiciones de gane del tipo de juego seleccionado,
		 y muestra un mensaje con código de este cartón.
Restricciones: No valida restricciones
'''
def validarGanadores():
	global tipoJuegoSeleccionado
	global btnCantar
	global premioJuego

	valorRetorno=0

	ganadores = LDN.validarTipoJuego(tipoJuegoSeleccionado)

	if(ganadores==[-1]):
		messagebox.showerror("Error al Validar","Se ha producido un error al validar el número cantado.")
	elif(ganadores!=[]):
		identificadores=""
		for x in range(0,len(ganadores)):
			identificadores=identificadores+" "+str(ganadores[x])
		messagebox.showinfo("Cartones Ganadores","¡Felicidades! Ha resultado ganador el cartón(es): \n"+identificadores)

		premioJuego.config(state="normal") 
		premio=premioJuego.get()
		premioJuego.config(state="disabled")

		valorRetorno = LDN.notificarGanadores(ganadores, premio)

		if(valorRetorno==1):
			messagebox.showinfo("Notificar Ganadores","Se ha enviado una notificación al correo del ganador(es)")
		elif(valorRetorno==-2):
			messagebox.showinfo("Notificar Ganadores","El cartón ganador na había sido asignado a ningún jugador.")

		btnCantar.config(state="disabled")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: El nombre de un jugador, su correo y su cedula 
Salidas: En el caso de haber guardado de forma correcta los datos saltara un mensaje indicando,
         cuando no suceda un error saltará una alerta del error 
Restricciones: El correo debe ser valido y la en la cedula solo puede ingresar números 
'''
def comandoRegistrarJugador():
	global nombreJugador
	global cedulaJugador
	global correoJugador

	nombre=nombreJugador.get()
	cedula=cedulaJugador.get()
	correo=correoJugador.get()

	if(nombre=="" or cedula=="" or correo==""):
		messagebox.showwarning("Texto Vacío","Deben completarse todos los espacios.")	
	else:
		if(LDN.validarCedula(cedula)==1 or esNumero(cedula)==False):
			messagebox.showwarning("Error en Cédula","El valor ingresado para la cédula no es válido o ya ha sido registrado.")	 
		elif(LDN.validarCorreo(correo)==False):
			messagebox.showwarning("Error en Correo","El valor ingresado para el correo no es una dirección válida.")
		else:			
			valorRetorno = LDN.agregarJugadorCSV(nombre, cedula, correo)

			if(valorRetorno == 1):
				messagebox.showinfo("Jugador Agregado","Los datos del jugador se han guardado con exito.")
				nombreJugador.delete(0,END)
				cedulaJugador.delete(0,END)
				correoJugador.delete(0,END)					
			else:
				messagebox.showerror("Error al Guardar","Se ha producido un error al guardar los datos.")	  


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Un correo electronico
Salidas: Se enviará un correo con la cantidad de cartones ingresados en el apartado de Enviar Cartón a Jugador Registrado
Restricciones:
'''
def comandoEnviarCartones():
	global cantidadEnviar
	global cedulaEnviar

	cantidad=0
	cartonesPorAsignar=[]

	if(LDN.contarCartones()==0):
		messagebox.showerror("Error de Bingo","No se han generado los cartones del bingo. ")	
	else:
		if(cantidadEnviar.get() =="" or cedulaEnviar.get()==""):
			messagebox.showwarning("Texto Vacío","Deben completarse todos los espacios.")			
		elif(esNumero(cantidadEnviar.get())==False or int(cantidadEnviar.get())<0):
			messagebox.showerror("Cantidad no válida","La cantidad debe ser un número entre 1 y el total de cartones generados.")
		else:
			cedula=cedulaEnviar.get()
			cantidad=int(cantidadEnviar.get())

			if(LDN.validarCedula(cedula)==1):
				cartonesPorAsignar=LDN.asignarCartones(cantidad, cedula)
				
				if(cartonesPorAsignar==[-1]):
					messagebox.showerror("Error en Cartones","Se ha producido un error al asignar los cartones.")
				elif(cartonesPorAsignar==[-2]):
					messagebox.showerror("Error en Cartones","No se tienen cartones suficientes disponibles para asignar.")
				else:			
					if(LDN.enviarCartones(cedula, cartonesPorAsignar)==1):
						messagebox.showinfo("Cartones Enviados","Los cartones ha sido enviados al jugador.")
						cantidadEnviar.delete(0,END) 
						cedulaEnviar.delete(0,END)	
			else:
				messagebox.showerror("Error en Cédula","El valor ingresado para la cédula, no corresponde a ningún jugador.")	 


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se configuran los objetos de la ventana principal del programa y se invoca.
Restricciones: Ninguna
'''
def inicio():

	global cantidadCartones
	global codigoCarton
	global opcionJuego_StringVar
	global premio
	global labelTipo
	global premioJuego
	global txtNumCantados
	global nombreJugador
	global cedulaJugador
	global correoJugador
	global cantidadEnviar
	global cedulaEnviar
	global frameImagen
	global txtNumCantados
	global ventanaGestorBingos
	global subFrConsultar
	global labelTotCartones
	global labelTotJugadores
	global btnCantar
	global btnIniciar
	global labelAsignacion

	ventanaGestorBingos = Tk()
	ventanaGestorBingos.title("Gestor de Bingos")
	ventanaGestorBingos.iconbitmap("Recursos/icon.ico")
	ventanaGestorBingos.config(bg="#F8F9FA")
	ventanaGestorBingos.resizable(False, False) 

	tabControl = ttk.Notebook(ventanaGestorBingos)

	frGestBingo = Frame(tabControl, bg="#F8F9FA")
	frGestBingo.rowconfigure((0,1), minsize=100, weight=1)
	frGestBingo.columnconfigure(0, minsize=800, weight=1)

	frJuego = Frame(tabControl, bg="#F8F9FA")
	frJuego.rowconfigure((0,1), minsize=100, weight=1)
	frJuego.columnconfigure(0, minsize=800, weight=1)

	frGestJugador = Frame(tabControl, bg="#F8F9FA")
	frGestJugador.rowconfigure((0,1), minsize=100, weight=1)
	frGestJugador.columnconfigure(0, minsize=800, weight=1)

	# #Seccion para generar los cartones---------------------------------------------------------------------#
	subFrGenerar = Frame(frGestBingo, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrGenerar.rowconfigure((0,1,2), weight=1)
	subFrGenerar.columnconfigure((0,1,2), weight=1)
	
	label1 = Label(subFrGenerar, text="Generar Cartones de Bingo ", bg="#F8F9FA", fg="#ED7D31", font=("Calibri", 16, "bold"))
	label1.grid(row=0, column=0, columnspan = 2, sticky="w", padx=5, pady=5)

	label1_2 = Label(subFrGenerar, text="Cantidad: ", bg="#F8F9FA", fg="#ED7D31", font=("Calibri", 14))
	label1_2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

	cantidadCartones_StringVar = StringVar()
	cantidadCartones = Entry(subFrGenerar, bg="#ffffff", fg="#000000", textvariable=cantidadCartones_StringVar, width="20", font=("Calibri", 18))
	cantidadCartones.grid(row=1, column=1, padx=5, pady=5)

	btnGenerar = Button(subFrGenerar, text="Generar", command=comandoGenerarCartones, bg="#ED7D31", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnGenerar.grid(row=1, column=2, padx=5, pady=5)

	subFrGenerar.grid(row=0, column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para consultar los cartones-----------------------------------------------------------------#
	subFrConsultar = Frame(frGestBingo, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrConsultar.rowconfigure((0,3), weight=1)
	subFrConsultar.columnconfigure((0,1,2), weight=1)

	label2 = Label(subFrConsultar, text="Consultar Cartón: ", bg="#F8F9FA", fg="#ED7D31", font=("Calibri", 16, "bold"))
	label2.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)
	
	label2_2 = Label(subFrConsultar, text="Identificación: ", bg="#F8F9FA", fg="#ED7D31", font=("Calibri", 14))
	label2_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	codigoCarton_StringVar = StringVar()
	codigoCarton = Entry(subFrConsultar, bg="#ffffff", fg="#000000", textvariable=codigoCarton_StringVar, width="20", font=("Calibri", 18))
	codigoCarton.grid(row=1,column=1, padx=5, pady=5)

	btnMostrar = Button(subFrConsultar, text="Mostrar", command=comandoMostrarCarton, bg="#ED7D31", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnMostrar.grid(row=1, column=2, padx=5, pady=5)

	frameImagen = Frame(subFrConsultar, width=220, height=252)
	frameImagen.grid(row=2, column=1, padx=5, pady=5)

	img = Image.open('Recursos\PlantillaCarton.png')
	img = img.resize((220, 252), Image.BICUBIC)
	tkimage = ImageTk.PhotoImage(img)
	labelImage = Label(frameImagen, image=tkimage, width=220, height=252).pack()

	label2_3 = Label(subFrConsultar, text="Asignación: ", bg="#F8F9FA", fg="#ED7D31", font=("Calibri", 14))
	label2_3.grid(row=3,column=0, sticky="e", padx=5, pady=5)

	labelAsignacion = Label(subFrConsultar, text="", bg="#F8F9FA", fg="#000000", font=("Calibri", 14))
	labelAsignacion.grid(row=3,column=1, sticky="w", padx=5, pady=5)

	subFrConsultar.grid(row=1,column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para iniciar juego-------------------------------------------------------------------------#
	subFrIniciar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrConsultar.rowconfigure((0,1,2), weight=1)
	subFrConsultar.columnconfigure((0,1,2,3), weight=1)
	
	label3 = Label(subFrIniciar, text="Iniciar juego de Bingo: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 16, "bold"))
	label3.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)

	label3_2 = Label(subFrIniciar, text="Configuración: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	label3_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	opciones = ( "Jugar en X", "Cuatro esquinas", "Cartón lleno", "Jugar en Z" ) 

	opcionJuego_StringVar = StringVar()
	opcionJuego = OptionMenu(subFrIniciar, opcionJuego_StringVar, *opciones)
	opcionJuego.config(width=15, bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14,))
	opcionJuego.grid(row=1,column=1, padx=5, pady=5)
	opcionJuego_StringVar.set("Jugar en X")

	label3_3 = Label(subFrIniciar, text="Premio: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	label3_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	premio_StringVar = StringVar()
	premio = Entry(subFrIniciar, bg="#ffffff", fg="#000000", textvariable=premio_StringVar, width="20", font=("Calibri", 14,))
	premio.grid(row=1,column=3, padx=5, pady=5)

	btnIniciar = Button(subFrIniciar, text="Iniciar", command=comandoIniciarJuego, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnIniciar.grid(row=2, column=1, columnspan = 2, sticky="e", padx=5, pady=5)

	subFrIniciar.grid(row=0,column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para visualizar juego----------------------------------------------------------------------#
	subFrJugar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrJugar.rowconfigure((0,1,2,3), weight=1)
	subFrJugar.columnconfigure((0,1,2,3), weight=1)

	labelTipo = Label(subFrJugar, text="Tipo de juego: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	labelTipo.grid(row=0,column=0, sticky="w", padx=5)

	label4_2 = Label(subFrJugar, text="Premio: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	label4_2.grid(row=0,column=2, sticky="e", padx=5, pady=5)

	premioJuego_StringVar = StringVar()
	premioJuego = Entry(subFrJugar, bg="#ffffff", fg="#000000", textvariable=premioJuego_StringVar, state="disabled",  width="20", font=("Calibri", 14))
	premioJuego.grid(row=0,column=3, padx=5, pady=5)

	btnCantar = Button(subFrJugar, text="Cantar Número", command=comandoCantarNumero, bg="#2196f3", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 14))
	btnCantar.grid(row=1, column=1, columnspan = 2, padx=5, pady=5)

	frameTexto = Frame(subFrJugar, width=75, height=50)

	txtNumCantados = Text(frameTexto)

	scrollbarTexto = Scrollbar(frameTexto)
	txtNumCantados = Text(frameTexto, width=70, height=5)
	scrollbarTexto.pack(side=RIGHT,fill=Y)
	txtNumCantados.pack(side=LEFT, fill=Y)
	scrollbarTexto.config(command=txtNumCantados.yview)
	txtNumCantados.config(yscrollcommand=scrollbarTexto.set, state="disabled")

	frameTexto.grid(row=2, column=0, columnspan = 5, padx=10, pady=10)

	labelTotCartones = Label(subFrJugar, text="Total de Cartones: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 11))
	labelTotCartones.grid(row=3,column=0, sticky="w", padx=5, pady=5)

	btnTerminar = Button(subFrJugar, text="Terminar", command=comandoTerminarJuego, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnTerminar.grid(row=3, column=2, padx=5, pady=5)

	labelTotJugadores = Label(subFrJugar, text="Total de Jugadores: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 11))
	labelTotJugadores.grid(row=3,column=3, sticky="e", padx=5, pady=5)

	subFrJugar.grid(row=1,column=0, padx=15, pady=15, sticky="nsew")

	# #Seccion para registrar jugadores--------------------------------------------------------------------#
	subFrRegistrar = Frame(frGestJugador, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrRegistrar.rowconfigure((0,1,2), weight=1)
	subFrRegistrar.columnconfigure((0,1,2,3), weight=1)

	label5 = Label(subFrRegistrar, text="Registrar jugador: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 16, "bold"))
	label5.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)

	label5_2 = Label(subFrRegistrar, text="Nombre: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label5_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	nombreJugador_StringVar = StringVar()
	nombreJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#000000", textvariable=nombreJugador_StringVar, width="25", font=("Calibri", 14))
	nombreJugador.grid(row=1,column=1, sticky="w",padx=5, pady=5)

	label5_3 = Label(subFrRegistrar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label5_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	cedulaJugador_StringVar = StringVar()
	cedulaJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#000000", textvariable=cedulaJugador_StringVar, width="15", font=("Calibri", 14))
	cedulaJugador.grid(row=1,column=3, sticky="w", padx=5, pady=5)

	label5_4 = Label(subFrRegistrar, text="Correo: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label5_4.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	correoJugador_StringVar = StringVar()
	correoJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#000000", textvariable=correoJugador_StringVar, width="25", font=("Calibri", 14))
	correoJugador.grid(row=2,column=1, sticky="w", padx=5, pady=5)

	btnGuardar = Button(subFrRegistrar, text="Guardar", command=comandoRegistrarJugador, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnGuardar.grid(row=2, column=3, sticky="w", padx=5, pady=5)

	subFrRegistrar.grid(row=0,column=0, padx=15, pady=15, sticky="nsew")

	# #Seccion para enviar cartones-----------------------------------------------------------------------#
	subFrEnviar = Frame(frGestJugador, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrEnviar.rowconfigure((0,1,2), weight=1)
	subFrEnviar.columnconfigure((0,1,2,3), weight=1)

	label6 = Label(subFrEnviar, text="Enviar cartón a jugador registrado: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 16, "bold"))
	label6.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)
	
	label6_2 = Label(subFrEnviar, text="Cantidad: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label6_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	cantidadEnviar_StringVar = StringVar()
	cantidadEnviar = Entry(subFrEnviar, bg="#ffffff", fg="#000000", textvariable=cantidadEnviar_StringVar, width="25", font=("Calibri", 14))
	cantidadEnviar.grid(row=1,column=1, sticky="w",padx=5, pady=5)

	label6_3 = Label(subFrEnviar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label6_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	cedulaEnviar_StringVar = StringVar()
	cedulaEnviar = Entry(subFrEnviar, bg="#ffffff", fg="#000000", textvariable=cedulaEnviar_StringVar, width="15", font=("Calibri", 14))
	cedulaEnviar.grid(row=1,column=3, sticky="w", padx=5, pady=5)

	btnEnviar = Button(subFrEnviar, text="Enviar Cartones Digitales", command=comandoEnviarCartones, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnEnviar.grid(row=2, column=3, sticky="w", padx=5, pady=5)

	subFrEnviar.grid(row=1,column=0, padx=15, pady=15, sticky="nsew")

	# menuBar = Menu(ventanaGestorBingos)
	# menuSuperiorB = Menu(menuBar, tearoff=0)
	# menuSuperiorB.add_command(label="Manual de Usuario", command=comandoTemporal)
	# menuSuperiorB.add_command(label="Acerca de", command=comandoTemporal)
	# menuBar.add_cascade(label="Ayuda", menu=comandoTemporal)
	# ventanaGestorBingos.config(menu=comandoTemporal)

	# #Agregar las pestañas
	tabControl.add(frGestBingo, text ='Gestionar Cartones') 
	tabControl.add(frGestJugador, text ='Gestionar Jugadores')
	tabControl.add(frJuego, text ='Juego Nuevo') 
	tabControl.pack(expand = 1, fill ="both") 

	ventanaGestorBingos.mainloop()

inicio()