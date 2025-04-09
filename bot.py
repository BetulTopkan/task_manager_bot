import discord
from discord.ext import commands
from database import Database
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
db = Database()

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def add_task(ctx, *, description: str):
    task_id = db.add_task(description)
    await ctx.send(f'Görev eklendi! ID: {task_id}')

@bot.command()
async def delete_task(ctx, task_id: int):
    if db.delete_task(task_id):
        await ctx.send(f'Görev {task_id} silindi!')
    else:
        await ctx.send('Görev bulunamadı!')

@bot.command()
async def show_tasks(ctx):
    tasks = db.get_all_tasks()
    if not tasks:
        await ctx.send('Henüz görev eklenmemiş!')
        return
    
    message = "Görev Listesi:\n"
    for task_id, description, completed in tasks:
        status = "✅" if completed else "❌"
        message += f"{task_id}. {description} {status}\n"
    
    await ctx.send(message)

@bot.command()
async def complete_task(ctx, task_id: int):
    if db.complete_task(task_id):
        await ctx.send(f'Görev {task_id} tamamlandı olarak işaretlendi!')
    else:
        await ctx.send('Görev bulunamadı!')

token = os.getenv('DISCORD_TOKEN')
if token is None:
    print("Hata: DISCORD_TOKEN bulunamadı. Lütfen .env dosyasını kontrol edin.")
    exit(1)

bot.run(token) 