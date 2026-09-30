from openAI_factory import openAI_factory
def main():
    s1=openAI_factory.getinstance("openAI")
    s2=openAI_factory.getinstance("chatgpt")
    s1.chat()
    s2.chat()
if __name__=="__main__":
    main()