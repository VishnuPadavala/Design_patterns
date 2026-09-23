from abstractpro import prototypeabstrac
from copy import deepcopy
class prototype(prototypeabstrac):
    def __init__(self):
                self.company_name="ABC"
                self.company_addrees="Hydrabab"
                self.employee_name=""
                self.employee_id=0
    def clone(self):
          return deepcopy(self)
    @classmethod
    def getconfiguration(cls):
        return cls()
    def set_employeename(self,name):
        self.employee_name=name
    def set_employeeid(self,id):
        self.employee_id=id
    def display(self):
          print("employee name is--> ",self.employee_name)
          print("employee id is---> ",self.employee_id)