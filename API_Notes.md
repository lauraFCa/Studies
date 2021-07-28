# Couses

## Course **API Testing Foundation**

[Original Course GitHub](https://github.com/djwester/api-testing-foundations.git)
[NPM download](https://npmjs.com/get-npm)

Idempotency: You can repeat the same action over again but it'll always result in the same (state of the holder stay the same) - PUT and DELETE  
Safety: Action don't affect the state of holder (don't change anything on the server) - GET   

### Types of API
- REST  
Set of principles to make creating API  
Representation State Tranfer (consistenly apply actions to resources - nouns)  
- SOUP  
Simple Object Protocol Approach  
Follow stricted set of rules (more than REST API) - standard responses and request  
Any changes require ALL users to rebuild (less independency between server and client)  
- GraphQL  
Trying to bridge REST and SOUP  
- Hypermedia  
Term to describe a way of using REST API - the API tells you what it can and can't do  

*Authentication:* who you are (confirm identity)  
*Authorization:* what you can do (your permissions)  
*API Security:* checks Authorization and Authentication  

OAuth Workflow: way of athorizing an application  
- Application: send request to auth server to authenticate
- Auth server: sends a token to authenticate and authorize you
- Web Server: Application gets the token and send to the server, which validates
App -> Auth -> App -> Web

*Basic token:* Basic authentication
*Bearer token:* OAuth authentication

### Examples
Star Wars API - some examples of request
people/?search=hidden
- number of hidden elements
people/schema
- infos about the api data

PUT - Edit existing object (Can't modify ID)

> try: POST on existing id  
> expand object with "null"

**Test Doubles** - Stand in for the system  
Mocks, Stubs, Fakes  
New > Mockserver  
Create JSON data in text files, and organize into folders that fits the url structure of the API  
Can just reference them (those JSONs)  

### API Automation
Can use API to run test automation  
Extension of exploratory testing  
**Exploration:** lays the foundation for the automated test (about understanding what need to be investigated)  
Automation is based on things that will need to be repeated  
- Repeat things that don't change (ex: if other APIs are being used)

### Data Driven Testing
Check every endpoint (and combination)  
How to share data across tests?  
### Workflow driven
Series of API calls in sequency, mimiking what a customer might do  
How to pass data around?  

- Approach automation like coding (carefull with data)
- Don't automate everything
- What and Why it's being automated

### **Performance Testing**
API allows you to programatically access a funcionality in the system, given a real life feeling of usage  
Load testing, Speed testing, Request limit, Itens in a page limit, stress test.

#### Load/Stress test on parts of app

- See what happens when you have a 100 requests on a page
- Create a POST request with 100 iteration

#### Speed testing

- How long it takes for the server to respond
- Create a POST, send, and check "time" on Postman
- Can do this request on slow networks to see how it responds.
- Allows me to find areas to focus on during development

#### Security Testing

  - Not just authorization and authentication
  - Dont try to implement your own version. Use standart auth protocol
  - Vulnerabilities: SQL injecting, cross-site scripting
  - Check standart security points, but also more for APIs  
    - Areas of responsability: an attack can happen somewhere, but you can't find the part responsable for the "leak"
    - Cross-site scripting can be blocked by the API or by the cliente - we must check that one of them is bloking those requests
  
*Validation:* check all validation is correctly done!  
Some attacks just send random inputs to the API, or cycling through known lists of vulnerabilities  

### Testing Microserveces and IoT
Microserveces are API driven (each microserver is a small part and talk to each other through APIs)  
IoTs generally don't even have interfaces, so they comunicate through APIs.  

**Some Refs:**  
https://katrinatester.blogspot.com/  
https://github.com/DannyDainton/All-Things-Postman  
  
<br>
  
## Course **Learning REST APIs**

### **Módulo 01**

Representational State Transfer REST  
group of software architecture design constrains that brings efficient, reliable and scalable systems  
(data architecture methodology) - give verbs retur resourcs  
Application Programming Interace = API  
  
App can render new data without rendering the whole page  
**URL = Universal Resource Locator**  
- Subset of URI - identify resource and explains how to access (ftp / http) - my actual physical location  
- ***URI = Universal Resource Identifier**
    - Characters that identify a resource (generic method for naming and locating web resource)  
    - **URN = Universal Resource Name**
            - Any URI under with properties of name (unique name identifier)  
  
*Explicit URN:* oasis:names:spcification:doc  
Resource name: linkedin.com/learning/instructors  

http://site.com/autor/pagina.html#posts  
#post = resource  
URN = URL + resource  
URL might be a URN, both are URI  
  
**CONSTRAINS OF REST**  
1. Client-server architecture
Client manage interface, server manage data
Complete separation of content and presentation/interaction
2. Statelessness
No state (contex/info) can be stored on the server between requests
Cliente keep track of its own session state, all requests sent must be self contained and complete
If server needs to save state, it passes on to database or similar, for a time (ex: autentication token)
3. Cacheability
Storing responses for a period of time, all REST responses must be marked as cacheable or not
4. Layered System
Client cannot know wheter ir's directly connected to the server or others (escalability and security)
5. Code on demand
Servers transfer executable code and compile to/in the cliente
6. Uniform interface
  
- Must have resource identification in requests
- Must allow resource manipulation through representation (client can modify, control)
- Must issue self descriptive message
- Hypermedia as the Engine of App State (once cliente has access to REST service, msut be able to discover all resource and methods through hiperlink)
  
*RESTfull API = rund with HTTP (it's not a must)*
  
Clients who consume the REST API  
client = website / app (create and consume request)  
RestAPI: receive request, process data and send responses  
  
Most APIs have limits on who can access what  
Open APIs, a client must autenticate themselfs, and limits are imposed so the user don't overuse the server  

### **Módulo 02**

Request: method + URI (PUT + http://site.com)  
The request shuld include metadata: content type (required for REST API), user agent, language, autentication, cash control  
Also, send the actual data, if is wanted to update  
  
Good REST API has extensive documentation, but thanks to Hipermedia as engine the app constraint.  
To get the info on a REST API, you can use the GET method  
"OPTIONS url" --> give list with all methods available  

**Resource:**  
Abstract of information, if it can be named it's a resource (conceptual mapping to set of entities - not the entity)  
Conceptual Mapping: "red book in shelf number 4" (single), "all red books" (resource collections)  
  
**Representation:**  
REST perform action on resource by using representation to capture states and transfer representation between components.  
REST Server: generates unique representation of your book and modify to specifications  
  
**METHODS**
***GET*** - want to receive data  
***POST*** - send data to the server / create new resource and add to collection  
***PUT*** - send data to the server / update data (replace all existing data / replace)  
***PATCH*** - send data to the server / modify existing resource (not necessarly replacing everything)  
***DELETE*** - delete the specified resource (only able to do it to single - no collections)  
***OPTIONS*** - description of communication options for the target resource  
***HEAD*** - returns the head section of the response  

**RESPONSES:**  
Information - 1XX  
(tipically to ask the client to wait, or ask to continue)  
*Success - 2XX*  
- 200 = ok
- 201 = created
- 204 = no content (server returned "no content")
**Redirection - 3XX (new URL)**
- 301 = moved permanently
- 302 / 303 = found at this other URL
- 307 = temporary redirect
- 308 = resume incomplete (permanent redirect)
**Cliente Error - 4XX**
- 400 = bad request (request is malformed or too large)
- 401 = unauthorizes
- 403 = forbidden (request outright refused by the server - not logged in or don't have right permissions)
- 404 = not found
- 405 = method not allowed
- 409 = conflict (ex: already exist)
**Server Error - 5XX**
- 500 = internal server error (something went wrong at the server)
- 502 = bad getaway (server receive invalid response from whatever is trying to connect to)
- 503 = service unavailable (server is overloaded or down)

### **Módulo 03**

HEAD http://restful.dev/wp-json/wp/v2/posts  
Authorization: Basic username password  

### **Módulo 04**
Authorization: NEVER passed as clear text, it's encrypted  
In the response you can see the allowed methods  
filtering responses: www.site.com/posts?per_page=1  
www.site.com/posts/4  --> pega o post com id = 4  
  
With a POST request I must send **content** (type, ) and **authorization**  
In the content json (or whatever language), must include *title*, *content* and *status* ("publish" if I want to be public right away)  
  
> Any time you send a POST request it returns the entire source after creating (so the client can check erros and make sure everything worked properly)  
  
If I want to update the post I made, gotta know what method to use (PATCH, POST, PUT) - check with OPTIONS request  
*To update* using PUT, send only the data I want to change!  
*To delete* don't use collections, authorization is a must (sent an ID ex: ../post/1)  
The return status should be "trash" (or similar)  
  
**OBS:** The API tries to mimic the behavior of the app it's accessing.  
To delete completely, not just put on trash, use ?force=true (WORDPRESS EXEMPLE)  

!DELETE! = If the resource exists and you have the correct authorization, the resource is deleted or its status is changed on the server.  
  
<br>
  
## Course **Introduction to Web APIs**

**Aplication Programming Interface - API**

Request n Response cycle:  
Request: get (ask API for data)  
HTTP protocols (request verbs)  
- **GET:** get data sent to you
- **POST:** update data on the server
- **PUT:** add new data from server
- **DELETE:** delete data from server
  
Data format: XML and JSON  
JSON: Format data like obj in JS (most used)  
{"key": "value"} - JavaScript Object Notation  
  
> Data in response is "string"  
> Need to be object, so do parsing()  
> JSON.parse(responseFromAPI)  
> *Object can came as array, but it's still object (array of obj)  
> http://hplussport.com/api/products + JSON Formatter (extension)  
> typeOf  

Objects: have properties (model), actions (honk - method), object.innerObject.property  
  
**Make request:** XMLHttpRequest  

JQuery Ajax method of connecting to API  
Assynchronous JavaScript and XML (don't works only with XML)  
*OBS:* To use JQuery, must include in HTML < script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js">  
  
**FETCH**  
Build on promises  
A way to connect to an API  
**ENDPOINTS**  
Different places (locations) you can connect to the API (URLs)  
restaurant.com/salads  (location / endpoint)  
restaurant.com/appetizers  
restaurant.com/desserts  
  
**PARAMETERS**  
Helps define and/or filter responses (calories=light):  
restaurant.com/api/desserts?calories=light&allergy=dairy  
*Look for API documentation*

**API Key: control to use the API**  
META object:  
*Satus Codes:*
- 200s (ok)
- 300s (redirected to apropriet resource)
- 400s (problems on our end - client)
- 500s (problems on the server)

request.onerror = a way to deal with errors
  
<br>

## Course **API REST Youtube Course**

**API = Application Programming Interface**  
Interface de programação de aplicações, com objetivo de expor um serviço sem que as pessoas que consomem o serviço conheçam sua estrutura (conceito de caixa preta)  
OBS: API Local = download da API e uso dentro do software  
- Espera que outros softwares se comuniquem com ela (não foca na interface)
- Foco da API é ter boa interoperabilidade
- Protocolos REST ou SOAP: padrões a serem seguidos para desenvolvimento de API
- Troca de requisições respondem geralmente por JSON
- Serve para expor serviço de um software sem expor sua estrutura.

JPA: framework para simplificar a interação com BD  
Testar API: vai além de olhar envio de requisições e de respostas;
Interoperabilidade = essencial a API

Protocolo SOAP | Protocolo REST
--------- | ------
Simple Object Access Protocol | Estilo de arquitetura
Usa padrões HTTP e XML | Usa padrões HTTP, JSON (o mais leve), URL e XML
Maneira de expor lógica de negócio:  interfaces de serviços como @WebService | Necessários menos recursos e largura de banda (por usar mais padrões)
. | Maneira de expor lógica de negócio: REST aproveita a exposição da URL como @path (“/ WeatherService”)
  
<br>
  
- Services: camada dentro da aplicação que, geralmente armazena regra de negócio;  
- Repositories: camada responsável por trafegar informações entre regra de negócios do sistema de armazenamento (interface entre a aplicação e o banco de dados);  

Importante entender se a inconsistência está no Service ou no Repository, dependendo de onde está exige forma específica para lidar.  
Criando um software para buscar todas as viagens ou filtrar por região:

1.	Definir serviços, repository e tabelas necessários
2.	Criar métodos no service para buscar viagens
3.	Criar repository para intercessão com BD
4.	Repository faria requisição direta ao BD
5.	Implementar outro Service para buscar viagens respeitando filtro (método recebe parâmetro de filtro - região)

Repository recebe do service informação de query com WHERE  
Qualquer interface pode chamar um Service (back-end)  
API REST: forma que vai expor esses métodos de maneira remota para que outro software possa consumi-los  
API REST tem um controlador que intermedia a aplicação consumindo a API e os serviços do back-end.  

**Controller:** implementa a API REST buscando informações através dos serviços   (controller determina o que vem no método e o que ele precisa chamar)  
Intermediador entre aplicação e os serviços (e repositórios) - Postman  
Postman/interface -> controller -> service -> repository -> BD  

1.	Controller (é uma classe): disponível de maneira remota (HTTP), para pessoas autenticadas poderem fazer requisição
2.	Coloco anotações nos métodos: @requestMapping (value = endereço, method= GET/POST) -> value = endpoint
3.	Chamo service nos métodos [viagens - viagemervice.listar()]
4.	Método no controller retorna uma resposta:
5.	response.status(HttpStatus.OK).body(saidaDoMetodo)
6.	statusOk = 200

Método GET: Não altera nada no servidor (apenas uma busca) - método SAFE (retorna um statusCode)  

![Fluxo do Controller](imgs\fluxo.png)

Crio um controlador, que vai estar disponível via HTTP (de maneira remota) para que pessoas autenticadas e autorizadas possam realizar uma requisição e então ter acesso.  
REQUESTS E RESPONSES  
Curl: para enviar requisições via HTTP (via terminal)  
Token: serie de caracteres alfa numéricos que permitem que tenhamos acesso a algum endpoint  

- token pode representar, por exemplo, que sou usuário válido
- curl -X (método que quero chamar) (url do endpoint)
- curl -X GET http://site.com/api/v1/viagem  
Para adicionar o token com a autorização:
- curl -X [metodo] [url] -H 'Autorization: [token]'

  
Resposta JSON: data = lista de objetos (entre chaves{})

Posso validar inúmeros fatores na resposta (desde códigos de status, a valores dos parâmetros de objetos, existência de objetos, autorizações para diferentes tokens).
