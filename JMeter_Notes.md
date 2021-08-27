# Courses

## Course **JMeter - Step by Step for Beginners**

[Udemy Course](https://www.udemy.com/course/jmeter-step-by-step-for-beginners/)

Thread Group: users used to create/run the test  
First test thread: protocol = https

Thread Properties:  
Number of thread (users): number of users accessing the page (not simultaneously)

Ramp-up period: Every x seconds 1 user will be headed (x = number of threads / ramp-up) - In x seconds the number of users will hit the application

Assertion: request response  
Size assertion = bytes  
HTML assertion = check format of the response (check if it's HTML)
> Erros threshold: limit number of erros (after that, it'll call error)  
> Warning threshold: more than that will make it as warning (else, it's not called)

Listener: get information about the application response

Thread Group 1-5 = (first iteration of user 5)

Latency: when we start getting the response

OBS: View result in tree takes up a lot of memory

Graph results: Because of cache, the average will get higher and the throughput will get smaller  
(Not recommended for heavly loaded performance test - high memory consuming)

### Lesson 01

**Step 1 :** Check java is installed on your system  
>java -version  
[How to install java on windows](https://youtu.be/FqpmH8MVO6A?list=PLhW3qG5bs-L_qj1L5hnHvJYeFpQ_g4UuU)  
[How to install java on mac](https://youtu.be/NSvtis2fGlA?list=PLhW3qG5bs-L_qj1L5hnHvJYeFpQ_g4UuU)

**Step 2 :** [Download Jmeter from internet](http://jmeter.apache.org/download_jmeter.cgi)

**Step 3 :** Unzip and keep Jmeter folder at any location  
**Step 4 :** Start Jmeter  
> Windows - jmeter/bin - jmeter.bat

### Lesson 02

Step 1 - Start Jmeter  
Step 2 - Create a TestPlan  
Step 3 - Create a Thread Group (Users) Step 4 - Add a Sampler (Http)  
Step 5 - Add Listeners  
Step 6 - To Run the Test

### Lesson 03

Assertions = checks on the Response

1. Response Assertion
2. Duration Assertion
3. Size Assertion
4. HTML Assertion
5. XML Assertion
6. XPATH Assertion

### Lesson 04

Listener = elements that gather information about the performance test  
Used to view results / metrics of the test  
Latency = time to first byte  

1. View Results in Table
2. View Results Tree
3. Aggregate Report
4. Graph Results
5. Summary Report
6. Simple Data Writer


## Course **JMeter: Performance and Load Testing**

[Linkedin Learning Course](https://www.linkedin.com/learning/jmeter-performance-and-load-testing/)

Test Anatomy

- Test Plan
    - Thread Group
    - Sampler
    - Listener

HTTP Infos:

1. Cache Manager  
Manipulate cache sent with requests  
Preserve or delete cache during a test
2. Cookie Manager  
Manage cookies within the request  
Authentication
3. Header Manager  
Manages headers of the request  
Can store for later use

Testing in landonhotel.com
