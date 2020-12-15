import json
class ThemeParser():
    def __init__(self, DIR=""):
        self.ThemeDirectory = DIR
    def Load(self):
        with open(self.ThemeDirectory) as json_file:
            data = json.load(json_file)
            self.DATA = data
    def GetName(self):
        return self.DATA["Theme_Name"]
    def GetDifficulty(self):
        Difficulties = {
            1: "Easy",
            2: "Medium",
            3: "Hard",
            4: "EXTREME"
        }
        return Difficulties.get(self.DATA["Theme_Difficulty"], "Unknown Difficulty")
    def GetDetails(self):
        return self.DATA["Theme_Details"]
    def GetRoles(self):
        buffer = []
        for p in self.DATA["Theme_Steps"]:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')