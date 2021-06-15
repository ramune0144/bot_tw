import os
from twitchio.client import Client
from twitchio.ext import commands
import json
def json_read(data):
        with open(data,"r") as json_file:
            data = json.load(json_file)
        return data

print(json_read("setting.json")['CLIENT_ID'])           
def bot_init():
    bot = commands.Bot(
        irc_token=json_read("setting.json")['TMI_TOKEN'],
        client_id=json_read("setting.json")['CLIENT_ID'],
        nick=json_read("setting.json")['BOT_NICK'],
        prefix=json_read("setting.json")['BOT_PREFIX'],
        initial_channels=[json_read("setting.json")['CHANNEL']]
    )
    return bot, json_read("setting.json")['BOT_NICK'],json_read("setting.json")['CHANNEL']

def client_init():
    client = Client(
        client_id=json_read("setting.json")['CLIENT_ID'],
        client_secret=json_read("setting.json")['CLIENT_SECRET']
    )
    return client