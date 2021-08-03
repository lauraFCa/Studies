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

### Tools with WebDriver

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
Then you can switch to the alert, and accept() the alert.
  
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

<<<<<<< HEAD
Som common components: **Radio buttons**, **Checkboxes**, **Date pickers**, **Dropdoen menus** and **File uploads**  

**Radio Buttons** and/or **Checkboxes**: different strategies to automate:

- Based on ID
- Based on value - By.cssSelector(" *input[value='valor']* ")
- Using XPath - right click on element > copy > copy XPath  
  By.xPath("copied xpath")

**Datepicker**: clicking on the field, a datepicker (calendar) opens, with today's date highlighted.  
When I hover the mouse on other dates they're also highlighted.  
Once I select a date the datepicker (calendar) closes, and the field is populated with the clicked date.  
Automation options: 

- Open the datepicker and select the date
- Populate the field (input) manually  
  element.*sendKeys("a data no formato correto")*  
  Must close the dateFiled = press enter  
    - sendKeys(Keys.RETURN)

**Dropdown**: Click the dropdown, click on a component from the dropdown  
Find the dropdown and click on it - element.click()  
Define the desired dropped down item, and clikck on it

**File upload**: To chose a file, with an input I can send the file name fully to the field (find the input and send keys).

**Synchronization Issues** (test *speed*)

- Page to load
- Action to finish
- Components to appear

1. Brownsers work on different speeds  
Chromedriver and geckdriver are fster
2. The more tests are executed there's a discrepancy between runnig:
    - Locally
    - Remotally
3. Network speed

**Implicit Wait**: waits an amount of time untill throwing a "no such element" exception (default time is zero)

- *PROS:*  
  Easy to implement  
  Non-intrusive  
  Can be apllied to all elements in a script (not just one)
