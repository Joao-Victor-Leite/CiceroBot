from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
from asm_functions import *

load_dotenv()

class Cicero(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            intents=intents,
            commands_prefix="//"
        )

        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        await self.tree.sync()


    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


bot = Cicero()

@bot.tree.command(name='asm_roll', description='Rolls knowledge and practices')
async def asmRoll(interaction:discord.Interaction, knowledge:int, practices:int):

    await interaction.response.send_message('Rolling knowledge and practices...')

    knowledge_result = roll_asm_dice(knowledge, 6)
    practices_result = roll_asm_dice(practices, 10)

    await interaction.followup.send(f"**Knowledge Rolls:**\n{knowledge_result}\n\n**Practices Rolls:**\n{practices_result}")
    ...


bot.run(DISCORD_TOKEN)
