import disnake
from disnake.ext import commands


class DevButton(disnake.ui.View):
    def __init__(self):
        super().__init__()

    @disnake.ui.button(label="IGepi", style=disnake.ButtonStyle.green, emoji="👑")
    async def manual1(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='IGepi | Павел',
                            description='ㅤ\n', colour=disnake.Colour.blurple())
        emb.set_image(
            url='https://i.imgur.com/Vpo1GDo.png')
        await ctx.response.send_message(embed=emb, ephemeral=True)

    @disnake.ui.button(label="CUPcqkeee", style=disnake.ButtonStyle.green, emoji="🔰")
    async def manual3(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='CUPcqkeee | Максим',
                            description='ㅤ', colour=disnake.Colour.blurple())
        emb.set_image(
            url='https://i.imgur.com/Nj7K6Au.png')
        await ctx.response.send_message(embed=emb, ephemeral=True)

    @disnake.ui.button(label="VanishStoun", style=disnake.ButtonStyle.blurple, emoji="💼", row=2)
    async def manual2(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='VanishStoun | Иван',
                            description='ㅤ\n', colour=disnake.Colour.blurple())
        emb.set_image(
            url='https://i.imgur.com/EIHOtnI.png')
        await ctx.response.send_message(embed=emb, ephemeral=True)

    @disnake.ui.button(label="Rairon_Horner", style=disnake.ButtonStyle.blurple, emoji="💻", row=2)
    async def manual4(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='Rairon_Horner | Максим',
                            description='ㅤ\n', colour=disnake.Colour.blurple())
        emb.set_image(
            url='https://i.imgur.com/wFB0CRL.png')
        await ctx.response.send_message(embed=emb, ephemeral=True)

    @disnake.ui.button(label="Jesssian", style=disnake.ButtonStyle.danger, emoji="🕵", row=3)
    async def manual5(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='Jesssian | Айдар',
                            description='ㅤ\n', colour=disnake.Colour.blurple())
        emb.set_image(
            url='https://i.imgur.com/T4ok8CJ.png')
        await ctx.response.send_message(embed=emb, ephemeral=True)

class DevCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='команда')
    async def dev(self, ctx):
        emb = disnake.Embed(title='Команда проекта MineSkills',
                            description='Ниже будет предоставлены кнопки выбора\n определённого члена команды\nВыбор лежит лишь за Вами.',
                            colour=disnake.Colour.blurple())
        emb.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
        emb.set_image(url='https://i.gifer.com/4Cb2.gif')
        await ctx.send(embed=emb, view=DevButton())


def setup(bot):
    bot.add_cog(DevCommand(bot))
    print("Файлы: Раздел >> DevCommand << успешно запущен")
