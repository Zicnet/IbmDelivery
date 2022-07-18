import discord
import sqlite3 as sq
from discord.ext import commands
from datetime import timedelta, datetime

bot = commands.Bot(command_prefix='.')

with sq.connect('DataBase.db') as con:
    cur = con.cursor()

    cur.exec

@bot.command()
async def info(ctx):ute("""CREATE TABLE IF NOT EXISTS warn ( 
        id INTEGER PRIMARY KEY,
        userid INT, 
        moderid INT,
        reason TEXT,
        time TEXT,
        activ BLOB DEFAULT TRUE,   
        time_out TEXT
        )""")
    member = ctx.author
    embed = discord.Embed(colour=discord.Colour.from_rgb(204, 255, 0), title=f"Профиль {member}")
    embed.add_field(name="Заработано", value=f"")
    embed.add_field(name="Кол-во выполненых закозов:", value=f"")
    embed.add_field(name="Кол-во НЕ выполненых закозов:", value=f"")
    embed.add_field(name="Активный заказ", value=f"")
    embed.set_footer(text=f"{datetime.now()}")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.reply(embed=embed)

@bot.command()
async def work(ctx):
    member = ctx.author
    embed = discord.Embed(colour=discord.Colour.from_rgb(204, 255, 0), title=f"Профиль {member}")
    embed.add_field(name="Активный заказ", value=f"")
    embed.add_field(name="Награда", value=f"")
    embed.add_field(name="Описание", value=f"")
    embed.add_field(name="Срок взятие заказа", value=f"")
    embed.add_field(name="Срок выполнение заказа", value=f"")
    embed.set_footer(text=f"{datetime.now()}")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.reply(embed=embed)


@bot.event
async def on_ready():
    print(f'{datetime.now()} ON READY')
    await bot.change_presence( status= discord.Status.online , activity= discord.Game('Zicnet'))




print(f'{datetime.now()} BOT START')
bot.run('OTMwNzcxMTQzODEwNDk4NjAw.Yd6uLQ.PMcl5jr4rs1Tm4_8qiG4hufLcxE')