from api_info import api_info
class config_mannager(api_info):
    _instance=None
    def __new__(cls):
        if (cls._instance is None):
            cls._instance=super().__new__(cls)
            cls._instance.info={}
        return cls._instance
    def set_apikey(self, api):
        self.info['api']=api
    def get_apikey(self):
        return self.info['api']
    def set_model(self, model):
        self.info['model']=model
    def get_model(self):
        return self.info['model']
    def set_max_tokens(self, max_token):
        self.info['max_token'] = max_token
    def get_max_tokens(self):
        return self.info['max_token']
    @classmethod
    def remove(cls):
        cls._instance=None