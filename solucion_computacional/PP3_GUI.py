from tkinter import *                   
from tkinter import ttk 

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
	#ventanaGestorBingos.iconbitmap("Recursos/icon.ico")

	ventanaGestorBingos.config(bg="#F8F9FA")
	# ventanaGestorBingos.resizable(width=0, height=0) 

	tabControl = ttk.Notebook(ventanaGestorBingos) 

	frGestion = Frame(tabControl, bg="#F8F9FA", height="600", width="800")
	frJuego = Frame(tabControl, bg="#F8F9FA", height="600", width="800")

	#Seccion para generar los cartones
	subFrGenerar = Frame(frGestion, bg="#F8F9FA", height="200", width="800")
	label1 = Label(subFrGenerar, text="Generar Cartones de Bingo: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label1.grid(row=0,column=0, sticky="w", padx=5)
	subFrGenerar.grid(row=0,column=0, padx=5)

	#Seccion para consultar los cartones
	subFrConsultar = Frame(frGestion, bg="#F8F9FA", height="200", width="800")
	label2 = Label(subFrConsultar, text="Consultar Cartón: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label2.grid(row=0,column=0, sticky="w", padx=5)
	subFrConsultar.grid(row=1,column=0, padx=5)

	#Seccion para registrar jugadores
	subFrRegistrar = Frame(frGestion, bg="#F8F9FA", height="200", width="800")
	label3 = Label(subFrRegistrar, text="Registrar jugador: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label3.grid(row=0,column=0, sticky="w", padx=5)
	subFrRegistrar.grid(row=2,column=0, padx=5)

	#Seccion para enviar cartones
	subFrEnviar = Frame(frGestion, bg="#F8F9FA", height="200", width="800")
	label4 = Label(subFrEnviar, text="Enviar cartón a jugador registrado: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label4.grid(row=0,column=0, sticky="w", padx=5)
	subFrEnviar.grid(row=3,column=0, padx=5)

	#Seccion para iniciar juego
	subFrIniciar = Frame(frJuego, bg="#F8F9FA", height="400", width="800") 
	label5 = Label(subFrIniciar, text="Iniciar juego de Bingo: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label5.grid(row=0,column=0, sticky="w", padx=5)
	subFrIniciar.grid(row=4,column=0, padx=5)

	#Seccion para visualizar juego
	subFrJugar = Frame(frJuego, bg="#F8F9FA", height="400", width="800")
	label6 = Label(subFrJugar, text="Tipo de juego: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
	label6.grid(row=0,column=0, sticky="w", padx=5)
	subFrJugar.grid(row=5,column=0, padx=5)

	# frameTexto = Frame(frPrincipal, width=250, height=350)

	# txtDocumento = Text(frameTexto)

	# scrollbarTexto = Scrollbar(frameTexto)
	# txtDocumento = Text(frameTexto, width=70, height=25)
	# scrollbarTexto.pack(side=RIGHT,fill=Y)
	# txtDocumento.pack(side=LEFT, fill=Y)
	# scrollbarTexto.config(command=txtDocumento.yview)
	# txtDocumento.config(yscrollcommand=scrollbarTexto.set)

	# treeViewTokens = ttk.Treeview(frPrincipal) 

	# frBtnDocumento = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
	# btnAbrirArchivo = Button(frBtnDocumento, text="Abrir Archivo", command=comandoLeerArchivo, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	# btnAbrirArchivo.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
	# btnLimpiarTexto = Button(frBtnDocumento, text="Limpiar Texto", command=comandoReiniciarDocumento, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12)) 
	# btnLimpiarTexto.grid(row=0, column=1, sticky="ew", padx=5)

	# frBtnLista = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
	# btnTokenizar = Button(frBtnLista, text="Tokenizar", command=comandoTokenizarDocumento, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
	# btnTokenizar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
	# btnTraducir = Button(frBtnLista, text="Traducir", command=comandoTraducirTokens, bg="#0288d1", fg="#ffffff",  relief=GROOVE, font=("Calibri", 12))
	# btnTraducir.grid(row=0, column=1, sticky="ew", padx=5)

	# btnGenerarHtml = Button(frPrincipal, text="Generar HTML", command=comandoGenerarHTML, bg="#0288d1", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 12))

	# label1.grid(row=0,column=0, sticky="w", padx=5)
	# frameTexto.grid(row=1, column=0, sticky="ns", padx=10)
	# frBtnDocumento.grid(row=2, column=0, sticky="se", padx=5, pady=10)
	# label2.grid(row=0, column=1, sticky="w", padx=5)
	# treeViewTokens.grid(row=1, column=1, sticky="ns", padx=5)
	# frBtnLista.grid(row=2, column=1, sticky="e", padx=5, pady=10)
	# btnGenerarHtml.grid(row=1, column=2, sticky="n", padx=5)

	# frPrincipal.pack()

	# menuBar = Menu(ventanaGestorBingos)
	# menuSuperiorA = Menu(menuBar, tearoff=0)
	# menuSuperiorA.add_command(label="Abrir un archivo", command=comandoLeerArchivo)
	# menuSuperiorA.add_command(label="Borrar valores", command=reiniciarValores)
	# menuSuperiorA.add_command(label="Salir del programa", command=comandoSalir)
	# menuBar.add_cascade(label="Opciones", menu=menuSuperiorA)
	# menuSuperiorB = Menu(menuBar, tearoff=0)
	# menuSuperiorB.add_command(label="Manual de Usuario", command=comandoAbrirManual)
	# menuSuperiorB.add_command(label="Acerca de", command=comandoAcercaDe)
	# menuBar.add_cascade(label="Ayuda", menu=menuSuperiorB)
	# ventanaGestorBingos.config(menu=menuBar)



	#Agregar las pestañas
	tabControl.add(frGestion, text ='Gestionar Juego') 
	tabControl.add(frJuego, text ='Juego Nuevo') 
	tabControl.pack(expand = 1, fill ="both") 

	ventanaGestorBingos.mainloop()

inicio()