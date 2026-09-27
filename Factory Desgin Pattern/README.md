**Factory Design Pattern is a Creational Design Pattern.**

_It provides an interface for creating objects without exposing the object creation logic to the client._

**main important think that is**

**Interview Answer**

If asked:

_"Does Factory Pattern violate OCP?"_

A good answer is:

  A Simple Factory implemented using large if-else or switch statements can violate OCP because the factory must be modified whenever a new product is added. However, the GoF Factory Method Pattern avoids this by introducing separate factory classes, allowing new products to be added through extension rather than modification.

**statment 1:-**
in any paymentapps use many payment apps like phonepay,gpay,pythm and Amazonpay etc..
if a class is **tightly coupled** and it is difficut that to pay by another paymentmethod

**In the Factory Design Pattren**

it will provides an interface for creating Object without exposing the **object creation logic** to the client.

**solution:**

payment class is an interface for the all payement classes.(interface)

phonepay,gpay,paythm,Amazonpay.(there are the class that abstract the interface and implemented in there own class)

paymentmethos class(this is class in which the cilent will not no that how the object will be created and will have multiple if--else if phonepay--->phonepay() class return)---------------->Factory

client class(it calls the paymenymethos by passing the methos there want to use without knowning that how the class will be created)

**Benifits:-**

losses coupled
Easy Maintenance (by adding the new classes)
Code Reusability

By using this the Factory(paymentmethod) are voilating the ocp rules **(Simple Factory)**

when we have to remove the if--else and separe the class by converting the paymentmethod class as interface separate the class phonepaymethod(),gpaymethod(),paythmmethod() and etc..........

when it follows the ocp rule **(Factory Method Pattren)**
