print('Груз:', сargo.group(0),сargo.group(1))
        print('Адрес доставки:', delivery_address.group(3),delivery_address.group(4)),
        print('Награда:', reward.group(4)),
        print('Доставить до:', deliver_to.group(5))

сargo = re.search(r'Груз: ([a-zA-z]+), (\d+)', message_content)
    delivery_address = re.search(r'Адрес доставки: ([a-zA-z]+), ([+\s-]\d+)', message_content)
    reward = re.search(r'Награда: (\d+)', message_content)
    deliver_to = re.search(r'Доставить до (\d+)', message_content)

сargo = re.search(r"Груз: ([a-zA-z]+), (\d+)", message_content)
delivery_address = re.search(r"Адрес доставки: ([a-zA-z]+), ([+\s-]\d+)", message_content)
reward = re.search(r"Награда: (\d+)", message_content)
deliver_to = re.search(r"Доставить до (\d+)", message_content)

id = re.search(r"([i,d,I,D]+):\s(\d+)", message.content)
сustomer = re.search(r"([а-я,А-Я]+):\s(\w+)", message.content)
сargo = re.search(r'([а-я,А-Я]+)\s(\d+)\s(.*)\.', message.content)
delivery_address = re.search(r'([a-z,A-Z]+)\s([+|-]\d+)\s([+|-]\d+)', message.content)
reward = re.search(r'(\d+)\s([а,л,м]+)\.', message.content)
disc = message.content.rpartition(":", message.content)


(id_order, id_courier, cargo, delivery_address, reward, description, сustomer, time_out, activ)

print(payload.member.id)
cur.execute(f"SELECT id_courier FROM orders WHERE id_courier = {payload.member.id}")
con.commit()
# id = cur.execute(f"SELECT id_order FROM orders WHERE id_courier = {member_id}")
# con.commit()

@bot.command()
async def job(id: int):
    member = ctx.author
    cur.execute(f"UPDATE orders SET id_courier ==? WHERE id_order ==?", (member, id))
    con.commit()
    record = cur.fetchall()
    if len(record):
        await member.send(
            embed=discord.Embed(
                title="Заказ принят",
                description=f"Вы приняли заказ {id}, срок которого истечёт через `1` день",
                colour=discord.Colour.from_rgb(77, 246, 102)
            ))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')