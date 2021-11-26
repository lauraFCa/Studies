# Course **Learning C#**

**.NET** = library that works with several languages (just for microsoft plataforms)  
**.NET Core** = multiplataform (windows, linux, mac)

> foreach(var nome in collectionNomes)

Refactoring: making the code smaller/better for mantainence

CAN  
var student = new Student()  
CANNOT  
int x = null

A variable that holds an object type is a REFERENCE type  
A variable that holds an int type is a VALUE type

Reference: something that points to a memory location (doesn't actually contain the value)  
Each time we use a new keyword we ocupy memory

**Memory Leak:** when a variable is no longer usefull (just ocupy space) - .NET Garbage Collector checks for all unreferenced objects and delete them

Declaring variables os value type (int) have pre set size, or pre allocated (Stack - simpler memory managment)  
References have dinamic memory allocation

## Interfaces

I want a class to have some of the methods from another class, but not all.  
CAN inherit from 1 class, and from multiple interfaces  
- Inherit from interface is restricting the definition of the class that uses the interface  
  - for a class to use the interface, they must use method (must have the "same" function - shcool system > principal.cs)

Can create a list with all classes that use an Interface!  
So I can have diferent types of objects through an Interface (and other methods and functions are unaccessable)

Interfaces can't have implemented functions
Abstract class is a mix of regular classes and interfaces. 

## Anonymous Data

Good for non SQL databases  
Allow to create an object without creating a class for that obj  
var someObj = new { name = "alex", age = 54 };  

## Lambda Expressions

(student) => { return (student.Name == "Jim"); }  
Function have no name  

## Asynchronous Code

Methods work on separate threads  

## String Interpolation

Add $ in front of string  
> $"Mensagem: {msg}"  

<br>

# Course **C++: Orientação a Objetos - Introdução**

//TODO