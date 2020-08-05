 
# from PIL import Image, ImageDraw, ImageFont

# def generarImagenCarton(cartonBingo): 
	
# 	cartonBase = Image.open('PlantillaCarton.png')
# 	draw = ImageDraw.Draw(cartonBase)
# 	fuenteNumeros = ImageFont.truetype('arial.ttf', size=45)
# 	fuenteCodigo = ImageFont.truetype('arial.ttf', size=35)
# 	color = 'rgb(0, 0, 0)'
	
# 	x=30
# 	y=165
# 	potencia=1

# 	matriz=cartonBingo[:-1]

# 	#Anotar los numeros de la matriz en la imagen.
# 	for i in range(0,len(matriz[0])):
# 		for j in range(0,len(matriz)):
# 			numero=str(cartonBingo[i][j])
# 			draw.text((x, y), numero, fill=color, font=fuenteNumeros)
# 			x+=110
# 		y=165+(85*potencia)-3
# 		potencia+=1
# 		x=30

# 	# draw.text((30, 165), "1", fill=color, font=fuenteNumeros) 
# 	# draw.text((140, 165), "2", fill=color, font=fuenteNumeros) 
# 	# draw.text((250, 165), "3", fill=color, font=fuenteNumeros) 
# 	# draw.text((360, 165), "4", fill=color, font=fuenteNumeros) 
# 	# draw.text((470, 165), "5", fill=color, font=fuenteNumeros) 
	
# 	# draw.text((30, 165+(85*1)-3), "6", fill=color, font=fuenteNumeros) 
# 	# draw.text((30, 165+(85*2)-3), "7", fill=color, font=fuenteNumeros)
# 	# draw.text((30, 165+(85*3)-3), "8", fill=color, font=fuenteNumeros)  
# 	# draw.text((30, 165+(85*4)-3), "9", fill=color, font=fuenteNumeros) 

# 	#Anotar el ID al final de la imagen.	
# 	draw.text((215, 585), cartonBingo[5], fill=color, font=fuenteCodigo) 

# 	cartonBase.save(cartonBingo[5]+'.png')

# #Coordenadas en X = 30, 140, 250, 360, 470
# #Coordenadas en Y = 165, 245, 325, 405, 485


# def imprimirMatriz(lista):
# 	for i in lista:
# 	    for j in i:
# 	        print(j, end=" ")
# 	    print()


# import smtplib, ssl

# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "proyectoBingo3@gmail.com"
# receiver_email = "josealt2197@gmail.com"
# password = "cursoTEC2020"
# message = """\
# Subject: Mensaje de Prueba de Correo."""

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.starttls(context=context)
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders

def enviarCorreo(correo, cartonesPorAsignar):

	# global jugadores

	correoDeEnvio = "proyectoBingo3@gmail.com"
	correoReceptor = correo
	contrasena = "cursoTEC2020"

	mensaje = MIMEMultipart("alternative")
	mensaje["Subject"] = "Cartón para Juego de Bingo"
	mensaje["From"] = correoDeEnvio
	mensaje["To"] = correoReceptor

	text = """\¡Hola!</h1>
	Parece que has sido invitado a participar en un juego de BINGO
	Junto a este correo se han adjuntado los cartones para que puedas participar
	¡Buena Suerte!"""

	# textoHTML = open("Recursos\plantillaCorreo.html","r", encoding='utf-8')
	# html = textoHTML.read()
	# textoHTML.close()

	parte1 = MIMEText(text, "plain")
	# parte2 = MIMEText(html, "html")

	mensaje.attach(parte1)
	# mensaje.attach(parte2)

	# # for imagen in os.listdir('Cartones'): 
	# # 	if imagen.endswith('.png'):
	# for i in range(0,len(cartonesPorAsignar)): 
	# 	filename = cartonesPorAsignar[i]+".png"
		
	# 	attachment = open('Cartones/'+cartonesPorAsignar[i]+'.png', "rb")
  
	# 	adjunto = MIMEBase('application', 'octet-stream') 

	# 	adjunto.set_payload((attachment).read()) 

	# 	encoders.encode_base64(adjunto) 
		   
	# 	adjunto.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
		  
	# 	mensaje.attach(adjunto)

	try:
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(correoDeEnvio, contrasena)
			server.sendmail(correoDeEnvio, correoReceptor, mensaje.as_string())
		# jugadores+=1

		return 1
	except Exception as e:
		print(e)
		return -1


