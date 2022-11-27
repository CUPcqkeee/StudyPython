import datetime

import disnake
from disnake.ext import commands

from discord_bot.cogs.helpmenu import HelpMenu
from discord_bot.cogs.devmenu import DevMenu

from disnake import Button, ButtonStyle, member, user, Client, client


class SlashCommands(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name="clear", description='Очистка чата в определённом количестве')
    async def clear(self, ctx, amount=None):
        await ctx.channel.purge(limit=int(amount))
        await ctx.response.send_message(f"{ctx.author.mention}, {amount} Сообщений успешно удалено!", delete_after=1.5)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.response.send_message(f'{ctx.author.mention}, У вас недостаточно прав!', delete_after=0.5)
        else:
            raise error

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name='ban', description='Бан участника')
    async def ban(self, ctx, member: disnake.Member, reason=None):
        await member.ban(reason=reason)

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name='kick', description='Кик участника')
    async def kick(self, ctx, member: disnake.Member, *, reason):
        channel = commands.get_channel(789968921432031272)
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=0)
        emb = disnake.Embed(color=344462)
        emb.add_field(name=f'✅ Наказание',
                      value=f'Пользователь {member.mention} был кикнут {ctx.author.mention}\nПо следующей причине: **{reason}**')
        await ctx.response.send_message(embed=emb, delete_after=5)
        embk = disnake.Embed(colour=disnake.Colour.red())
        embk.add_field(name=f'✅ Наказание',
                       value=f'Вы были кикнуты с сервера **MineSkills**!\nПричина кика: **{reason}**\nКем были кикнуты: **{ctx.author.mention}**\nВремя кика: **{datetime.datetime.now()}**')
        embk.add_field(name=f'Если вы желаете обжаловать наказание:', value='https://vk.com/choopa_io', inline=False)
        await member.send(embed=embk)

    @kick.error
    async def kick(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.response.send_message(f'{ctx.author.mention}, У вас недостаточно прав!', delete_after=0.5)
        else:
            raise error

    @commands.slash_command(name="menu", description="Вывод меню с выбором команд")
    async def menu(self, ctx):
        view = HelpMenu()
        embed = disnake.Embed(colour=disnake.Colour.blue(), title="Помощь по моим командам")
        embed.add_field(name="Ниже будут предоставлены кнопки выбора \nНажмите на одну из понравившейся Вам\n",
                        value="\nПриятной Вам игры на **MineSkills**!", inline=True)
        embed.set_footer(text=commands.user.name, icon_url=commands.user.avatar)
        embed.set_image(url="https://i.gifer.com/7Zc6.gif")
        await ctx.response.send_message(embed=embed, view=view)

    @commands.slash_command(name="dev", description="Команда проекта MineSkills")
    async def dev(self, ctx):
        view = DevMenu()
        emb = disnake.Embed(title='Команда проекта MineSkills',
                            description='Ниже будет предоставлены кнопки выбора\n определённого члена команды\nВыбор лежит лишь за Вами.')
        emb.set_image(url='https://i.gifer.com/4Cb2.gif')
        await ctx.response.send_message(embed=emb, view=view)


def setup(bot: commands.Bot):
    bot.add_cog(SlashCommands(bot))
    print(f'>Extension {__name__} is ready')
