# Courses

## Course **Agile Testing**

Validating and verifying each step in developing  
Interactive, self-organizing process  
  
|-- Initiation --|-- Planning --|-- Implementation --|-- Closing  
  
Include quality checks in each stage where decisions are being made  
  
Conceptualize the product and talk about it's antecipated use, a measure is created.  
Product Complete: tester knows what is expected of the software  
  
- Give vividdescriptions to the team, through feedback  
- Tell them how they are and are not aligned with the producit vision  
  
Create documented stories created by interacting and testing the product  
Beggining of a project:

- Tester reviews product requirements;
- Asks clarifying questions;
- Extract information to set a quality standart;
- Create a plan, outlining the product testability;
- Implement a structure to realize quality;

Skills: comunication, curiosity (desire to explore), attentiveness, active discovery, problem solving, mitigation, creativity and risk assessment.

**Shift Testing Left - do it earlier**

### Backlog Grooming

Meeting held to discuss user stories (or tickets)  
Meeting often includes POs and stakeholders, it should include QAs  
*Any place a decision is being made about the way the product is being build is great for a tester*

- Wheter USs are valid or need updates
- Is the use case relevante
- What is the impact
- How long it takes to construct  
  Testers can:
  - Outline dependencies
  - Determine testing timeline
  - Accurately determine testability
  - Escope shortcomings

Tester can create a loose test plan;  
Ask questions about client, plataform, devices, etc;  
Tester = Forager

### Sprint Planing

The team evaluate what lays arread. Assess backlog and define priorities
- Outline details
- Calculate measurements
- Agree on acceptance criteria (definition of done)

Tester get completed acceptance criteria matched with the test plans (including testing methods);  
Ask questions about the developer approach (antecipated execution);  
Helps id tools, plugins or data needed for testing;  
Gets acceptance criteria from stakeholder;  
Tester = Investigator

**The Three Amigos**  
Stakeholder + Developer + Tester  
Each has different perspectives so each ask different questions  

*Story Kickoff*  
Changes since planning are considered  
Tester designate an execution matrix, with final checks on each ticket detail  
Coverage approach, quality execution and automation  
Tester = Flagman

*Retrospectve*  
Feedback from the team to understand where they go.  
Analysis in what happened on the sprint  
- What the team is doing well
- What failed
- What they can improve

### Bug Tracking
- what is a name convention
- what is the priority (costly, loss)
- what is the matter (screenshot, desciptions)
- how did you find the bug
- how to reproduce the error
- where was the bug found

<br>

**Workflow**: Epics > Stories > Tasks

**Bug Advocacy:** Important to know the impact of the bug, if it will cause big issues

**Test Matrices:**  
Determine how a user is using the product;  
Tools: Google Analytics, Looker, Fabric - percentage of use in brownsers;  
- A tester can determine the most important browsers to test / the most used plataforms (devices/operational system)

### Manual Testing

Includes automated process that needs to be executed/stewarded by a person;

- Positive Testing: Whats supposed to be present
- Negative Testing: Any misinformation or incorrect entry is calculated appropriately
- Exploratory Testing: cognitive approach to address software
  - Stretching, moving, trying and shrinking aspects of the application (reveal strenths and weakness of the system)

### Test Automation

Series of tests that need to be run in succession at rapid speed, or are redundant / excessive / extreme;  
Not necessarily tests, but checks! **Ensure all key factors af the app are working**;  
Loading Testing: understand conditions of software under extreme exposure or visitation

### Continuous Integration

The practice of regularly pushing code to a shared repository, and runing quality checks on smaller batches of code.  
Smaller iterations can lead to earlier status updates
- Continuous Integration Schedule: fully automated regression suite to identify if new code has caused specific issues

<br>

## Course **Behavior Driven Development (BDD)**

Agile is an approach that highlights BDD  
Using Cucumber (navegating comand lines) and Ruby  
  
BDD emphasizes the client's perspective  
Define acceptance criterya for user stories  
User Story: functional incremetswritten by stakeholders (each contributes to the value of the product and help defines system purpose)  

US: As **who/why/where** I want somethins **why**  
Helps dev understand the goal of a feature, and are primary drivers in determing user needs.  

Acceptance criteria: helps prevent miscomunication between dev team and clients.  
Set of statements with well stablished pass/fail results for functional and non functional requirements (basis for testing systems)

Types of Acceptance Criteria:
- List-drive / Rule-oriented  
  Usefull for creating backlog
- Scenario-oriented / Illustrated  
  Helpful for translating tests into a format to drive the behavior development driven process

TDD: Test Driven Development  
Developers create their own unit tests  
First Write a test, then implement the code until the test pass.  
Hard to define what to test and how much.  
BDD helps focusing on what matters in TDD  
  
BDD = Agile + TDD  
Stop using the word Test, and start understanding the behavior of the app  
Write tests with expressive names, usually in the form of a sentence (make clear what the app is supposed to do)

**Vanguard Group case study**

Build the Right Thing - main goal for BDD  
Clear understanding on what the client will want  
BDD is for correctly building!

- PO and stakeholders must have clear understanding on the desire for the product
- Most (all) acceptance criteria have been defined
- User stories are already written

*Example Mapping:*  
Before starting a US, must clarify and confirm acceptance criteria  
EM helps create a visual representation of a US to guide and document the discussion  
For color pack of index cards;  
Each color is a specific piece of information  
Blue cards = rules (acceptance criteria)  
Green cards = examples of the US on each rule  
Red card = questions that cannot be immediatly answered  
Obs: if it is done to early the details are easily forgotten

