import disnake

from config import settings

from disnake.ext import commands

bot = commands.Bot(command_prefix=settings['prefix'], intents=disnake.Intents.all())

bot.remove_command('help')

bot.load_extension("cogs.commands")
bot.load_extension("cogs.events")
bot.load_extension("cogs.helpmenu")
bot.load_extension("cogs.devmenu")


# Старт бота
bot.run(token=settings['token'])
