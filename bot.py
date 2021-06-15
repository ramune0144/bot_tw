from scr import bot_inv as _bot
import requests as req
import aiohttp
bot, nick, channel = _bot.bot_init()
client = _bot.client_init()

@bot.event
async def event_ready():
    print(f'Ready | {nick} | {channel}')

@bot.event
async def event_message(ctx):
    print(f'[{ctx.timestamp}] {ctx.author.name}: {ctx.content}')
    print(f'Mod: {ctx.author.is_mod} | Sub: {ctx.author.is_subscriber}')
    await bot.handle_commands(ctx)


async def get_chatters(channel):
    async with aiohttp.ClientSession() as session:
        url = 'https://tmi.twitch.tv/group/user/'+channel+'/chatters'
        async with session.get(url) as resp:
            chatters = await resp.json()
            return chatters["chatters"]["viewers"] 



async def get_chatters():
    chatters = await client.get_chatters(channel)
    return chatters.all


@bot.event
async def event_raw_data(data):
    print(data)


@bot.event
async def event_usernotice_subscription(metadata):
    print(metadata)

#ช้าเกินไม่ใช้-*-
'''
@bot.event
async def event_userstate(user):
    print(user)
'''
#

@bot.command(name='point')
async def payday(ctx):
    if ctx.author.name.lower() == channel or ctx.author.name.lower() == 'lamut_4480':  # only allow admin to execute
        argument = ctx.content.split()
        
        chatterList  = len(await get_chatters(channel))
        try:
            coin = int(argument[1])
        except:
            coin = 1
        #user_list = await get_chatters()
        await ctx.send(f'คนดู {chatterList} คน ได้รับ {coin} point')


if __name__ == "__main__":
    bot.run()