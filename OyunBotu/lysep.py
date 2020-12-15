#-*- coding:utf-8
import discord
import asyncio
import importlib
import lib.commands         as cogs
from discord.ext.commands   import MissingPermissions, CommandNotFound
from discord.ext            import commands, tasks
class LysepBot():
    #region Initializors
    def __init__(self, INPUT_TOKEN="", INPUT_COMMAND_PREFIX="", INPUT_BOT_VERSION="", INPUT_THEME_COLOR_DEFAULT=0x0):
        self.client = commands.Bot(command_prefix=INPUT_COMMAND_PREFIX, help_command=None)
        self.InitializeBotFunctions()
        self.Token          = INPUT_TOKEN
        self.ThemeColor     = INPUT_THEME_COLOR_DEFAULT
        self.Prefix         = INPUT_COMMAND_PREFIX
        self.Version        = INPUT_BOT_VERSION
        self.COGS_STATE     = False
        print("[!] LYSEP yüklemesi...")
    def InitializeBotFunctions(self):
        self.InitializeEvents()
        self.LoadCogs()
        self.client.add_cog(cogs.Admin(self)) # Ayrı tuttum çünkü reloadlanmaması gereken tek COG
        print("[!] LYSEP Bot eylemleri tanımlamaları...")
    def InitializeEvents(self):
        @self.client.event
        async def on_ready():
            print("[!] Event: OnReady")
            await self.OnReady()
        @self.client.event
        async def on_command_error(ctx, error):
            if isinstance(error, CommandNotFound):
                return
            raise error
    #endregion

    #region Event Callbacks
    async def OnReady(self):
        self.activity = discord.Activity(type=discord.ActivityType.streaming, name="Discord Oyunları - Beklemede...", url="https://www.twitch.tv/ProtonCrasher")
        await self.client.change_presence(status=discord.Status.online, activity=self.activity)
        print("[!] Bot'un durumu düzenlendi.")
        self.avatar_url = "https://cdn.discordapp.com/avatars/%s/%s.png?size=1024" %(self.client.user.id, self.client.user.avatar)
        print("""
--------------------------------
├─  %s
    └── KULLANICI ID'SI :   %s
    └── VERSIYON        :   %s
    └── TEMA RENGI      :   #%06X
    └── KOMUT ISARETI   :   %s
    └── KUTUPHANE       :   %s.py
        └── Version :   %s.%s.%s
        └── Release :   %s
        └── Serial  :   %s
--------------------------------
"""%(self.client.user.name, self.client.user.id, self.Version, self.ThemeColor, self.Prefix, discord.__name__, discord.version_info[0], discord.version_info[1], discord.version_info[2], discord.version_info[3].upper(), discord.version_info[4]))
    #endregion
    
    def Start(self):
        self.client.run(self.Token)

    #region Functionals
    def LoadCogs(self):
        self.client.add_cog(cogs.OyunYonetim(self))
    def UnloadCogs(self):
        self.client.remove_cog('OyunYonetim')
    def Reload(self):
        if(not self.COGS_STATE):
            self.COGS_STATE=True
            self.UnloadCogs()
            importlib.reload(cogs)
            self.LoadCogs()
            self.COGS_STATE=False
    #endregion