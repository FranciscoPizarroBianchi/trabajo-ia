import discord
from discord.ext import commands
import uuid
import json
import requests
import shutil
import os

"""
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "La variable %s no existe" %secret_name
"""

bot = commands.Bot(command_prefix='>', description="Soy un bot para el ramo de IA")



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#Evento
@bot.event
async def on_ready():
    print("Hola discord")

@bot.command()
async def save(ctx):
    # USAGE: use command .save in the comment box when uploading an image to save the image as a jpg
    try:
        url = ctx.message.attachments[0].url            # check for an image, call exception if none found
    except IndexError:
        print("Error: No attachments")
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'      # uuid creates random unique id to use for image names
            with open("img/" + imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)     # save image (goes to project directory)

@bot.command()
async def give(ctx):
    await ctx.send(file=discord.File(r'C:\Users\frpiz\Desktop\Universidad 2022\IA\TrabajoFinal\trabajo-ia\img/20bf9b3f-af6c-4ece-84e6-a1639f214337.jpg'))


bot.run(os.environ['BOT_TOKEN'])
