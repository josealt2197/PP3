from PIL import Image, ImageDraw, ImageFont
import os

# if __name__ == '__main__':
#     height = 600
#     width = 600
#     image = Image.new(mode='L', size=(height, width), color=255)

#     # Draw a line
#     draw = ImageDraw.Draw(image)
#     x = image.width / 2
#     y_start = 0
#     y_end = image.height
#     line = ((x, y_start), (x, y_end))
#     draw.line(line, fill=128)
#     del draw

#     image.show()


# def text_on_img(filename='01.png', text="Hello", size=12, color=(255,255,0), bg='red'):
#     "Draw a text on an Image, saves it, show it"
#     fnt = ImageFont.truetype('arial.ttf', size)
#     # create image
#     image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = bg)
#     draw = ImageDraw.Draw(image)
#     # draw text
#     draw.text((10,10), text, font=fnt, fill=(255,255,0))
#     # save file
#     image.save(filename)
#     # show file
#     os.system(filename)
 

# text_on_img(text="Text to write on img", size=300, bg='red')


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviarCorreo():
    
    sender_email = "proyecto3bingo@gmail.com"
    receiver_email = "josuebrenesa26@gmail.com"
    password = "cursoTEC2020"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a> 
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )