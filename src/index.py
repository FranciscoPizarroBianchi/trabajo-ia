import discord
from discord.ext import commands
import uuid
import requests
import shutil


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

bot.run('MTAwNDgzMjk2ODU2NjY0NDczNg.GV8I8f.UgxD426Cbl3RYyORfo0M_wTpPtFvUV--Tj7blE')
