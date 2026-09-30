from openAI import openAI
from chatgpt import chatgpt
class openAI_factory:
    @classmethod
    def getinstance(self,name):
        if name=="openAI":
            return openAI()
        elif name=="chatgpt":
            return chatgpt()
        else:
            print("No charcilent")