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

from PIL import Image, ImageDraw

# size of image
canvas = (400, 300)

# scale ration
scale = 5
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]

# init canvas
im = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw = ImageDraw.Draw(im)

# draw rectangles
for frame in frames:
    x1, y1 = frame[2], frame[3]
    x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
    draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255))

# make thumbnail
im.thumbnail(thumb)

# save image
im.save('im.png')