import datetime
import time

import disnake
from disnake.interactions import message

from config import settings

from disnake.ext import commands
from disnake import Button, ButtonStyle, member, user, Client, client

bot = commands.Bot(command_prefix=settings['prefix'], intents=disnake.Intents.all())


@commands.has_permissions(administrator=True)
@bot.command(name='clear')
async def clear(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.response.send_message(f"{ctx.author.mention}, {amount} Сообщение было удалено!", delete_after=1.5)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.response.send_message(f'{ctx.author.mention}, У вас недостаточно прав!', delete_after=0.5)
    else:
        raise error


@commands.has_permissions(administrator=True)
@bot.slash_command(name='ban', description='Бан участника')
async def ban(ctx, member: disnake.Member, reason=None):
    await member.ban(reason=reason)
    # await ctx.response.send_message(f"{ctx.member.ban} Был успешно забанен администратором {ctx.author.mentuin}")


@commands.has_permissions(administrator=True)
@bot.slash_command(name='kick', description='Кик участника')
async def kick(ctx, member: disnake.Member, *, reason):
    channel = bot.get_channel(789968921432031272)
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
async def kick(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.response.send_message(f'{ctx.author.mention}, У вас недостаточно прав!', delete_after=0.5)
    else:
        raise error


class HelpMenu(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

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
        emb.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
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
        emb.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
        await ctx.response.send_message(embed=emb, delete_after=30)


@bot.slash_command(name="menu", description="Вывод меню с выбором команд")
async def menu(ctx):
    view = HelpMenu()
    embed = disnake.Embed(colour=disnake.Colour.blue(), title="Помощь по моим командам")
    embed.add_field(name="Ниже будут предоставлены кнопки выбора \nНажмите на одну из понравившейся Вам\n",
                    value="\nПриятной Вам игры на **MineSkills**!", inline=True)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
    embed.set_image(url="https://i.gifer.com/7Zc6.gif")
    await ctx.response.send_message(embed=embed, view=view)


class DevMenu(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

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


@bot.slash_command(name="dev", description="Команда проекта MineSkills")
async def dev(ctx):
    view = DevMenu()
    emb = disnake.Embed(title='Команда проекта MineSkills',
                        description='Ниже будет предоставлены кнопки выбора\n определённого члена команды\nВыбор лежит лишь за Вами.')
    emb.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
    emb.set_image(url='https://i.gifer.com/4Cb2.gif')
    await ctx.response.send_message(embed=emb, view=view)


@bot.event
async def on_ready():
    print(f'{settings["author"]}, Я запустился и готов к работе!')


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


# mute
@bot.command()
@commands.has_permissions(administrator=True)
async def user_mute(ctx, member: disnake.Member):
    await ctx.channel.purge(limit=1)
    await member.timeout_for()


# Старт бота
bot.run(token=settings['token'])
