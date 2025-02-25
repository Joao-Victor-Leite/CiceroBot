from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

class Cicero(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()



Cicero.run()
