import discord
import sqlite3
import random
from PIL import Image, ImageDraw, ImageFont 
import io
import os
import uuid
connection = sqlite3.connect('Niggerbase.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages(message TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS images_uuid(id TEXT)")
connection.commit()
TOKEN = "MTIyOTM5Nzc5MTY3MTk4MDA4Mw.G8U2b2.cGoA0TuzQRxMSWERuvdeSBx82_NivBJ0ncKIi0"
bot = discord.Bot(intents=discord.Intents.all())


def anti_link(linestring): # say no to links, except gif ones(tenor)!
    if "https://tenor.com/" in linestring or 'tenor.com' in linestring:
        return True
    
    for item in ['https://', 'http://', 'www./', '.org/', 'ru/', '.com/', '.net/', '.ua/', '.uk/', '.eu/']:
        if item in linestring:
            return False
    
    return True

available_fonts = ['./fonts/comicsans/ComicSansMS3.ttf', './fonts/lobster/Lobster-Regular.ttf']

# def compressing_process(saved_img):  #  compressing fcking image to optimize memeory-containing
    
# def random_string_generator(data):  #  doing somee goofy ah sentences with random amount of string with random parts of'em
def imaged(path, text):
    if "https://tenor.com/" in text or 'tenor.com' in text:
        return False
    img = Image.open(path)
    draw = ImageDraw.Draw(img)

    font_path = available_fonts[random.randint(0, len(available_fonts)-1)]

    width, height = img.size
    ratio = width // height

    outline_color = 'black'  #  mega default
    text_color = 'white'
    font_size = 120*ratio*0.7
    while font_size <= 0.1:
        font_size += 1

    draw = ImageDraw.Draw(img)                                                                                                  

    font = ImageFont.truetype(font_path, size=font_size)
    (x, y) = ((width//2 - len(text)*ratio*0.3*20, height*0.8))

    for adj in range(-3, 4):
        # We create a shadow for each x, y offset
        draw.text((x + adj, y), text, font=font, fill=outline_color)
        draw.text((x, y + adj), text, font=font, fill=outline_color)

    draw.text((x, y), text, fill=text_color, font=font) 

    with io.BytesIO() as image_binary:
                            img.save(image_binary, 'PNG')
                            image_binary.seek(0)
                            file = discord.File(fp=image_binary, filename='image.png')
    return file

@bot.event
async def on_ready():
    print('Я негр')
    try:
        os.mkdir('./images')
    except:
        pass
message_counter = 0
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if anti_link(message.content):
        if message.content != '':
            cursor.execute('INSERT INTO messages VALUES(?)', (message.content,))   #  saves up a message if anti_link returns True
    if random.randint(0, 21) in [i for i in range(0, 14)]:
        file = None
        randomnoe_znach = random.randint(0, 9)
        if randomnoe_znach in [1, 2, 3, 4, 5, 6]:  #  рандом чекается тут! типо 4 из 8
            cursor.execute("SELECT * FROM images_uuid")
            data = cursor.fetchall()
            if data == []:
                return
            path = f"{data[random.randint(0, len(data) - 1)][0]}"
            cursor.execute("SELECT * FROM messages")
        
            data = cursor.fetchall()
            file = imaged(f"./images/{path}", data[random.randint(0, len(data) - 1)][0])

        cursor.execute("SELECT * FROM messages")
        
        data = cursor.fetchall()
        if data == []:
            return
        if file != False:
            print('Попытка сгенерить картинку...')
        await message.channel.send(data[random.randint(0, len(data) - 1)][0], file=file)
    
    if message.attachments != []:
        for attach in message.attachments:
            current_id = uuid.uuid4()
            print(attach.content_type)

            await attach.save(f'./images/{current_id}.{attach.filename}')

            cursor.execute('INSERT INTO images_uuid VALUES(?)', (f"{current_id}.{attach.filename}",))

    connection.commit()

bot.run(TOKEN)
