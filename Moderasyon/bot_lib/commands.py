#-*-coding:utf-8-*-
import discord
import datetime
from discord.ext    import commands
from time import sleep
from lib.settings import ANNOUNCMENT_CHANNEL, GAMME_ANNOUNCMENT, TEST_CHANNEL, LOG_CHANNEL, RULES_CHANNEL
class ModKomutlari(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="clear",pass_context=True)
    @commands.has_role('Yetkili')
    async def clear(self, ctx, *args):
        await ctx.channel.purge(limit=100)
        await self.bot.client.get_channel(LOG_CHANNEL).send("```%s, %s isimli yerde temizleme komutu kullandı.```"%(ctx.author, ctx.channel))
    @commands.command(name="duyuru",pass_context=True)
    @commands.has_role('Yetkili')
    async def duyuru(self, ctx, *args):
        embed = discord.Embed(color=0x00FF00, title="%s"%(' '.join(args)), description="@everyone")
        embed.set_author(name="Duyuru", icon_url=ctx.guild.icon_url)
        embed.set_footer(text="%s (%s) tarafından"%(ctx.author, ctx.author.display_name), icon_url="https://cdn.discordapp.com/avatars/%s/%s.png?size=1024" %(ctx.author.id, ctx.author.avatar))
        embed.set_thumbnail(url="http://pngimg.com/uploads/megaphone/megaphone_PNG98.png")
        await self.bot.client.get_channel(ANNOUNCMENT_CHANNEL).send(embed=embed)
        await self.bot.client.get_channel(LOG_CHANNEL).send("```ß%s bir duyuru gönderdi: \n%s```"%(ctx.author, ' '.join(args)))
        await ctx.message.delete()
    @commands.command(name="oyunduyuru",pass_context=True)
    @commands.has_role('Yetkili')
    async def oyunduyuru(self, ctx, *args):
        embed = discord.Embed(color=0xFF0000, title="%s"%(' '.join(args)), description="@everyone")
        embed.set_author(name="Oyun Ile Alakalı Duyuru", icon_url=ctx.guild.icon_url)
        embed.set_footer(text="%s (%s) tarafından"%(ctx.author, ctx.author.display_name), icon_url="https://cdn.discordapp.com/avatars/%s/%s.png?size=1024" %(ctx.author.id, ctx.author.avatar))
        embed.set_thumbnail(url="http://pngimg.com/uploads/megaphone/megaphone_PNG98.png")
        await self.bot.client.get_channel(GAMME_ANNOUNCMENT).send(embed=embed)
        await self.bot.client.get_channel(LOG_CHANNEL).send("```%s bir oyun duyurusu gönderdi: \n%s```"%(ctx.author, ' '.join(args)))
        await ctx.message.delete()
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
    @commands.command(name="kuralyolla",pass_context=True)
    @commands.has_role('Yetkili')
    async def kuralyolla(self, ctx):
        embed = discord.Embed(color=0xe3e6e5, description="Oyun kuralları aşağıda mevcuttur.")
        embed.set_author(name="Oyun Kuralları ve Oynanışı", icon_url = ctx.guild.icon_url)
        embed.add_field(name=":joystick: Oynanış", value="İlk olarak oyuncular belirlenir ve oyun odasına moderatör tarafından alınırlar. Rol atamaları yapılır ve rastgele olarak sayısı önceden belirlenmiş miktarda hainler dağıtılır. O haftanın hikayesine göre oyun temasına uygun olarak herkes önceden belirtilen hedeflere ulaşmaya çalışır. Oyun sırasında size engeller sunulacak ve bunlar oyunun oynayışını etkileyecektir. Oyunda senaristlerimizin hazırladığı birkaç son ile beraber herkese iyi eğlenceler diliyoruz!", inline=False)
        embed.add_field(name=":pencil: Kurallar", value="""
        - Oyun içi roleplay halinin tamamen dışına çıkmak yasaktır.
        - Oyunu alternatif bir evren gibi düşünebilirsiniz. Ama kendi hayatınızdan detaylar da katabilirsiniz.
        - Oyunda insanların seçimine karışmak kesinlikle yasaktır.
        - Saygısızlık & Hakaret vs. direkt olarak men sebebidir.
        - Siyasi & dini & ırki konular kesinlikle konuşmaya dahi açıktır. Gündem hakkında sohbet edebilirsiniz...
        - Burası oyun dışı hiç bir sohbete açık değildir. Oyun içinde normal konuşabilirsiniz. Çünki alternatif bir evrende yaşadığınızıı hayal ediyorsunuz. Konuşma burdaki en doğal hareket...
        """, inline=False)
        embed.set_thumbnail(url="https://www.wpclipart.com/cartoon/robot/robot_2/robot_rules_T.png")
        embed.set_footer(text="%s (%s) tarafından"%(ctx.author, ctx.author.display_name), icon_url="https://cdn.discordapp.com/avatars/%s/%s.png?size=1024" %(ctx.author.id, ctx.author.avatar))
        await self.bot.client.get_channel(RULES_CHANNEL).send(embed=embed)
        await self.bot.client.get_channel(LOG_CHANNEL).send("```%s kuralları tekrar gönderdi```"%(ctx.author))
        await ctx.message.delete()