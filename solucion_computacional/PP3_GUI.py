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
	ventanaGestorBingos.geometry("800x500+250+5")
	ventanaGestorBingos.iconbitmap("Recursos/icon.ico")
	ventanaGestorBingos.rowconfigure(0, minsize=800, weight=1)
	ventanaGestorBingos.columnconfigure(0, minsize=500, weight=1)
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
	
	label1 = Label(subFrGenerar, text="Generar Cartones de Bingo ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 16, "bold"))
	label1.grid(row=0, column=0, columnspan = 2, sticky="w", padx=5, pady=5)

	label1_2 = Label(subFrGenerar, text="Cantidad: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	label1_2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

	cantidadCartones_StringVar = StringVar()
	cantidadCartones = Entry(subFrGenerar, bg="#ffffff", fg="#000000", textvariable=cantidadCartones_StringVar, width="20", font=("Calibri", 18))
	cantidadCartones.grid(row=1, column=1, padx=5, pady=5)

	btnGenerar = Button(subFrGenerar, text="Generar", command=comandoTemporal, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnGenerar.grid(row=1, column=2, padx=5, pady=5)

	subFrGenerar.grid(row=0, column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para consultar los cartones-----------------------------------------------------------------#
	subFrConsultar = Frame(frGestBingo, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrConsultar.rowconfigure((0,1), weight=1)
	subFrConsultar.columnconfigure((0,1,2), weight=1)

	label2 = Label(subFrConsultar, text="Consultar Cartón: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 16, "bold"))
	label2.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)
	
	label2_2 = Label(subFrConsultar, text="Identificación: ", bg="#F8F9FA", fg="#2196f3", font=("Calibri", 14))
	label2_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	codigoCarton_StringVar = StringVar()
	codigoCarton = Entry(subFrConsultar, bg="#ffffff", fg="#000000", textvariable=codigoCarton_StringVar, width="20", font=("Calibri", 18))
	codigoCarton.grid(row=1,column=1, padx=5, pady=5)

	btnMostrar = Button(subFrConsultar, text="Mostrar", command=comandoTemporal, bg="#2196f3", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnMostrar.grid(row=1, column=2, padx=5, pady=5)

	frameImagen = Frame(subFrConsultar, width=150, height=150)
	frameImagen.grid(row=2, column=1, padx=5, pady=5)

	subFrConsultar.grid(row=1,column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para iniciar juego-------------------------------------------------------------------------#
	subFrIniciar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrConsultar.rowconfigure((0,1,2), weight=1)
	subFrConsultar.columnconfigure((0,1,2,3), weight=1)
	
	label3 = Label(subFrIniciar, text="Iniciar juego de Bingo: ", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 16, "bold"))
	label3.grid(row=0,column=0, columnspan = 2, sticky="w", padx=5)

	label3_2 = Label(subFrIniciar, text="Configuración: ", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 14))
	label3_2.grid(row=1,column=0, sticky="e", padx=5, pady=5)

	opcionJuego = [ "Jugar en X", "Cuatro esquinas", "Cartón lleno", "Jugar en Z" ] 

	opcionJuego_StringVar = StringVar()
	opcionJuego = OptionMenu(subFrIniciar, opcionJuego_StringVar, *opcionJuego)
	opcionJuego.config(width=20, bg="#F8F9FA", fg="#e64a19", font=("Calibri", 14,))
	opcionJuego.grid(row=1,column=1, padx=5, pady=5)

	label3_3 = Label(subFrIniciar, text="Premio: ", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 14))
	label3_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	premio_StringVar = StringVar()
	premio = Entry(subFrIniciar, bg="#ffffff", fg="#29a891", textvariable=premio_StringVar, width="20", font=("Calibri", 14,))
	premio.grid(row=1,column=3, padx=5, pady=5)

	btnIniciar = Button(subFrIniciar, text="Iniciar", command=comandoTemporal, bg="#e64a19", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnIniciar.grid(row=2, column=1, columnspan = 2, sticky="e", padx=5, pady=5)

	subFrIniciar.grid(row=0,column=0, padx=15, sticky="nsew", pady=15)

	# #Seccion para visualizar juego----------------------------------------------------------------------#
	subFrJugar = Frame(frJuego, bg="#F8F9FA", borderwidth = 3, relief="ridge")
	subFrJugar.rowconfigure((0,1,2,3), weight=1)
	subFrJugar.columnconfigure((0,1,2,3), weight=1)

	label4 = Label(subFrJugar, text="Tipo de juego: Cuatro Esquinas", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 14))
	label4.grid(row=0,column=0, sticky="w", padx=5)

	label4_2 = Label(subFrJugar, text="Premio: ", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 14))
	label4_2.grid(row=0,column=2, sticky="e", padx=5, pady=5)

	premioJuego_StringVar = StringVar()
	premioJuego = Entry(subFrJugar, bg="#ffffff", fg="#29a891", textvariable=premioJuego_StringVar, width="20", font=("Calibri", 14))
	premioJuego.grid(row=0,column=3, padx=5, pady=5)

	btnCantar = Button(subFrJugar, text="Cantar Número", command=comandoTemporal, bg="#e64a19", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnCantar.grid(row=1, column=1, columnspan = 2, padx=5, pady=5)

	frameTexto = Frame(subFrJugar, width=75, height=50)

	txtNumCantados = Text(frameTexto)

	scrollbarTexto = Scrollbar(frameTexto)
	txtNumCantados = Text(frameTexto, width=70, height=5)
	scrollbarTexto.pack(side=RIGHT,fill=Y)
	txtNumCantados.pack(side=LEFT, fill=Y)
	scrollbarTexto.config(command=txtNumCantados.yview)
	txtNumCantados.config(yscrollcommand=scrollbarTexto.set)

	frameTexto.grid(row=2, column=0, columnspan = 5, padx=10, pady=10)

	label4_3 = Label(subFrJugar, text="Total de Cartones: 500", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 11))
	label4_3.grid(row=3,column=0, sticky="w", padx=5, pady=5)

	label4_4 = Label(subFrJugar, text="Total de Jugadores: 41", bg="#F8F9FA", fg="#e64a19", font=("Calibri", 11))
	label4_4.grid(row=3,column=3, sticky="e", padx=5, pady=5)

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
	nombreJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=nombreJugador_StringVar, width="25", font=("Calibri", 14))
	nombreJugador.grid(row=1,column=1, sticky="w",padx=5, pady=5)

	label5_3 = Label(subFrRegistrar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label5_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	cedulaJugador_StringVar = StringVar()
	cedulaJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=cedulaJugador_StringVar, width="15", font=("Calibri", 14))
	cedulaJugador.grid(row=1,column=3, sticky="w", padx=5, pady=5)

	label5_4 = Label(subFrRegistrar, text="Correo: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label5_4.grid(row=2,column=0, sticky="e", padx=5, pady=5)

	correoJugador_StringVar = StringVar()
	correoJugador = Entry(subFrRegistrar, bg="#ffffff", fg="#29a891", textvariable=correoJugador_StringVar, width="25", font=("Calibri", 14))
	correoJugador.grid(row=2,column=1, sticky="w", padx=5, pady=5)

	btnGuardar = Button(subFrRegistrar, text="Guardar", command=comandoTemporal, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
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
	cantidadEnviar = Entry(subFrEnviar, bg="#ffffff", fg="#29a891", textvariable=cantidadEnviar_StringVar, width="25", font=("Calibri", 14))
	cantidadEnviar.grid(row=1,column=1, sticky="w",padx=5, pady=5)

	label6_3 = Label(subFrEnviar, text="Cédula: ", bg="#F8F9FA", fg="#4caf50", font=("Calibri", 14))
	label6_3.grid(row=1,column=2, sticky="e", padx=5, pady=5)

	cedulaEnviar_StringVar = StringVar()
	cedulaEnviar = Entry(subFrEnviar, bg="#ffffff", fg="#29a891", textvariable=cedulaEnviar_StringVar, width="15", font=("Calibri", 14))
	cedulaEnviar.grid(row=1,column=3, sticky="w", padx=5, pady=5)

	btnEnviar = Button(subFrEnviar, text="Enviar Cartones Digitales", command=comandoTemporal, bg="#4caf50", fg="#ffffff", relief=GROOVE, font=("Calibri", 14))
	btnEnviar.grid(row=2, column=3, sticky="w", padx=5, pady=5)

	subFrEnviar.grid(row=1,column=0, padx=15, pady=15, sticky="nsew")

	# menuBar = Menu(ventanaGestorBingos)
	# menuSuperiorB = Menu(menuBar, tearoff=0)
	# menuSuperiorB.add_command(label="Manual de Usuario", command=comandoTemporal)
	# menuSuperiorB.add_command(label="Acerca de", command=comandoTemporal)
	# menuBar.add_cascade(label="Ayuda", menu=comandoTemporal)
	# ventanaGestorBingos.config(menu=comandoTemporal)

	# #Agregar las pestañas
	tabControl.add(frGestBingo, text ='Gestionar Juego') 
	tabControl.add(frJuego, text ='Juego Nuevo') 
	tabControl.add(frGestJugador, text ='Gestionar Jugadores') 
	tabControl.pack(expand = 1, fill ="both") 

	ventanaGestorBingos.mainloop()

inicio()