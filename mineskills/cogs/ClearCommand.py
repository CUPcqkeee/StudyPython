import disnake
from disnake.ext import commands


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name='clear')
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send(f"{ctx.author.mention}, {amount} Сообщение было удалено!")

def setup(bot):
    bot.add_cog(ClearCommand(bot))
    print("Файлы: Раздел >> ClearCommand << успешно запущен")
