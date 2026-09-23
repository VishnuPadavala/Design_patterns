from abc import ABC,abstractmethod
class prototypeabstrac(ABC):
    @abstractmethod
    def clone(self):
         pass
    @abstractmethod
    def set_employeename(self,name):
          pass
    @abstractmethod
    def set_employeeid(self,id):
          pass
    @abstractmethod
    def display(self):
         pass
