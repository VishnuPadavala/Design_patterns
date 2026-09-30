
**Prototype Design Pattern**

The Prototype Design Pattern is a **Creational Design Pattern.**

Instead of creating a new object **from scratch using new**, we create a **copy (clone)** of an existing object.

**Real-Life Example:-**

__Imagine a company form:__

Employee 1 form → Name: Vishnu, Department: CSE, Salary: 50000
Employee 2 form → Almost same details

Instead of filling the entire form again, you **photocopy** the first form and change only the required fields.

This **photocopy idea** is the **Prototype Pattern.**


__impoertant concept in the prototype is that__

**Deep Copy vs Shallow Copy**

**Shallow Copy:-**

If one object changes a nested object, the other may also be affected.

i have an object obj1--->Address--->22341
i copy the obj1 to obj2,obj2--->Address--->(22341)(it will be same,if you modify one object it will reflect the all the objects)

**Deep copy**

if copy the object with diffrent Address (means it will not affect the other objects)
Example:-

i have an object obj1--->Address--->22341
i copy the obj1 to obj2,obj2--->Address--->(it will be Diffrent)(22437)

**Advantages**

fast object creation(insted of creating the object from the scratch it will clone(copy) it.)
Reduces Repeated Initialization Code
Hides Complex Object Creation
Less Memory and Processing Overhead(If initialization is expensive, cloning saves CPU time and resources.)
