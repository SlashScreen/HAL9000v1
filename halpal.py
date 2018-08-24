import discord
import haltoken
client = discord.Client()

def powerup():
    import HAL9000V1

@client.event
async def on_message(message):
    msg = message.content.lower()
    if "halpal" in msg:
        if message.author.id == '199046815847415818':
            if "open" in msg:
                powerup()
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(type = 2, name='you'))
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



token = haltoken.halpal()
client.run(token)

