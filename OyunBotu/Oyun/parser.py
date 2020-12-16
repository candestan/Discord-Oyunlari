import json
class ThemeParser():
    INTERFACE = {
            "Theme":{
                "Name": str,
                "Difficulty": int,
                "Details": str,
                "Objective": str,
                "Roles": {
                    str:[
                        {
                            "Name": str,
                            "Count_Per_Game": int,
                            "IsImportant": bool
                        }
                        ]
                },
                "Steps":{
                    str:[
                        {
                            "StoryText": str,
                            "IsAllMuted": bool,
                            "BlockCount": int,
                            "VictimsRoleName": str
                        }
                    ]
                }
            }
        }
    def __init__(self, DIR=""):
        self.ThemeDirectory = DIR
    def Load(self):
        with open(self.ThemeDirectory) as json_file:
            data = json.loads(json_file)
            if(self.ControlTheme(self.INTERFACE,data)):
                self.DATA = data
                #+ SUCCESS MESSAGE
            else:
                pass#+ FAILED MESSAGE
    def ControlTheme(self,interface,control_dict,i=0):
        for key in interface:
            result_key = key in control_dict
            # Type oriented key input check
            if(key in [str,bool,int,float]):
                target_type = key
                checkBuffer = []
                for key_target in control_dict:
                    checkBuffer.append(type(key_target) == target_type)
                result_key = all(checkBuffer)
            
            if(type(interface) == dict):
                value = interface[key]
            #Type oriented value input check
            if(value in [str,bool,int,float] and result_key):
                # print("value") # FOR DEBUG
                if(not type(control_dict[key]) == value):

                    # print(control_dict,interface) # FOR DEBUG
                    # print("yes 1,",i) # FOR DEBUG
                    return False
                # print("okay 1") # FOR DEBUG
                continue
            else:
                pass#MAYBE FAILED
            # Dict oriented value input check
            if(type(value) == dict and result_key):
                # print("dict") # FOR DEBUG
                if(key in [str,bool,int,float]):
                    for i_n in control_dict:
                        if(not self.ControlTheme(value,control_dict[i_n],i+1) or key != type(i_n)):
                            # print("yes 2.-1") # FOR DEBUG
                            return False
                    continue
                state = self.ControlTheme(value,control_dict[key],i+1)
                if(not state):
                    # print("yes 2,") # FOR DEBUG
                    return False
                # print("okay 2") # FOR DEBUG
                continue
            else:
                pass# Maybe Failed
            if(type(value) == list and type(value) == list):# List Oriented
                # print("list") # FOR DEBUG
                sample = value[0]
                sample_type = type(sample) if not sample in [str,bool,float,int] else sample
                # print(sample_type ) # FOR DEBUG
                if(sample_type == dict):
                    for l_target_value in control_dict[key]:
                        if(not self.ControlTheme(sample,l_target_value,i+1)):
                            # print("yes 3",i) # FOR DEBUG
                            return False
                    # print("okay 3") # FOR DEBUG
                    continue
                if(sample_type in [str,bool,int,float]):
                    # print("as",control_dict[key]) # FOR DEBUG
                    for l_target_value in control_dict[key]:
                        if(type(l_target_value) != sample_type):
                            return False
                    continue
            # print(key,value) # FOR DEBUG
            # print("yes 4") # FOR DEBUG
            return False
        return True
    def GetName(self):
        return self.DATA["Theme"]["Name"]
    def GetDifficulty(self):
        Difficulties = {
            1: "Easy",
            2: "Medium",
            3: "Hard",
            4: "EXTREME"
        }
        return Difficulties.get(self.DATA["Theme"]["Difficulty"], "Unknown Difficulty")
    def GetDetails(self):
        return self.DATA["Theme"]["Details"]
    def GetRoles(self):
        buffer = []
        for p in self.DATA["Theme"]["Steps"]:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')