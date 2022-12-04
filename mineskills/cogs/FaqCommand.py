import disnake
from disnake.ext import commands
from config import faq_bot


class FaqButton(disnake.ui.View):
    def __init__(self):
        super().__init__()

    @disnake.ui.button(label="• Как зайти на сервер?", style=disnake.ButtonStyle.green, row=1, emoji='🌎')
    async def faq1(self, button: disnake.ui.Button, ctx):
        embeds = disnake.Embed(colour=disnake.Colour.yellow())
        embeds.add_field(name="👉 Как зайти на сервер?", value=faq_bot['1'], inline=False)
        await ctx.send(embed=embeds, ephemeral=True)

    @disnake.ui.button(label="• С чего начать выживание?", style=disnake.ButtonStyle.green, row=1, emoji='🌕')
    async def faq2(self, button: disnake.ui.Button, ctx):
        embed2 = disnake.Embed(colour=disnake.Colour.yellow())
        embed2.add_field(name='👉 С чего начать выживание?', value=faq_bot['2'], inline=False)
        await ctx.send(embed=embed2, ephemeral=True)

    @disnake.ui.button(label="• Кто состоит в команде проекта и как в неё попасть?",
                       style=disnake.ButtonStyle.secondary,
                       row=4, emoji='🛡')
    async def faq4(self, button: disnake.ui.Button, ctx):
        embed4 = disnake.Embed(colour=disnake.Colour.yellow())
        embed4.add_field(name='👉 Кто состоит в команде проекта и как в неё попасть?', value=faq_bot['4'], inline=False)
        await ctx.send(embed=embed4, ephemeral=True)

    @disnake.ui.button(label="• Какая валюта на сервере и как её получать?", style=disnake.ButtonStyle.secondary, row=3,
                       emoji='💎')
    async def faq5(self, button: disnake.ui.Button, ctx):
        embed5 = disnake.Embed(colour=disnake.Colour.yellow())
        embed5.add_field(name='👉 Какая валюта на сервере и как её получать?', value=faq_bot['5'], inline=False)
        await ctx.send(embed=embed5, ephemeral=True)

    @disnake.ui.button(label="• На что я могу потратить валюту?", style=disnake.ButtonStyle.secondary, row=3, emoji='🛒')
    async def faq6(self, button: disnake.ui.Button, ctx):
        embed6 = disnake.Embed(colour=disnake.Colour.yellow())
        embed6.add_field(name='👉 На что я могу потратить валюту?', value=faq_bot['6'], inline=False)
        await ctx.send(embed=embed6, ephemeral=True)

    @disnake.ui.button(label="• Разрешены ли мобо-фермы/афк-фермы?", style=disnake.ButtonStyle.secondary, row=4,
                       emoji='♻')
    async def faq7(self, button: disnake.ui.Button, ctx):
        embed7 = disnake.Embed(colour=disnake.Colour.yellow())
        embed7.add_field(name='👉 Разрешены ли мобо-фермы/афк-фермы?', value=faq_bot['7'], inline=False)
        await ctx.send(embed=embed7, ephemeral=True)

    @disnake.ui.button(label="• Разрешено ли использование кликера?", style=disnake.ButtonStyle.secondary, row=4,
                       emoji='🖱')
    async def faq8(self, button: disnake.ui.Button, ctx):
        embed8 = disnake.Embed(colour=disnake.Colour.yellow())
        embed8.add_field(name='👉 Разрешено ли использование кликера?', value=faq_bot['8'], inline=False)
        await ctx.send(embed=embed8, ephemeral=True)

    @disnake.ui.button(label="• Где я могу посмотреть новые предметы и механики?", style=disnake.ButtonStyle.secondary,
                       row=4, emoji='📜')
    async def faq3(self, button: disnake.ui.Button, ctx):
        embed3 = disnake.Embed(colour=disnake.Colour.yellow())
        embed3.add_field(name='👉 Где я могу посмотреть новые предметы и механики?', value=faq_bot['3'], inline=False)
        await ctx.send(embed=embed3, ephemeral=True)

    @disnake.ui.button(label="• Как связаться с администрацией сервера?", style=disnake.ButtonStyle.secondary, row=3,
                       emoji='☎')
    async def faq9(self, button: disnake.ui.Button, ctx):
        embed9 = disnake.Embed(colour=disnake.Colour.yellow())
        embed9.add_field(name='👉 Как связаться с администрацией сервера?', value=faq_bot['9'], inline=False)
        await ctx.send(embed=embed9, ephemeral=True)

    @disnake.ui.button(label="• Как узнать все доступные команды?", style=disnake.ButtonStyle.secondary, row=3,
                       emoji='📃')
    async def faq10(self, button: disnake.ui.Button, ctx):
        embed10 = disnake.Embed(colour=disnake.Colour.yellow())
        embed10.add_field(name='👉 Как узнать все доступные команды?', value=faq_bot['10'], inline=False)
        await ctx.send(embed=embed10, ephemeral=True)

    @disnake.ui.button(label="• Что за Эра / Сезон?", style=disnake.ButtonStyle.secondary, row=1, emoji='🔑')
    async def faq11(self, button: disnake.ui.Button, ctx):
        embed11 = disnake.Embed(colour=disnake.Colour.yellow())
        embed11.add_field(name='👉 Что за Эра / Сезон?', value=faq_bot['11'], inline=False)
        await ctx.send(embed=embed11, ephemeral=True)

class FaqCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="вопросы")
    async def faq(self, ctx):
        emb = disnake.Embed(title='Часто задаваемые вопросы',
                            description='Ниже будет предоставлены кнопки выбора\n определённого вопроса\nВыбор лежит лишь за Вами.',
                            colour=disnake.Colour.blurple())
        emb.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
        emb.set_image(url='https://i.gifer.com/fyhz.gif')
        await ctx.send(embed=emb, view=FaqButton())

def setup(bot):
    bot.add_cog(FaqCommand(bot))
    print("Файлы: Раздел >> FaqCommand << успешно запущен")
