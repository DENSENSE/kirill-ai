import os
from PIL import Image 
from PIL import ImageFont 
from PIL import ImageDraw 

img = Image.open('D:/programming time/images/9932780b-05a8-47d4-936a-0e9eab803d16.OSJ0613.png')
font_path = 'D:/programming time/fonts/lobster/Lobster-Regular.ttf'


outline_color = 'black'  #  mega default
text_color = 'white'
text = input()

width, height = img.size
ratio = width // height
draw = ImageDraw.Draw(img) 

font_size = 120*ratio*0.3  #  will be configuratable
font = ImageFont.truetype(font_path, size=font_size)
(x, y) = ((width//2 - len(text)*ratio*0.3*20, height*0.8))

for adj in range(-3, 4):
    # We create a shadow for each x, y offset
    draw.text((x + adj, y), text, font=font, fill=outline_color)
    draw.text((x, y + adj), text, font=font, fill=outline_color)

draw.text((x, y), text, fill=text_color, font=font)

# saving the image 
img.save('sample.png') 