# from PIL import Image, ImageDraw, ImageFont
# import os

# # if __name__ == '__main__':
# #     height = 600
# #     width = 600
# #     image = Image.new(mode='L', size=(height, width), color=255)

# #     # Draw a line
# #     draw = ImageDraw.Draw(image)
# #     x = image.width / 2
# #     y_start = 0
# #     y_end = image.height
# #     line = ((x, y_start), (x, y_end))
# #     draw.line(line, fill=128)
# #     del draw

# #     image.show()


# # def text_on_img(filename='01.png', text="Hello", size=12, color=(255,255,0), bg='red'):
# #     "Draw a text on an Image, saves it, show it"
# #     fnt = ImageFont.truetype('arial.ttf', size)
# #     # create image
# #     image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = bg)
# #     draw = ImageDraw.Draw(image)
# #     # draw text
# #     draw.text((10,10), text, font=fnt, fill=(255,255,0))
# #     # save file
# #     image.save(filename)
# #     # show file
# #     os.system(filename)
 

# # text_on_img(text="Text to write on img", size=300, bg='red')

# from PIL import Image, ImageDraw

# # size of image
# canvas = (400, 300)

# # scale ration
# scale = 5
# thumb = canvas[0]/scale, canvas[1]/scale

# # rectangles (width, height, left position, top position)
# frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]

# # init canvas
# im = Image.new('RGBA', canvas, (255, 255, 255, 255))
# draw = ImageDraw.Draw(im)

# # draw rectangles
# for frame in frames:
#     x1, y1 = frame[2], frame[3]
#     x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
#     draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255))

# # make thumbnail
# im.thumbnail(thumb)

# # save image
# im.save('im.png')


# def validarCorreo(correo):
#     contador=0
#     longitud=len(correo)
#     punto=correo.find(".")
#     arroba=correo.find("@")

#     if(punto==-1 or arroba==-1):
#     	return False

#     for i in range (0,arroba):
#         if((correo[i]>='a' and correo[i]<='z') or (correo[i]>='A' and correo[i]<='Z')):
#             contador=contador+1
    
#     if(contador>0 and arroba>0 and (punto-arroba)>0 and (punto+1)<longitud):
#         return True
#     else:
#         return False


# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email.mime.image import MIMEImage

# Define these once; use them twice!
emisor = 'proyecto3bingo@gmail.com'
receptor = 'josealt2197@gmail.com'

# Create the root message and fill in the from, to, and subject headers
mensaje = MIMEMultipart('related')
mensaje['Subject'] = 'test message'
mensaje['From'] = emisor
mensaje['To'] = receptor
mensaje.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
mensaje.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('imagenCorreoCartones.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
mensaje.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)

# smtp = smtplib.SMTP()
# smtp.connect('smtp.gmail.com')
# smtp.login('proyecto3taller@gmail.com', 'cursoTEC2020')
# smtp.sendmail(emisor, receptor, mensaje.as_string())
# smtp.quit()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('proyecto3bingo@gmail.com', 'cursoTEC2020')
    server.sendmail(emisor, receptor, mensaje.as_string())