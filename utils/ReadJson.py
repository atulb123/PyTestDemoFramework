import json,os
class ReadJson:
    @staticmethod
    def getUserData(userType):
        with open(os.getcwd()+"/testData/userData.json") as f:
            userTypes=json.load(f)
            return dict(list(filter(lambda v:v['userType']==userType,userTypes))[0])
    @staticmethod
    def getConfigData(key):
        with open(os.getcwd()+"/testData/config.json") as f:
            return json.load(f).get(key)
