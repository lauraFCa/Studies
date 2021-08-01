# Courses

## Course **Learning Selenium**

Linkedin Learning Course: [Learning Selenium](https://linkedin.com/learning/learning-selenium/)  
**Selenium WebDriver 3.0**

- Support WebAPIs
- Browser vendors manage their own driver
- W3C Specification: standarts and guidelines
- Open Source
- Uses client server communication

### WebDriver

- WebDriver: Quickly and easily write automated tests;
- Emulate actions of users (clicking, typing);
- Test application across multiple browsers and plataforms;
- Selenium WebDriver works with client-server communication;
- For each command on a test, a request is sent to the WebDriver API, it interprets the request and the step is executed on the browser (act as the server);

**Supported Languages:** C, Java, Ruby, Python, JavaScript  
**Supported Plataforms:** macOS, Windows, Linux  
**Supported Browsers:** Chrome, Firefox, Explorer, Safari

geckodriver: browser driver

### Notes on Gems in Ruby

- Gems are independent software packages (like libraries or plugins)
- RubiGems is the package management framework
- _gem install_ is included in Ruby by default
- _bundle install_ need a gemfile (to define the gems, and required versions), but allows any - individual system that builds and runs the application can install all the same versions of the gem easily

1. Create a Gemfile with the source and version of the gems
2. Use Bundle to install -> gem install bundler (on the same directory as the Gemfile)
3. Download _geckodriver_ from Mozilla github releases page.

**Steps on test:**

1. Set up new instance of the Firefox driver (mandatory to specify the name, can also specify version, screen size or plataform)
2. Tell the driver what to do (navigate to a page, find an element, do an action)  
   [Selenium classes command lists](https://www.selenium.dev/selenium/docs/api/rb/Selenium/WebDriver/Driver.html)
3. Close the driver session (quit)

### Know what to automate

- Knowledge of the and functionalities
- Outline test scenarios (steps to automate)
  - Think of Inputs and Outputs
  - Define the value each scenario will provide
- Find the web elements needed for testing (locate)

### Assertions

Are not native, so a library (gem) is needed.

- RSpec: library for assertions
- RSpec-core: behavior driven development format for test classes **and** provides nicely formatted output.
  - Add a describe block on the test

\*\*Put geckodriver on the enviromment variables.

### WebDrivers

- ChromeDriver
  - By Google; Webdriver wire protocol for Chromium (android and desktop)
- Geckodriver
  - By Mozilla; Written in Rust; Default for Firefox since Selenium 3.0 (best in Firefox 55+)
- EdgeDriver
  - By Microsoft; Written in C#, best in Windows 10
- SafariDriver
  - By Apple; Build with WebKit

When decidign wich to use, refer to usage data on the app - to define the most commonly used browsers.

### Selenium Grid

- Proxy server that runs tests against remote browser instances;
- Distributes tests across several servers;
- Test in different browsers, plataforms and devices at the same time;

**Central Points to the Grid:**

- Hub  
  Central cerver where test are executed;  
  One hib in a grid instance;
- Node
  Registered to a hub; Where tests are run; Any plataform;  
  **Many Nodes registered to one Hub in a grid instance;**

1. Test is executed on the Grid;
2. Hub searches the node with the necessary configuration;
3. Hub sends the test to that Node;  
    If multiple nodes have the configuration, the first found is used!
   **Great to run lots of tests at once**

To use Selenium Grid is required Selenium Standalone Server  
Download: _selenium-server-standalone-3.141.59.jar_  
Run: _java -jar selenium-server-standalone-3.141.59.jar -role hub_  
Go to: [address]/grid/console

Configure the Node: java -jar selenium-server-standalone-3.141.59.jar -role node -hub [address]  
Register a new server: [address]/grid/register  
OBS: I can customize the Node on the "Customize" tab  
 The port will change for each node running

Using a generic Firefox driver: driver = Selenium::WebDriver.for :firefox
Using a remote driver: driver = Selenium::WebDriver.for :remote, desired_capabilities: :firefox
Create an instance of the remote webdriver, indicating tests will be run remotely
Desired capabilities: browser name, version, plataform, etc.

The hub received a request (when test executed), and forwarded the request to the remote Firefox instance.  
The node translate the test script using JSON wire protocol, and rund it remotly.

- When using the grid its either hosted on physical or virtual hosts.
- Physical server should be hosted for testing only

#### PROS

- Scale: runs many tests on parallel
- Central way to manage multiple envirements (can run in diferent systems, browsers, etc)
- Smart: quickly and easily find nodes, and run tests on the approprieted nodes

#### CONS

- Maintenance is required to keep it running
  - Help with maintenance: enable warnings and logs (easy debug), create scripts for common behaviors (start and stop hubs)
- Performance might start to degrade over time: some nodes may start running extremely slow, there might be still browser windows (not shut down properly)
  - Help with it: explicitly kill browsers after tests, periodically restart grid nodes, restart the server after runs.

### Clean Test Code

- Readable tests  
- Minimize lines os codes  (not repeat steps over and over)  
- Repetitive lines can be extracted into **reusable variables and methods**
  - extract strings into variables  
  - Some actions are repeated, such as finding an element -> send key to the element (break into actions and methods)  

### Page Object Pattern

Set classes for each page in the application to model behavior.  
Each page has test *Selectors* and test *Methods*.  
In the test a new page object is created and then call that class's methods directly.  
**Goals**: Separate *test* and *code* and makes the test more mainteinable! (things are updated at one place only)  
Ex: "Signup Page" and "User Page": each has its own class.

### Test Organization

It's important to be able to know:

- Where the test live  
- What they cover  
- How to run them  

***Some tips:***

- Each Test Class focus on one area of the application (one scope/focus)  
- Group tests into sub-suits by feature  
- Document tests with a readme (explain structure and how to run them)  

### Test Pyramid

Structure tests, different levels of testing and guide coverage.

- **Unit:** Bottom of the pyramid - Fastest, test a single function and should always be the most numbered (have as many unit tests as possible).  
- **Integration:** (Service level test) - How many servers work together. Are a bit slower.  
- **UI:** At the top, test end to end workflows but are the slowest (run through browser) - least amount.

[Selenium Oficial](https://www.selenium.dev/)  
[Selenium Wiki](https://github.com/SeleniumHQ/selenium/wiki)

<br>

## Course **Selenium Essential Training**

Linkedin Learning Course: [Selenium Essential Training](https://www.linkedin.com/learning/selenium-essential-training/)

**Selenium Grid:** central hub that allows multiple tests to run concurrently  
**Selenium IDE:** Plugin to record each interaction of an application as test steps. Test code was able to be generated quickly and easy.
  Good for those who want to get familiar with element locators and creating test scripts.
  
Selenium Webdriver uses *Client x Server* communication.  
For each command in the script, a request is sent to the WebDriver API (REST base service), that interprets the request and the steps are executed in the browser.

### Driver Browsers

#### ChromeDriver

- Maintained by Google  
- Implements WebDriver wire protocol for Chromium
- Available on Chrome (Android and Desktop)

#### Geckodriver

- WebDriver maintained by Mozilla
- BWritten in Rust
- Default for Firefox

#### EdgeDriver

- Owned by Microsoft
- Written in C#
- Support is best in Windows 10
- It's traditionally slower than others

#### SafariDriver

- Maintained by Apple
- SafariDriver is included by default (no need for aditional configurations) - Set Sarafi appart from others
- Built with WebKit
  
Finding an element on the page:  

- By.ClassName
- By.CssSelector
- By. Id
- By. Name
- By.Xpath

#### Tools with WebDriver

Use **autocomplete**, with Google Places API.

1. Identify the autocomplete webelement
2. Fill the autocomplete item field (including number, street, city and state)
3. Put a sleep statment (so that the dropdown can load)
4. Click on the result

To **move to an element** you need to import the *Actions* class.  
With actions you can move to the element ( *actions.moveToElement( driver.findElement(By.id("name)) )* )
This will scroll the page to the field previously defined.
  
**Switch Windows**  
driver.switchTo()

- .window("windowName");
- .frame("frameName");
- .alert();

To switch windows I declare a handle for the orinal one, and then create a for loop to create handlers for all the new windows.  
After the for loop we go back to the original handle (first window).

**Alerts** can be used by imorting the *Alert* class.  
Then you can switch to the alert, and accept the alert.
  
**JavaScript** commands may be needed in tests.

1. *executeAsyncScript*  
  Execute asyncronous script and signal they're finished by invoking the callback
2. *executeScript*  
  Executes the script as an anonymous function

When to use this JavaScriptExecutor:

- WebDriver fails to click
- Trigger actions
- Perform movement on a page (scrolling and zooming)

Using "Drag and Drop"

- For manipulating images
- Arranging components on the screen

> Actions actions = new Action(driver)  
actions.dragAndDrop(elementoPraArrastar, caixaRecebeElemento).build().perform()  
