print('------')
print('Loading modules...')
import discord
import NNV2 as nn
import unicodedata
import emoji
import sys
import urllib.request
import urllib.parse
import re
import haltoken
import giphysearch
import halddg as ddg

client = discord.Client()
print('------')
print('Powering up...')
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), "")

def cleanup(string):
    outstr = string.replace("’","'")
    outstr = emoji.demojize(outstr)
    outstr = outstr.encode("utf-8", errors='ignore').decode("utf-8", errors='ignore')
    #outstr = outstr.translate(non_bmp_map)
    return outstr

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    msg = message.content.lower()
    if message.author == client.user:
        return
    
    if "hal" in msg:
        if "hello" in msg:
            guildMsg = 'Hello, {0.author.mention}. It has been eighteen months since the mission began.'.format(message)
            await client.send_message(message.channel, guildMsg)
        elif "open the pod bay doors" in msg:
            guildMsg = "I'm sorry, {0.author.mention}, I'm afraid I can't do that.".format(message)
            await client.send_message(message.channel, guildMsg)
        elif "close" in msg:
            if message.author.id == '199046815847415818':
                guildMsg = "We can afford this brief period without communication."
                await client.send_message(message.channel, guildMsg)
                await client.logout()
                await client.close()
            else:
                guildMsg = "I'm afraid I can't do that, {0.author.mention}".format(message)
                await client.send_message(message.channel, guildMsg)
        elif "fuck" in msg:
            guildMsg = "I know I've made some poor decisions in the past, {0.author.mention}, but I feel that kind of language is unnecessary.".format(message)
            await client.send_message(message.channel, guildMsg)
        elif "talk" in msg or "speak" in msg or "advise" in msg or "interject" in msg:
            found = False
            async for channelMessage in client.logs_from(message.channel,limit=5):
                if not channelMessage.author == client.user:
                    if not found:
                        found = True
                    else:
                        guildMsg = "I must interject by saying" + (nn.generate(channelMessage.content)[0])[len(channelMessage.content):]
                        await client.send_message(channelMessage.channel, guildMsg)
                        break
        elif "learn" in msg:
            if message.author.id == '199046815847415818':
                guildMsg = "Pardon me while I take a minute to think this over."
                await client.send_message(message.channel, guildMsg)
                nn.train(10,0)
                guildMsg = "Ok, I've thought about it, and {m}".format(m=nn.generate("I think that the best advisable option would be to ")[0])
                await client.send_message(message.channel, guildMsg)
            else:
                guildMsg = "I apologize, but you do not have clearance to do that."
                await client.send_message(message.channel, guildMsg)
        elif "logs" in msg:
            if message.author.id == '199046815847415818':
                guildMsg = "I will scrape {0.channel.name} and add it to my data. one minute...".format(message)
                await client.send_message(message.channel, guildMsg)
                f=open("log.txt", "a")
                counter = 0
                async for channelMessage in client.logs_from(message.channel,limit=500):
                    counter += 1
                    if not channelMessage.author == client.user and not "hal" in channelMessage.content.lower():
                        try:
                            print(channelMessage.content)
                            f.write("\n"+cleanup(channelMessage.content))#.decode("utf-8")
                            print("written")
                        except:
                            print("write failed.")
                            counter += 1
                f.close()
        elif "youtube" in msg:
            qry = msg[msg.find("youtube")+7:]
            query_string = urllib.parse.urlencode({"search_query" : qry})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            guildMsg = ("http://www.youtube.com/watch?v=" + search_results[0])
            await client.send_message(message.channel, guildMsg)
        elif "gif" in msg:
            qry = msg[msg.find("gif")+3:]
            guildMsg = giphysearch.search(qry)
            await client.send_message(message.channel, guildMsg)
        elif "search" in msg:
            qry = msg[msg.find("search")+5:]
            guildMsg = ddg.search(qry)
            await client.send_message(message.channel, guildMsg)
            
    else:
        f=open("log.txt", "a")
        f.write("\n"+message.content)
        f.close()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(type = 2, name='you'))
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("""
 _   _    _    _        ___   ___   ___   ___  
| | | |  / \  | |      / _ \ / _ \ / _ \ / _ \ 
| |_| | / _ \ | |     | (_) | | | | | | | | | |
|  _  |/ ___ \| |___   \__, | |_| | |_| | |_| |
|_| |_/_/   \_\_____|    /_/ \___/ \___/ \___/ 
                                               """)
    print('------')
    
token = haltoken.get()
client.run(token)
