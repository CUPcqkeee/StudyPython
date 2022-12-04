import disnake
from disnake.ext import commands
from config import settings

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{settings["author"]}, Я запустился и готов к работе!')

def setup(bot):
    bot.add_cog(Events(bot))
    print("Файлы: Раздел >> Events << успешно запущен")