- *CONS:*  
  Coud take unnecessary time (wait when don't need)

> Doesn't depend on elements, just time  
> **Can take the *InterruptedException* out**

driver.manage().timeouts().*implicityWait(TimeOut, TimeUnit.SECONDS)*

**Explicit Wait**: waits an amount of time untill a condition is met  
If is not met, throws an exception

- *PROS:*  
  Is intelligent  
  Better options than implicit (more flexibility)  
  Waits for dinamically located elements
- *CONS:*  
  Coud take unnecessary time (wait when don't need)

> Doesn't

WebDriverWait wait = new WebDriverWait(driver, 10); //seconds
WebElement element = wait.until( ExpectedConditions.visibilityOfElementLocated(By.id("idElemento)) );

### Automating a Webpage

Filling a form with: inputs, radio buttons, check boxes, dropdowns and date pickers, with a submit button.  

#### **General code**

System.setProperty("webdriver.chrome.driver", "/Users/meaghanlewis/Downloads/chromedriver");

> WebDriver driver = new ChromeDriver();  
driver.get("https://formy-project.herokuapp.com/form");  

>//field First Name  
driver.findElement(By.id("first-name")).sendKeys("John");  
//field Last Name  
driver.findElement(By.id("last-name")).sendKeys("Doe");  
//field Job title  
driver.findElement(By.id("job-title")).sendKeys("QA Engineer");  
//field Education level  
driver.findElement(By.id("radio-button-2")).click();  
//field Sex  
driver.findElement(By.id("checkbox-2")).click();  
//field Years of experience  
driver.findElement(By.cssSelector("option[value='1']")).click();  
//field Date 
driver.findElement(By.id("datepicker")).sendKeys("05/28/2019");  
driver.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);  
//button Submit  
driver.findElement(By.cssSelector(".btn.btn-lg.btn-primary")).click();  

>//Assertion of the success  
//Wait for the new page to appear
WebDriverWait wait = new WebDriverWait(driver, 10);  
WebElement alert = wait.until((ExpectedConditions.visibilityOfElementLocated(By.className("alert"))));  
//Create assertion  
//Text displayed is equal to text expected  
String alertText = alert.getText();  
assertEquals("The form was successfully submitted!");

>driver.quit();

<br>

#### **Cleaned up code**

Using **Page Objects** to separate functionalities into different classes.  
Organize test code and keep it clean.

      public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "/Users/meaghanlewis/Downloads/chromedriver");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/form");

        submitForm(driver);

        waitForAlertBanner(driver);

        assertEquals("The form was successfully submitted!", getAlertBannerText(driver));

        driver.quit();
    }

    public static void submitForm(WebDriver driver)
    {
        driver.findElement(By.id("first-name")).sendKeys("John");

        driver.findElement(By.id("last-name")).sendKeys("Doe");

        driver.findElement(By.id("job-title")).sendKeys("QA Engineer");

        driver.findElement(By.id("radio-button-2")).click();

        driver.findElement(By.id("checkbox-2")).click();

        driver.findElement(By.cssSelector("option[value='1']")).click();

        driver.findElement(By.id("datepicker")).sendKeys("05/28/2019");
        driver.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);

        driver.findElement(By.cssSelector(".btn.btn-lg.btn-primary")).click();
    }

    public static void waitForAlertBanner(WebDriver driver)
    {
        WebDriverWait wait = new WebDriverWait(driver, 10);
        wait.until((ExpectedConditions.visibilityOfElementLocated(By.className("alert"))));
    }

    public static String getAlertBannerText(WebDriver driver)
    {
        return driver.findElement(By.className("alert")).getText();
    }

Note: WebElements DO NOT need to be explicitly defined before using them in tests.

<br>

### Project Integration

Connect it to *GitHub*, or any other source control repository.  

- Keeps project on web, not depending on one machine
- Allows for collaboratory work
- Helps to allow further integrations with the WebDriver project

Setup a ***Continuous Integration*** server, to run tests everytime the code changes.
**Selenium Grid** is a server that routes commands to remote browsers.  

- It spreads the load of tests across several machines, and they run in different brownsers, versions and plataforms.
- **Hub** is where tests are executed. It accesses **nodes**.  
- **Nodes** are where the tests are *run*, being individual Selenium instances.

> To use Selenium Grid is required Selenium Standalone Server  
Download: _selenium-server-standalone-3.141.59.jar_  
Run: _java -jar selenium-server-standalone-3.141.59.jar -role hub_  
Go to: [address]/grid/console

> Configure the Node: java -jar selenium-server-standalone-3.141.59.jar -role node -hub [address]  
Register a new server: [address]/grid/register  
OBS: I can customize the Node on the "Customize" tab  
The port will change for each node running

- Must maintain the grid infraestructure
- Choose physical or virtual machines

Continuous integration provides constant feedback about the tests and application funcionality.  
Some continuous integration servers (that work with Selenium)

- Circle CI: up to 16 parallel builds
- Jenkins: open source, but require some expertise to set up
- TeamCity: from JetBrain, great for enterprises
- Travis CI: one of the oldest, free for open-source projects (hosted on github) and for the first 100 builds.

To choose a CI Server you should look into:

- Infraestructure cost
- Ease of Setup
- Mainteinance needs
- Flexibility to run tests

**Cloud-based test tools**:

- Allow for hundreds of thousands of combinations of cross-browser, cross-device, and cross-platform testing
- Alternative to using your own Selenium Grid, so you don't have to maintain it yourself
- Virtual machines can be turned on demand with all specifications, run test, and then shut down.

Suggestion: Sauce Labs, easy to set up with great support.  
Supports all major programming languages. Allows for real device testing in addition to using emulators.  
It is also a great option to run Selenium test and integrates well with major CI servers.
=======
<br>

**Advaced Locators**  
ClassName, CSS Selector, Name, Tag name, ID, Link text, XPath  
Best locators: **Unique, Descriptive, Static** (unlikely to change)  
Usually avoided:

- Link text: wirk as longs as links are unique on a page
- Tag name: usually not unique and not descriptive
- XPath: definetly not descriptive

Prefer using:

- ID (#id)
- Class (.class)
- Name ( By.cssSelector("input[name='nome']") )
- **CSS Selector**  
    Can be used with all the olher locators  
    Most powerfull choice for automation  
    Great for "hard to find" elements

CSS Selector is also great for:

- Find based on substring or string
- Using wildcards
- Child and sibiling nodes

Combinations of CSS Selector: (when a page has more elements)

- Tag and Class  
  By.cssSelector("input.classe"])
- Tag and ID  
  By.cssSelector("input#id"])
- Tag and Attribute  
  By.cssSelector("input[type='radio']")  
  By.cssSelector("input[value='radio button']")
- Class and Class  
  By.cssSelector(".btn.btn-lg.btn-success")  
  (pilha de classes)

Using Text Matching: best way is to use **Value** (exact value of selector)  
Wildcard matches text based on a selector or *part of a selector*.  

By Value: *BycssSelector( "<tagname>[type='<value>']" )*
By Wildcard: Matching by String or Substring

- **Prefix:** *BycssSelector( "a[id^='id_prefix_']" )*  
  By.cssSelector( "div[id^='textFieldID']" )
- **Suffix:** *BycssSelector( "a[id$='textFieldID']" )*  
  By.cssSelector( "div[id$='id_sufix_']" )
- **Substring:** *BycssSelector( "a[id*='id_pattern']" )*  
  By.cssSelector( "div[id*='textFieldID']" )
- **Exact match:** *BycssSelector( "a[id='id']" )*  
  By.cssSelector( "div[id='textFieldID']" )

Finding Child Nodes:  
" div#parent a "  
Finding Nth-Child:  
" #list li:nth-child(n) "  