BDD = Makes everyone understand and define acceptance criteria;  
US: Detailed and full context;  
Allow robust and focus tests;

**US: As a barista, I want to place an order for more coffee from a local distributor with an inventory system**  

"Can you give me a concrete example?"  
As a barista, when I came in to work early Monday morning to run through our inventory checklist I saw that we were running low on Colombian Dark Roast coffee.  
I logged into our inventory managment system and ordered two large bags of Colombian Dark RoastThe next monday the bags were delivered by our local distributor.  

Concrete example has: names, context and situational awareness.  

Acceptance Criteria (AC): defines a working system; written as pass or fail  

> **Given** *set of initial conditions* **when** *an event occurs* **then** *outcome expected*

Scenario: defines initial conditions for AC; states the trigger for expected outcome

Regular meetings between envolved parts
- share understanding of work increments
- Identify issues early
- Define clear acceptance criteria for when an increment is completed
- Allow each perspective to have buy-in (explains what need to be achieved by each person)

**Three Amigos**  
*PO, Developer and Tester (QA)*  
*PO* will tell a story envolving sales associates processing transactions  
Story:  
*"When processing transactions for coffee we want to allow customers to pay with cash or credit card. Either way, the amount charged should be the same"*  
Specific example:  
- "Maria wants buy a cup of coffe, realizes she forgot the money home, but has a credit card. So she asks a sales associate if he accept a card"  
- *QA* asks "Should we test that both forms of payment are accepted? What is the outcome we should test?"  
- *PO* - "Regardless the payment, they should be charged the same amount. Also, multiple types of credit cards should be accepted (mastercard, visa)"  
- *QA* reply "We have a minimum of 2 dollars for credit card purchase, because of fees in transactions."  
- So *PO* says "We should imbed a notification in the point of sale system so that cashiers can't accept a card bellow the 2 dollar limit. So we dont lose money on those transactions  
- *QA* brings the acceptance criteria "If the customer doesnt purchase at least 2$ credit card wont be accepted"  
- *Dev* adds "Usually a client gives a tip with the payment. What if the tip is added to the total and it becomes more than 2$? Also if they wanna tip with cash and pay with card?"  
- *PO* didnt think about that, "That is an edge case" but they will address that scenario later on, since for now, it runs out of the scope.  

The purpose of the meeting is NOT for PO to tell the others what to do, is so all perspectives come to a mutual understanding of the features.  
Ask questions, discuss concrete examples, propose solutions.

Dev team wants to know when the application is functioning.  
Translate the acceptance criteria into tests.  
Gherkin: language that describes the software behavior, but not how the behavior is implemented (for cucumber testing)  
https://cucumber.io/docs/gherkin/  
Language also great for documentarion
- Feature: name and bief description of the feature being tested
- Scenario: single concrete example to test. Each scenario has a way for how a feature should behave in any situation. Written as pass/fail examples

Each Feature has from 5 to 20 Scenarios  
**Given**: context for scenario  
**When**: action being taken by the system  
**Then**: expected behavior in this example, in this context.  

**Story: Customer pays with a credit card**  
*Scenario 1: Total charge is over the $2 credit card minimum*  
Given cliet orders $3 of coffe from cashier  
When client pays with a credit card  
Then cashier should process the payment  

*Scenario 2: Total charge is under the $2 credit card minimum*  
Given cliet orders $1 of coffe from cashier  
When client pays with a credit card  
Then cashier should NOT process the payment  

> BDD is a collection of process and techniques (not a tool)  
Maximize comunication between stakeholders, developers and testers.  
Some tools: Serenity - http://thucydides.info/#/  
SpecFlow - https://specflow.org/  
Jasmine - https://jasmine.github.io/  
minitest - http://docs.seattlerb.org/minitest/  
JGiven - https://jgiven.org/  
Cucumber - https://cucumber.io/  

Proactive and predicting QA paradigm
- Executable Specifications: used to define the behavior of an app in bussiness language.  
Are executable because they link to tests that apply the software.
- Test Automation: execute tests that compare the expectations for the software with actual outcomes.
- Living Documentation: system for dynamically generating docs with information up to date and accurate (the tests themselfs)  
Cucumber provides Gherkin language, and all the those above.

***Practical notes***  
Gemfile: Describes the Ruby libraries will need (add source, gem and version of the gem)  
Run: bundle install  
Then you sould be able to run "cucumber --init"  
Create feature file as .feature  
After, can run "cucumber"  
Needs to add steps definitions  
Create steps.rb file, inside step_definitions directory  

- Focus on the behavior of the application
- Focus on user stories from major perspective
- Define clear acceptance criteria, for all envolved

<br>

## Course **Insights on Software Quality Engineering**

### QA
Be able to break down a problem, and think about the most efficient ways to come to a solution  
Be able to think about the user, from the moment they start using the product, untill they stop  

It helps QA people to understand the thought process when the product is still being developed.  
Being a part of the process from the begining.  

### QA + Agile Dev
Greater focus on automation, because the main goal there is feaure development  
Make sure your core product still works  
Incorporate QA in the process  
Strategies to make sure everything has been developed, tested and bug fixed  

### QA for different types of applications

Mobile apps need to be submited and takes time;  
Make sure the app is not submitted full of bugs!  
Must test early and often;  
Desktop nowadays are able to offer updates as a way of fixing any critical bugs;  
Sowftware web its a lot of parts being developed in paralel but you gotta make sure its connected and working properly;  
Its easier to send a hot fix, and address the problem;

<br>

## Course **Introdução ao Teste de Software**

//TODO Couse in progress