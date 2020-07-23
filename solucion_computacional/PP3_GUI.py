from tkinter import *                   
from tkinter import ttk 

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:
Salidas:
Restricciones:
'''
def comandoTemporal():
    print("comandoTemporal")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se configuran los objetos de la ventana principal del programa y se invoca.
Restricciones: Ninguna
'''
def inicio():

	# global txtDocumento

	ventanaGestorBingos = Tk()
	ventanaGestorBingos.title("Gestor de Bingos")
	ventanaGestorBingos.geometry("650x400")
	#ventanaGestorBingos.iconbitmap("Recursos/icon.ico")

	ventanaGestorBingos.config(bg="#F8F9FA")
	# ventanaGestorBingos.resizable(width=650, height=000)
	# ventanaGestorBingos.resizable(width=0, height=0) 

	tabControl = ttk.Notebook(ventanaGestorBingos)

	frGestBingo = Frame(tabControl, bg="#F8F9FA")
	frJuego = Frame(tabControl, bg="#F8F9FA")
	frGestJugador = Frame(tabControl, bg="#F8F9FA")

	#Seccion para generar los cartones---------------------------------------------------------------------#
	subFrGenerar = Frame(frGestBingo, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	
	label1 = Label(subFrGenerar, text="Generar Cartones de Bingo ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14, "bold"))
	label1.grid(row=0,column=0, padx=5, pady=5)

	label1_2 = Label(subFrGenerar, text="Cantidad: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 12))
	label1_2.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	cantidadCartones_StringVar = StringVar()
	cantidadCartones = Entry(subFrGenerar, bg="#ffffff", fg="#29a891", textvariable=cantidadCartones_StringVar, width="35")
	cantidadCartones.grid(row=2,column=1, padx=5, pady=5)

	btnGenerar = Button(subFrGenerar, text="Generar", command=comandoTemporal, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnGenerar.grid(row=2, column=2, padx=5, pady=5)

	subFrGenerar.grid(row=0,column=0, sticky="nsew", padx=15, pady=15)

	#Seccion para consultar los cartones-----------------------------------------------------------------#
	subFrConsultar = Frame(frGestBingo, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	
	label2 = Label(subFrConsultar, text="Consultar Cartón: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14, "bold"))
	label2.grid(row=0,column=0, sticky="w", padx=5)
	
	label2_2 = Label(subFrConsultar, text="Identificación: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 12))
	label2_2.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	codigoCarton_StringVar = StringVar()
	codigoCarton = Entry(subFrConsultar, bg="#ffffff", fg="#29a891", textvariable=codigoCarton_StringVar, width="35")
	codigoCarton.grid(row=2,column=1, padx=5, pady=5)

	btnMostrar = Button(subFrConsultar, text="Generar", command=comandoTemporal, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnMostrar.grid(row=2, column=2, padx=5, pady=5)

	subFrConsultar.grid(row=1,column=0, sticky="nsew", padx=15, pady=15)

	#Seccion para registrar jugadores--------------------------------------------------------------------#
	subFrRegistrar = Frame(frGestJugador, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	label3 = Label(subFrRegistrar, text="Registrar jugador: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12, "bold"))
	label3.grid(row=0,column=0, sticky="w", padx=5)

	label3_2 = Label(subFrRegistrar, text="Nombre: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12))
	label3_2.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	nombreJugador_StringVar = StringVar()
	nombreJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=nombreJugador_StringVar, width="40")
	nombreJugador.grid(row=2,column=1, padx=5, pady=5)

	label3_3 = Label(subFrRegistrar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12))
	label3_3.grid(row=2,column=2, sticky="e", padx=5, pady=5)

	cedulaJugador_StringVar = StringVar()
	cedulaJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=cedulaJugador_StringVar, width="20")
	cedulaJugador.grid(row=2,column=3, padx=5, pady=5)

	label3_4 = Label(subFrRegistrar, text="Correo: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12))
	label3_4.grid(row=3,column=0, sticky="e", padx=5, pady=5)

	correoJugador_StringVar = StringVar()
	correoJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=correoJugador_StringVar, width="40")
	correoJugador.grid(row=3,column=1, padx=5, pady=5)

	btnGuardar = Button(subFrRegistrar, text="Guardar", command=comandoTemporal, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnGuardar.grid(row=3, column=3, sticky="e", padx=5, pady=5)

	subFrRegistrar.grid(row=2,column=0, sticky="nsew", padx=15, pady=15)

	#Seccion para enviar cartones-----------------------------------------------------------------------#
	subFrEnviar = Frame(frGestJugador, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	
	label4 = Label(subFrEnviar, text="Enviar cartón a jugador registrado: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12, "bold"))
	label4.grid(row=0,column=0, sticky="w", padx=5)

	label4_2 = Label(subFrEnviar, text="Cantidad: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12))
	label4_2.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	nombreJugador_StringVar = StringVar()
	nombreJugador = Entry(subFrEnviar, bg="#ffffff", fg="#29a891", textvariable=nombreJugador_StringVar, width="35")
	nombreJugador.grid(row=2,column=1, padx=5, pady=5)

	label4_3 = Label(subFrEnviar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 12))
	label4_3.grid(row=3,column=0, sticky="e", padx=5, pady=5)

	cedulaJugador_StringVar = StringVar()
	cedulaJugador = Entry(subFrEnviar, bg="#ffffff", fg="#29a891", textvariable=cedulaJugador_StringVar, width="35")
	cedulaJugador.grid(row=3,column=1, padx=5, pady=5)

	btnGuardar = Button(subFrEnviar, text="Guardar", command=comandoTemporal, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnGuardar.grid(row=3, column=3, sticky="e", padx=5, pady=5)

	subFrEnviar.grid(row=3,column=0, sticky="nsew", padx=15, pady=15)

	#Seccion para iniciar juego-------------------------------------------------------------------------#
	subFrIniciar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge") 
	
	label5 = Label(subFrIniciar, text="Iniciar juego de Bingo: ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12, "bold"))
	label5.grid(row=0,column=0, sticky="w", padx=5)

	label5_2 = Label(subFrIniciar, text="Cantidad: ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12))
	label5_2.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	opcionJuego = [ "Jugar en X", "Cuatro esquinas", "Cartón lleno", "Jugar en Z" ] 

	opcionJuego_StringVar = StringVar()
	opcionJuego = OptionMenu(subFrIniciar, opcionJuego_StringVar, *opcionJuego)
	opcionJuego.config(width=20, bg="#F8F9FA", fg="#f44336", font=("Calibri", 12,))
	opcionJuego.grid(row=2,column=1, padx=5, pady=5)

	label5_3 = Label(subFrIniciar, text="Premio: ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12))
	label5_3.grid(row=3,column=0, sticky="e", padx=5, pady=5)

	premio_StringVar = StringVar()
	premio = Entry(subFrIniciar, bg="#ffffff", fg="#29a891", textvariable=premio_StringVar, width="35")
	premio.grid(row=3,column=1, padx=5, pady=5)

	btnIniciar = Button(subFrIniciar, text="Iniciar", command=comandoTemporal, bg="#f44336", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnIniciar.grid(row=3, column=3, sticky="e", padx=5, pady=5)

	subFrIniciar.grid(row=4,column=0, sticky="nsew", padx=15, pady=15)

	#Seccion para visualizar juego----------------------------------------------------------------------#
	subFrJugar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge")

	label6 = Label(subFrJugar, text="Tipo de juego: ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12, "bold"))
	label6.grid(row=0,column=0, sticky="w", padx=5)

	label6_2 = Label(subFrJugar, text="Cuatro Esquinas ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12))
	label6_2.grid(row=0,column=1, sticky="e", padx=5, pady=5)

	label6_3 = Label(subFrJugar, text="Premio: ", bg="#F8F9FA", fg="#f44336", font=("Calibri", 12))
	label6_3.grid(row=0,column=3, sticky="e", padx=5, pady=5)

	premioJuego_StringVar = StringVar()
	premioJuego = Entry(subFrJugar, bg="#ffffff", fg="#29a891", textvariable=premioJuego_StringVar, width="35")
	premioJuego.grid(row=0,column=4, padx=5, pady=5)

	btnCantar = Button(subFrJugar, text="Cantar Número", command=comandoTemporal, bg="#f44336", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	btnCantar.grid(row=1, column=2, padx=5, pady=5)

	frameTexto = Frame(subFrJugar, width=75, height=50)

	txtNumCantados = Text(frameTexto)

	scrollbarTexto = Scrollbar(frameTexto)
	txtNumCantados = Text(frameTexto, width=35, height=10)
	scrollbarTexto.pack(side=RIGHT,fill=Y)
	txtNumCantados.pack(side=LEFT, fill=Y)
	scrollbarTexto.config(command=txtNumCantados.yview)
	txtNumCantados.config(yscrollcommand=scrollbarTexto.set)

	frameTexto.grid(row=2,  padx=10, pady=10)

	subFrJugar.grid(row=5,column=0, sticky="nsew", padx=15, pady=15)

	# menuBar = Menu(ventanaGestorBingos)
	# menuSuperiorB = Menu(menuBar, tearoff=0)
	# menuSuperiorB.add_command(label="Manual de Usuario", command=comandoTemporal)
	# menuSuperiorB.add_command(label="Acerca de", command=comandoTemporal)
	# menuBar.add_cascade(label="Ayuda", menu=comandoTemporal)
	# ventanaGestorBingos.config(menu=comandoTemporal)

	#Agregar las pestañas
	tabControl.add(frGestBingo, text ='Gestionar Juego', sticky="nsew") 
	tabControl.add(frJuego, text ='Juego Nuevo', sticky="nsew") 
	tabControl.add(frGestJugador, text ='Gestionar Jugadores', sticky="nsew") 
	tabControl.pack(expand = 1, fill ="both") 

	ventanaGestorBingos.mainloop()

inicio()