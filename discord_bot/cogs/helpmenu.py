import disnake
from disnake.ext import commands


class HelpMenu(commands.Cog, disnake.ui.View):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @disnake.ui.button(label="Инструкция", style=disnake.ButtonStyle.blurple, emoji="📃")
    async def manual(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='Инструкция',
                            description="Чтобы попасть к нам на сервер, \nВам нужно пройти несколько этапов",
                            colour=disnake.Colour.purple())
        emb.add_field(name="1) Приобрести проходку на нашем сайте:", value="https://mineskills.net", inline=False)
        emb.add_field(
            name=f"2) Присоединится к нашему дискорд серверу:",
            value="https://discord.gg/peseGDVf", inline=False)
        emb.add_field(name="3) Пройти регистрацию на сервере:", value="/register [пароль] [повторение пароля]",
                      inline=False)
        emb.add_field(name="4) Привязать аккаунт Discord к аккаунту Minecraft:",
                      value="Нажмите по NPC с названием «ВЫЖИВАНИЕ»", inline=False)
        emb.set_footer(text=commands.user.name, icon_url=commands.user.avatar)
        await ctx.response.send_message(embed=emb, delete_after=30)

    @disnake.ui.button(label="MineSkills", style=disnake.ButtonStyle.success, emoji='🌎')
    async def mineskills(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        emb = disnake.Embed(title='О проекте:',
                            description='Здесь я не буду описывать всю информацию о сервере, \nВам будет интереснее самим зайти и ощутить всю атмосферу игры!\nНо расскажу пару интересных механик сервера:',
                            colour=disnake.Colour.purple())
        emb.add_field(name='• На проекте имеются 300+ **уникальных зачарований**',
                      value='/enchants | /ecogui для подробностей', inline=False)
        emb.add_field(name='• На проекте имеются 15+ **уникальных питомцев** со своими эффектами',
                      value='/pet | /pets для подробностей', inline=False)
        emb.add_field(name='• На проекте нет привата, имеются ***правила привата***',
                      value='Перейдите в раздел <#1010904721105637396>', inline=False)
        emb.add_field(name='• На проекте **отсутствует** донат, имеется только МайнПасс',
                      value='/bp | /battlepass для подробностей', inline=False)
        emb.add_field(name='• На проекте имеются **кастомные** предметы', value='/ia для подробностей', inline=False)
        emb.add_field(name='• Проект построен полностью на доверии, просьба ознакомиться с правилами!',
                      value='Перейдите в раздер <#999336237250904114>', inline=False)
        emb.set_footer(text=commands.user.name, icon_url=commands.user.avatar)
        await ctx.response.send_message(embed=emb, delete_after=30)


def setup(bot: commands.Bot):
    bot.add_cog(HelpMenu(bot))
    print(f'>Extension {__name__} is ready')
