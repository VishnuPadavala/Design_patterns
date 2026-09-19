from abc import ABC,abstractmethod

class api_info(ABC):
    @abstractmethod
    def set_apikey(self,api):
        pass
    @abstractmethod
    def get_apikey(self):
        pass
    @abstractmethod
    def set_model(self,model):
        pass
    @abstractmethod
    def get_model(self):
        pass
    @abstractmethod
    def set_max_tokens(self,max_token):
        pass
    @abstractmethod
    def get_max_tokens(self):
        pass