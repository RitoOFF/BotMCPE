import discord
import os
from discord import *
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="+", intents=intents)
intents = discord.Intents().all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@bot.event
async def on_ready():
 print('Online')
 try:
    synced = await bot.tree.sync()
    print(f"------\n{len(synced)} commands Lancer\n------")
 except Exception as c:
      print(c)
@bot.tree.command(name="plugin", description="Voire la list des plugins et les téléchargers !")
async def db_slash(interaction: discord.Interaction,
                   name: str = None):
   if name is None:   
     folder_path = 'plugin'  
     file_names = os.listdir(folder_path) 
    
     files_str = '\n- '.join(file_names)
     embed = discord.Embed()
     embed.set_author(name=f"Plugin | List")
     embed.add_field(name='', value=f'Voici la list de tout les plugins disponibles actuelement:\n\n```{files_str}```\n- Bonne journée __{interaction.user.name}__')
     embed.set_footer(text=f"{bot.user.name}・ By rito.off")
     await interaction.response.send_message(embed=embed)
   else:   
     folder_path = 'plugin'  
     file_names = os.listdir(folder_path)
     matching_files = [file for file in file_names if name in file]
     if matching_files:
         matching_file = matching_files[0]
         file_path = os.path.join(folder_path, matching_file)
         file_to_send = discord.File(file_path)
         await interaction.response.send_message(f"```Le plugin'{name}' vous a été envoyez par message l'envoie est en cours ...```")
         await interaction.user.send(f"# Plugin {name}\n\n- Hey voici le plugin que tu a demander n'hesite pas a revenir\nBot create by rito.off")
         await interaction.user.send(file=file_to_send)
         await interaction.user.send(f"――――――――――――――――――――――――")
     else:
         await interaction.response.send_message(f"Aucun Plugin correspondant à '{name}' n'a été trouvé.")

@bot.tree.command(name="world", description="Voire la list des worlds et les téléchargers !")
async def db_slash(interaction: discord.Interaction,
                   name: str = None):
   if name is None:   
     folder_path = 'world'  
     file_names = os.listdir(folder_path) 
     
     files_str = '\n- '.join(file_names)
     embed = discord.Embed()
     embed.set_author(name=f"World | List")
     embed.add_field(name='', value=f'Voici la list de tout les worlds disponibles actuelement:\n\n```{files_str}```\n- Bonne journée __{interaction.user.name}__')
     embed.set_footer(text=f"{bot.user.name}・ By rito.off")
     await interaction.response.send_message(embed=embed)
   else:   
     folder_path = 'world' 
     file_names = os.listdir(folder_path)
     matching_files = [file for file in file_names if name in file]
     if matching_files:
         matching_file = matching_files[0]
         file_path = os.path.join(folder_path, matching_file)
         file_to_send = discord.File(file_path)
         await interaction.response.send_message(f"```Le world'{name}' vous a été envoyez par message l'envoie est en cours ...```")
         await interaction.user.send(f"# World {name}\n\n- Hey voici le world que tu a demander n'hesite pas a revenir\nBot create by rito.off")
         await interaction.user.send(file=file_to_send)
         await interaction.user.send(f"――――――――――――――――――――――――")
     else:
         await interaction.response.send_message(f"Aucun Monde trouvée correspondant à '{name}' n'a été trouvé.")         

@bot.tree.command(name="texture_pack", description="Voire la list des textures pack et les téléchargers !")
async def db_slash(interaction: discord.Interaction,
                   name: str = None):
   if name is None:   
     folder_path = 'texture_pack'  
     file_names = os.listdir(folder_path) 
     
     files_str = '\n- '.join(file_names)
     embed = discord.Embed()
     embed.set_author(name=f"Texture Pack | List")
     embed.add_field(name='', value=f'Voici la list de tout les textures packs disponibles actuelement:\n\n```{files_str}```\n- Bonne journée __{interaction.user.name}__')
     embed.set_footer(text=f"{bot.user.name}・ By rito.off")
     await interaction.response.send_message(embed=embed)
   else:   
     folder_path = 'texture_pack' 
     file_names = os.listdir(folder_path)
     matching_files = [file for file in file_names if name in file]
     if matching_files:
         matching_file = matching_files[0]
         file_path = os.path.join(folder_path, matching_file)
         file_to_send = discord.File(file_path)
         await interaction.response.send_message(f"```Le texture pack'{name}' vous a été envoyez par message l'envoie est en cours ...```")
         await interaction.user.send(f"# Texture Pack {name}\n\n- Hey voici le world que tu a demander n'hesite pas a revenir\nBot create by rito.off")
         await interaction.user.send(file=file_to_send)
         await interaction.user.send(f"――――――――――――――――――――――――")
     else:
         await interaction.response.send_message(f"Aucun Texture pack trouvée correspondant à '{name}' n'a été trouvé.") 
@bot.tree.command(name="backup", description="Voire la list des backup et les téléchargers !")
async def db_slash(interaction: discord.Interaction,
                   name: str = None):
   if name is None:   
     folder_path = 'backup'  
     file_names = os.listdir(folder_path) 
     
     files_str = '\n- '.join(file_names)
     embed = discord.Embed()
     embed.set_author(name=f"Texture Pack | List")
     embed.add_field(name='', value=f'Voici la list de toutes les backup disponibles actuelement:\n\n```{files_str}```\n- Bonne journée __{interaction.user.name}__')
     embed.set_footer(text=f"{bot.user.name}・ By rito.off")
     await interaction.response.send_message(embed=embed)
   else:   
     folder_path = 'backup' 
     file_names = os.listdir(folder_path)
     matching_files = [file for file in file_names if name in file]
     if matching_files:
         matching_file = matching_files[0]
         file_path = os.path.join(folder_path, matching_file)
         file_to_send = discord.File(file_path)
         await interaction.response.send_message(f"```La backup'{name}' vous a été envoyez par message l'envoie est en cours ...```")
         await interaction.user.send(f"# Backup {name}\n\n- Hey voici la backup que tu a demander n'hesite pas a revenir\nBot create by rito.off")
         await interaction.user.send(file=file_to_send)
         await interaction.user.send(f"――――――――――――――――――――――――")
     else:
         await interaction.response.send_message(f"Aucune backup  trouvée correspondant à '{name}' n'a été trouvé.")                    
      

bot.run('MTE2Nzg4Njk0MDQxMTAyMzM5MA.GtKhTk.LwbzeBj3ja8HP24UkpX0cf9wKiqsYiqmMvdaAs')