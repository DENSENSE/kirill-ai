# circles on the pic!
from PIL import Image, ImageDraw, ImageFont
import math as m
import random

def vector(img, x1, y1, x2, y2):
    sin60 = m.sin(60)
    # x1, x2, y1, y2 is for main part of arrow
    # ar1, ar2 = two addit. parts of arrow
    adda = 0.2 * m.ceil(m.sqrt((x1-x2)**2 + (y1-y2)**2))
    cd = m.tan(x1 + adda) * m.sqrt(3)
    o1 = x1 + cd
    u1 = x1 - cd
    ad = (cd * 2) / m.sqrt(3)
    o2 = y1 + ad
    u2 = y1 - ad
    
    
    
    (arx1, ary1) = (o1, o2)
    (arx2, ary2) = (u1, u2)
    
    draw.line((x2, y2, x1, y1), fill='red')
    draw.line((x2, y2, o2, o1), fill='red')
    draw.line((x2, y2, u2, u1), fill='red')
    img.show()

img = Image.open('programming-time-main/img.jpg')

draw = ImageDraw.Draw(img)
# img.show()

width, height = img.size

if width > height: ratio = width//height
else: ratio = height//width

(x, y) = (random.randint(251, width-250), random.randint(251, height-250))
rad = 250*ratio
outline = 25*ratio

draw.ellipse((x-rad, y-rad, x+rad, y+rad), outline='red', width=outline)

vector(img, x+rad, y+rad, 100, 100)