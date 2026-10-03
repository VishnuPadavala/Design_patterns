from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def transfer(self,amount):
        pass

class SBI:
    def get_balance(self):
        print("SBI balance is 10000")
    def send_money(self, amount):
        print(f"SBI transferred {amount} successfully")
class SBIAdapter(Bank):
    def __init__(self, sbi):
        self.sbi=sbi
    def check_balance(self):
        self.sbi.get_balance()
    def transfer(self, amount):
        self.sbi.send_money(amount)
class HDFC:
    def get_balance(self):
        print("HDFC balance is 20000")
    def send_money(self, amount):
        print(f"HDFC transferred {amount} successfully")
class HDFCAdapter(Bank):
    def __init__(self, hdfc):
        self.hdfc=hdfc
    def check_balance(self):
        self.hdfc.get_balance()
    def transfer(self, amount):
        self.hdfc.send_money(amount)

class phonepe:
    def check_balance(self,bank):
        bank.check_balance()
    def transfer(self,bank,amount):
        bank.transfer(amount)

class BankFactory:
    @staticmethod
    def get_bank(cls, bank_type):
        if bank_type == "SBI":
            return SBIAdapter(SBI())
        elif bank_type == "HDFC":
            return HDFCAdapter(HDFC())
        else:
            raise ValueError("Invalid bank type")

def main():
    phonepe_app=phonepe()
    sbi=BankFactory.get_bank("SBI")
    hdfc=BankFactory.get_bank("HDFC")
    phonepe_app.check_balance(sbi)
    phonepe_app.check_balance(hdfc)
    phonepe_app.transfer(sbi,5000)
    phonepe_app.transfer(hdfc,10000)