**Problem Statement**

You are developing an AI platform that supports multiple AI providers such as:

OpenAI
ChatGPT
Gemini
Claude

The client application should be able to create and use any AI provider without being tightly coupled to concrete classes.

**soluton:-**

AI Platform will use this OpenAI,ChatGPT insted of there developing them(developing the LLM will take time and cost to resreach about information so simply integrating them into the project is simple)

__First one:-__
creating the separate classes for the OpenAI,ChatGPT etc will miss some method 
example:-
OpenAI will have (chat,resumeAnalysis,imagegenation)
ChatGPT will have (chat,imagegenaration)-->it will miss the resumeAnalysis.

so them we follow the **Interface Segregation Principle (ISP).**:-

we have to create an interface to all the LLM's(which will have chat,resumeAnalysis,imagegenation and etc)
so that all the LLM's will must implement them in there classes.
by this it will ensure that **Liskov Substitution Principle (LSP)** also be sacticifed.

okay its do,

__second one:-__
When a client wants to create an instance of OpenAI or ChatGPT without needing to know the exact class names, internal setups, or hidden logic, you should use the Factory Design Pattern

in this all the LLM's are stored in the Factory and cilent will call the Factor and open the LLM's without knowing the internal logic of creation of the object.

__this is the Simple Factory Desgin beacuse:-__

the program violate the OCP rule by having the mutiple if-else statments

