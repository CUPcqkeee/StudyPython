import disnake
from disnake.ext import commands


class DevMenu(commands.Cog, disnake.ui.View):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @disnake.ui.button(label="CUPcqkeee", style=disnake.ButtonStyle.success, emoji="🧁")
    async def manual(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='CUPcqkeee | Максим',
                            description='**———————————————————————————————**\n')
        emb.add_field(
            name='Всем привет. Меня зовут Максим. Являюсь разработчиком данного проекта. Все баги - моя забота. Многого сказать не смогу о себе, но скажу главное... Я начинал заниматься созданием серверов с \n12-и лет.',
            value='ㅤ')
        emb.add_field(
            name='Было куча падений, куча неудач, но это опыт! И вот сейчас, я набрался достаточно опыта для открытия не маленького проекта.\nНадеюсь Вам понравится наше творение!',
            value='ㅤ', inline=True)
        emb.set_image(
            url='https://ic.wampi.ru/2022/11/26/CUPcqkeee.png')
        emb.set_footer(text='«Лучший выход всегда через». ©️ Роберт Фрост',
                       icon_url='https://minecraft-heads.com/media/k2/items/cache/a50d832102cc6e332d683d2706cedf12_XS.jpg')
        await ctx.response.send_message(embed=emb)

    @disnake.ui.button(label="IGepi", style=disnake.ButtonStyle.success, emoji="🧁")
    async def manual1(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='IGepi | Павел',
                            description='**———————————————————————————————**\n')
        emb.add_field(
            name='Всем привет. Меня зовут Максим. Являюсь разработчиком данного проекта. Все баги - моя забота. Многое сказать не смогу о себе, но скажу главное... Я начинал заниматься созданием серверов с \n12-и лет.',
            value='ㅤ')
        emb.add_field(
            name='Было куча падений, куча неудач, но это опыт! И вот сейчас, я набрался достаточно опыта для открытия не маленького проекта.\nНадеюсь Вам понравится наше творение!',
            value='ㅤ', inline=True)
        emb.set_image(
            url='https://ic.wampi.ru/2022/11/26/CUPcqkeee.png')
        emb.set_footer(text='«Лучший выход всегда через». ©️ Роберт Фрост',
                       icon_url='https://minecraft-heads.com/media/k2/items/cache/a50d832102cc6e332d683d2706cedf12_XS.jpg')
        await ctx.response.send_message(embed=emb)

    @disnake.ui.button(label="VanishStoun", style=disnake.ButtonStyle.blurple, emoji="🧁", row=2)
    async def manual2(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='VanishStoun | Иван',
                            description='**———————————————————————————————**\n')
        emb.add_field(
            name='Всем привет. Меня зовут Максим. Являюсь разработчиком данного проекта. Все баги - моя забота. Многого сказать не смогу о себе, но скажу главное... Я начинал заниматься созданием серверов с \n12-и лет.',
            value='ㅤ')
        emb.add_field(
            name='Было куча падений, куча неудач, но это опыт! И вот сейчас, я набрался достаточно опыта для открытия не маленького проекта.\nНадеюсь Вам понравится наше творение!',
            value='ㅤ', inline=True)
        emb.set_image(
            url='https://ic.wampi.ru/2022/11/26/CUPcqkeee.png')
        emb.set_footer(text='«Лучший выход всегда через». ©️ Роберт Фрост',
                       icon_url='https://minecraft-heads.com/media/k2/items/cache/a50d832102cc6e332d683d2706cedf12_XS.jpg')
        await ctx.response.send_message(embed=emb)

    @disnake.ui.button(label="Rairon_Horner", style=disnake.ButtonStyle.blurple, emoji="💻", row=2)
    async def manual3(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='Rairon_Horner | Максим',
                            description='**———————————————————————————————**\n')
        emb.add_field(
            name='Всем привет. Меня зовут Максим. Являюсь разработчиком данного проекта. Все баги - моя забота. Многого сказать не смогу о себе, но скажу главное... Я начинал заниматься созданием серверов с \n12-и лет.',
            value='ㅤ')
        emb.add_field(
            name='Было куча падений, куча неудач, но это опыт! И вот сейчас, я набрался достаточно опыта для открытия не маленького проекта.\nНадеюсь Вам понравится наше творение!',
            value='ㅤ', inline=True)
        emb.set_image(
            url='https://ic.wampi.ru/2022/11/26/CUPcqkeee.png')
        emb.set_footer(text='«Лучший выход всегда через». ©️ Роберт Фрост',
                       icon_url='https://minecraft-heads.com/media/k2/items/cache/a50d832102cc6e332d683d2706cedf12_XS.jpg')
        await ctx.response.send_message(embed=emb)
        
        
        
    @commands.slash_command(name="dev", description="Команда проекта MineSkills")
    async def dev(self, ctx):
        view = DevMenu()
        emb = disnake.Embed(title='Команда проекта MineSkills',
                            description='Ниже будет предоставлены кнопки выбора\n определённого члена команды\nВыбор лежит лишь за Вами.')
        emb.set_image(url='https://i.gifer.com/4Cb2.gif')
        await ctx.response.send_message(embed=emb, view=view)


def setup(bot: commands.Bot):
    bot.add_cog(DevMenu(bot))
    print(f">Extension {__name__} is ready")
