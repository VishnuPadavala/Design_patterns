
**Problem Faced Without Factory Pattern in Adapter**

1. Client Knows Too Many Classes
   SBI
  SBIAdapter
  HDFC
  HDFCAdapter
  ICICI
  ICICIAdapter
2. Modification Required for Every New Bank
  Suppose Axis Bank is introduced.
  axis = AxisAdapter(Axis())
3. Object Creation Logic is Scattered
   sbi = SBIAdapter(SBI())
  hdfc = HDFCAdapter(HDFC())
  icici = ICICIAdapter(ICICI())
  
  If the creation process becomes complex, many files must be updated.

  **Solution Using Factory Pattern**

  1.Move all creation logic into a single class.
  
  example:-
    class BankFactory:

    @staticmethod
    def get_bank(bank_name):

        if bank_name == "sbi":
            return SBIAdapter(SBI())

        elif bank_name == "hdfc":
            return HDFCAdapter(HDFC())

        elif bank_name == "icici":
            return ICICIAdapter(ICICI())

2. Centralized Object Creation
 
  All creation logic is in one place BankFactory.
  No duplication across the application.


3. Reduced Coupling
  PhonePe
     |
     v
  BankFactory
     |
     v
  Adapters
     |
     v
  Banks
  
  PhonePe no longer depends directly on specific bank classes




