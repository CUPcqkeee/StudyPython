import datetime
import os
import disnake

from config import settings

from disnake.ext import commands

bot = commands.Bot(command_prefix=settings['prefix'], intents=disnake.Intents.all())
bot.remove_command('help')


# Меню с выбором кнопок
# class HelpMenu(disnake.ui.View):
#     def __init__(self):
#         super().__init__()
#
#     @disnake.ui.button(label="Инструкция", style=disnake.ButtonStyle.blurple, emoji="📃")
#     async def manual(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
#         emb = disnake.Embed(title='Инструкция',
#                             description="Чтобы попасть к нам на сервер, \nВам нужно пройти несколько этапов",
#                             colour=disnake.Colour.purple())
#         emb.add_field(name="1) Приобрести проходку на нашем сайте:", value="https://mineskills.net", inline=False)
#         emb.add_field(
#             name=f"2) Присоединится к нашему дискорд серверу:",
#             value="https://discord.gg/peseGDVf", inline=False)
#         emb.add_field(name="3) Пройти регистрацию на сервере:", value="/register [пароль] [повторение пароля]",
#                       inline=False)
#         emb.add_field(name="4) Привязать аккаунт Discord к аккаунту Minecraft:",
#                       value="Нажмите по NPC с названием «ВЫЖИВАНИЕ»", inline=False)
#         emb.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
#         await inter.send(embed=emb, delete_after=30, ephemeral=True)
#
#     @disnake.ui.button(label="MineSkills", style=disnake.ButtonStyle.success, emoji='🌎')
#     async def mineskills(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
#         emb = disnake.Embed(title='О проекте:',
#                             description='Здесь я не буду описывать всю информацию о сервере, \nВам будет интереснее самим зайти и ощутить всю атмосферу игры!\nНо расскажу пару интересных механик сервера:',
#                             colour=disnake.Colour.purple())
#         emb.add_field(name='• На проекте имеются 300+ **уникальных зачарований**',
#                       value='/enchants | /ecogui для подробностей', inline=False)
#         emb.add_field(name='• На проекте имеются 15+ **уникальных питомцев** со своими эффектами',
#                       value='/pet | /pets для подробностей', inline=False)
#         emb.add_field(name='• На проекте нет привата, имеются ***правила привата***',
#                       value='Перейдите в раздел <#999336237250904114>', inline=False)
#         emb.add_field(name='• На проекте **отсутствует** донат, имеется только МайнПасс',
#                       value='/bp | /battlepass для подробностей', inline=False)
#         emb.add_field(name='• На проекте имеются **кастомные** предметы',
#                       value='Для подробностей подойдите к NPC "Рецепты"', inline=False)
#         emb.add_field(name='• Проект построен полностью на доверии, просьба ознакомиться с правилами!',
#                       value='Перейдите в раздел <#999336237250904114>', inline=False)
#         emb.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
#         await inter.send(embed=emb, ephemeral=True)
#
#
# @bot.slash_command(name="меню", description="Вывод меню с выбором команд")
# async def menu(ctx):
#     view = HelpMenu()
#     embed = disnake.Embed(colour=disnake.Colour.blue(), title="О проекте:")
#     embed.add_field(name="Ниже будут предоставлены кнопки выбора",
#                     value="\nНажмите на одну из понравившейся Вам", inline=True)
#     embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
#     embed.set_image(
#         url="https://media.discordapp.net/attachments/1024063231603511350/1024267835385577532/2022-09-27_13-22-20_Trim.gif")
#     await ctx.response.send_message(embed=embed, view=view)


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.author.send(f"Файл >> {extension} << был успешно загружен!")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.author.send(f"Файл >> {extension} << был успешно выгружен!")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.author.send(f"Файл >> {extension} << был успешно перезагружен!")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# Старт бота
bot.run(token=settings['token'])
