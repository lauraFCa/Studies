# Courses

## Course **JavaScript for QA Engineers and SDETs**

[Udemy Course](https://www.udemy.com/course/javascript-for-qa-engineers-and-sdets)

Definindo variável:  
var nome_variavel  

> " x " = string (aspas duplas ou simples)

var book1 = "Bee in the Hive";  
var book2 = "The secret life of the ant";  
var book3 = "Laptops. Not just for breakfast anymore";

> // comentario

/* comentario  
multiplas  
linhas */

//TODO finish the course

<br>

## Course **JavaScript Essencial Training**

[Linkedin Learning Course](https://www.linkedin.com/learning/javascript-essential-training)

**JavaScript: A scripting language for the web.**  
EVENTS (DOM = Document Object Model)  
Everything that happens in the browser are events  
> eventTarget.addEventListener(eventTarget, callback [, options])  
> Callback: function that will run when eventTarget is caught  
> Options = advanced (you may declare it false, so the default takes place)  

array.forEach() executes a provided callback function once for each item in the array;  
array.map() creates a new array with the results of executing a provided callback function once for each item in the original array;  
callback function dont take parameters, so I wrap it with another function  
> () => {lidToggle}

This way I can now pass parameters:  
lidToggle(param1, param2, param3)  
A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.  

VAR -> Global set variable  
If declared outside function, but it's reassinged inside a function it'll stil be valid for the hole document.  
Global and unchangable variable  

LET -> Local scope variable  
It can even have the same name as VAR but it'll only exist in a local scope
Used for changable scopes  

CONST -> Fixed variable, never changes  
Doesn't let you reassing values (browser "breaks")  
Editor doesn't let you know it's a problem, only browser  

UNDEFINED -> Type 1: variable not assigned | Type 2: defined as UNDEFINED
Using 3= (===) -> Look for ideal equality (will not consider 5 = "5")  
Using % -> Modules, used mostly for prime numbers  
Using ** -> Equivalent to power (2^2)  
Using increment -> Increment value (++a), (a++) First show variable ant then increment  

FUNCTION: a function that sits by itself  

METHOD: sits inside an object and works on this object  

Function declareted by constant (const functionName = function()) is good so you don't overwrite the function, even by accident  
Immediately Invoked Function Expression (IIFE): the function will run immediately after the browser loads, I don't have to call it.  

ARROW FUNCTIONS  
(a) => { return a + 100 }  
Function declarations can be hoisted = you can call the function before it's declared (imporper coding, but works), but Arrow Functions cannot.  
**Cant use arrow functions inside objects!**  
Reduced model: a => a + 100;  
Running a function inside a method, it get taken as a global scope (it'll return things globally)  
Arrow functions inside methods will return the parameters from inside (08_05), it doesnt have its own scope.  

CALLBACK: function sequencing -> way of making functions happen in a certain desired order.  
Ternary Operator:  
console.log( everydayPack.lidOpen ? "open":"closed" )  
Three distinc layers put together by he browser:  
1. HTML (content layer)
2. CSS rules (presenting layer)
3. JavaScript (interaction layer)

ECMAScript 2015, JavaScript, TypeScript, ES6, CoffeScript  
jQuery, AngularJS, React.js, Node.js  
Browser uses ECMAScript specifications to interpret JS  
Browsers are to slow to adopt technology  
Standart is ECMAScript 5.1  
> jQuery: js function library (simplifies js code)
> JS Front-end Frameworks: allow dev to build in browser apps that generates websites (Facebook runs on React)
> PhP generates the pages in the server and send to browser

These frameworks run in the browser and pull just the data from the server - makes them really fast, but
has significant drawback when js isn't working

> Node.js: js plataform build on browser runtime environments - allow to use js as a server site (js work beyond the browser)

Dev the code in ONE browser, but test on ALL BROWSERS  
JavaScript render blocking: Everytime a browser finds a js reference it stops loading and waits untill its downloaded and executed (can slow down the process)  
The defer keyword makes the browser wait until the document is loaded before running the JavaScript  
HTTP/2: allow the browser to download a lot o thing in paralel;  
Calling JS today: Load right away (render block), Load Asynchronous (script src="" async> - file download with html)-renderblock only when execute js, Load Deferred (only happens when everything else is load).

HOW TO WRITE GOOD CODE
1. Case sensitive
2. Camel case (name = umNome, objeto e classe = ObjetoClasse, constante = CONTANTE)
3. Whitespace matters (to human) - frase.grande = espaço + entre + elementos
4. End each statement with semicolon ; (makes reading easer)
5. Use comments

TROUBLESHOOTING  
Browser console is the primary Troubleshooting tool  
You can log anythonf from code to the console, to see what's going on
Console is a live code environment  
It gives the erros, the file with error and the line of the error.  
=> For errors inside functions it's better to use other trobleshooter tools.  
From the source (browser tab) I can add breakpoints to the file, to step through the code and see what's happening.  
Double click the line to debug in the browser and reload (with the "source" tab open)  
Pressing F9 I step through the code, line by line  
JSX = Extension to JS, that allows to output content in simple way (similar to Template Literal: no need to backticks nor dollar simbol in front of {})  
INSIDE THE METHODS CANNOT USE ARROW FUNCTION (exception: React)
