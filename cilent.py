from config_mannager import config_mannager
from api_info import api_info

def main():
    chartbot=config_mannager()
    resume_cls=config_mannager()
    chartbot.set_apikey('X-120')
    chartbot.set_model('GPT-4')
    chartbot.set_max_tokens(50000)
    print("After remove the instance of the chatbot")
    print(chartbot.get_apikey()," ",chartbot.get_model()," ",chartbot.get_max_tokens())
    print(chartbot is resume_cls)
    config_mannager.remove()
    document=config_mannager()
    print(chartbot is document)
    print("document info")
    document.set_apikey('Y-120')
    document.set_model('GPT-5')
    document.set_max_tokens(60000)
    print(document.get_apikey()," ",document.get_model()," ",document.get_max_tokens())
    print("After remove the instance of the chatbot")
    print(chartbot.get_apikey()," ",chartbot.get_model()," ",chartbot.get_max_tokens())
    assesment=config_mannager()
    print("assement info")
    print(assesment.get_apikey()," ",assesment.get_model()," ",assesment.get_max_tokens())
if (__name__=='__main__'):
    main()