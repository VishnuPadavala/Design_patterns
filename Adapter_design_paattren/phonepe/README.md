
**PhonePe allows users to check account balances and transfer money using different banks such as SBI, HDFC, ICICI, and Axis Bank.**

Each bank provides its own API with different method names and interfaces. For example:

SBI provides get_balance() and send_money()
HDFC provides fetch_balance() and make_payment()
ICICI provides balance_inquiry() and transfer_funds()

Because of these differences, PhonePe cannot directly interact with every bank using a common set of methods.

**PhonePe wants all banks to support a standard interface:**

check_balance()
transfer(amount)

**creating the Adapter for each and every bank and then the treams and methodname will be same as phonepe method inside Adapter will call the diffrent metjos According to the Bank(SBI,HDFC,Axis Banks).**

to use this Better we use both **Adapter+Factory** to maintain all the bank in the same Factor to avoid the object creation to the cilent.
