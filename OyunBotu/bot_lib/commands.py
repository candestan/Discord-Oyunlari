#-*-coding:utf-8-*-
import discord
import datetime
from discord.ext    import commands
from time           import sleep
import datetime

class OyunYonetim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="kayitac",pass_context=True)
    @commands.has_role('Yetkili')
    async def kayitac(self, ctx, arg1, arg2, arg3):
        selected_time = datetime.datetime.strptime("%s %s"%(arg1,arg2), '%Y.%m.%d %H:%M')
        str_time = selected_time.strftime("%Y.%m.%d %H:%M")
        embed=discord.Embed(color=0x327da8, title="Oyun kayıtları aıçılmıştır. Oyun tarihi: \n```%s```"%(str_time))
        embed.set_author(name="%s - Oyun Kayıtları"%(ctx.guild.name), icon_url=ctx.guild.icon_url)
        embed.add_field(name = "Kayıt olmak için gereksinimler:" ,value="- Etkinlik anında burada hazır olmanız gerekmektedir.\n- Onaylanmış bir oyuncu olmanız gerekmektedir.", inline=False)
        embed.add_field(name = "Bu haftanın teması" ,value="%s"%(arg2), inline=False)
        channel = self.bot.client.get_channel(773617532519055450)
        await channel.send(embed=embed)
        activity = discord.Activity(type=discord.ActivityType.streaming, name="Discord Oyunları - Kayıtlar Açıldı!", url="https://www.twitch.tv/ProtonCrasher")
        await self.bot.client.change_presence(status=discord.Status.online, activity=activity)
class Admin(commands.Cog):
    """Sadece adminlerin kullanabileceği komutlar"""
    def __init__(self,bot):
        self.bot=bot
    @commands.command(name="reload",pass_context=True)
    @commands.has_role('Yetkili')
    async def reload(self, ctx):
        self.bot.Reload()
        await ctx.send("OK.")
        await ctx.message.delete()