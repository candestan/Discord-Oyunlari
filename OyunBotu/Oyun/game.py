import parser
class DiscordOyunlari():
    def __init__(self, DISCORD_BOT, GAMENAME="", OBJECTIVE=""):
        self.GameLocation = "../Temalar/%s"%(GAMENAME)
        self.Theme = parser.ThemeParser(self.GameLocation)
        self.Bot = DISCORD_BOT
