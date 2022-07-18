import discord
import sqlite3 as sq
from discord.ext import commands
from datetime import timedelta, datetime
import re

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

with sq.connect('DataBase.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS orders( 
        id_order INT,
        id_courier INT,
        id_message_one INT,
        id_message_two INT,
        cargo TEXT,
        delivery_address TEXT,
        reward TEXT,
        description TEXT,   
        сustomer TEXT, 
        time_out TEXT,
        activ BLOB DEFAULT TRUE
        )""")


@bot.event
async def on_message(message):
    channel = bot.get_channel(937377907939106901)
    if message.channel != channel:
        return
    await bot.process_commands(message)
    message_content = message.content.split("\n")
    date_now = datetime.now()
    id = str(message_content[0]).rpartition(":")
    сustomer = str(message_content[1]).rpartition(":")
    cargo = str(message_content[2]).rpartition(":")
    cargo_id = re.search(r'(([I,D]+)-(\d+))', message_content[2])
    cargo_id = re.findall('[0-9]+', cargo_id[0])
    link = f"https://my_site/item/{cargo_id[0]}"
    delivery_address = str(message_content[3]).rpartition(":")
    reward = str(message_content[4]).rpartition(":")
    description = str(message_content[5]).rpartition(":")
    cur.execute(f"INSERT INTO orders"
                f" VALUES('{id[2]}',NULL,{message.id},NULL ,'{cargo[2]}','{delivery_address[2]}','{reward[2]}','{description[2]}','{сustomer[2]}','{date_now + timedelta(days=1)}',NULL)")
    con.commit()

    if message.author.id == 619181347084304386:
        emoji = '✅'
        await message.add_reaction(emoji)
    print(link)
    print(id[2])
    print(сustomer[2])
    print(cargo[2])
    print(delivery_address[2])
    print(reward[2])
    print(description[2])
    print(cargo_id[0])


@bot.event
async def on_raw_reaction_add(guild, payload: discord.RawReactionActionEvent):
    if payload.member.bot:
        return
    member = bot.get_user(payload.member.id)
    ChID = 937377907939106901
    if payload.channel_id != ChID:
        return
    if str(payload.emoji) == "✅":
        await member.send(
            embed=discord.Embed(
                title="Заказ принят",
                description=f"Вы приняли заказ , срок которого истечёт через `1` день",
                colour=discord.Colour.from_rgb(77,246,102)
            ))
    await guild.channel.message

@bot.event
async def on_ready():
    print(f'{datetime.now()} ON READY')
    await bot.change_presence( status= discord.Status.online , activity= discord.Game('Zicnet'))

print(f'{datetime.now()} BOT START')
bot.run('OTMwNzcxMTQzODEwNDk4NjAw.Yd6uLQ.PMcl5jr4rs1Tm4_8qiG4hufLcxE')