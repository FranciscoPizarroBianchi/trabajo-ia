import discord
from discord.ext import commands
import uuid
import json
import requests
import shutil
import os
import subprocess

with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "La variable %s no existe" %secret_name


bot = commands.Bot(command_prefix='>', description="Soy un bot para el ramo de IA")



@bot.command()
async def is_on(ctx):
    await ctx.send('ola si')

#Evento
@bot.event
async def on_ready():
    print("Hola discord")

@bot.command()
async def save(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("Error: No attachments")
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'
            with open("img/" + imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)

@bot.command()
async def persona(ctx):
    os.chdir("/root/IA/stargan-v2")
    subprocess.call(['sh', 'activate-persona.sh'])
    await ctx.send(file=discord.File(r'/root/IA/stargan-v2/expr/results/celeba_hq/reference.jpg'))



@bot.command()
async def mascota(ctx):
    os.chdir("/root/IA/stargan-v2")
    subprocess.call(['sh', 'activate-mascota.sh'])
    await ctx.send(file=discord.File(r'/root/IA/stargan-v2/expr/results/afhq/reference.jpg'))

bot.run(get_secret('tokenID'))
