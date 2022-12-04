import disnake
from disnake.ext import commands
from config import commands_bot, settings


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='помощь', description='Помощь по командам')
    async def help(self, ctx):
        emb = disnake.Embed(colour=disnake.Colour.blue())
        emb.add_field(name='Команды бота:', value=f'ㅤ')
        emb.add_field(name='.помощь', value=commands_bot['help'], inline=False)
        emb.add_field(name='.меню', value=commands_bot['menu'], inline=False)
        emb.add_field(name='.команда', value=commands_bot['dev'], inline=False)
        emb.add_field(name='.stats', value=commands_bot['stats'], inline=False)
        emb.add_field(name='.вопросы', value=commands_bot['qa'])
        emb.set_image(url='https://i.gifer.com/Q81V.gif')
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
    print("Файлы: Раздел >> HelpCommand << успешно запущен")
