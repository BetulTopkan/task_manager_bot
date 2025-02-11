import discord
from discord.ext import commands
from database import Database

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
db = Database()

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')
    await db.create_tables()

@bot.command()
async def add_task(ctx, *, description):
    task_id = await db.add_task(description)
    await ctx.send(f'Görev eklendi! Görev ID: {task_id}')

@bot.command()
async def delete_task(ctx, task_id: int):
    if await db.delete_task(task_id):
        await ctx.send(f'Görev {task_id} silindi!')
    else:
        await ctx.send('Görev bulunamadı!')

@bot.command()
async def show_tasks(ctx):
    tasks = await db.get_tasks()
    if not tasks:
        await ctx.send('Hiç görev bulunmamaktadır!')
        return
    
    message = "**Görevler:**\n"
    for task in tasks:
        status = "✅" if task[2] else "❌"
        message += f"ID: {task[0]} | Durum: {status} | Görev: {task[1]}\n"
    await ctx.send(message)

@bot.command()
async def complete_task(ctx, task_id: int):
    if await db.complete_task(task_id):
        await ctx.send(f'Görev {task_id} tamamlandı olarak işaretlendi!')
    else:
        await ctx.send('Görev bulunamadı!')


bot.run('YOUR_BOT_TOKEN') 