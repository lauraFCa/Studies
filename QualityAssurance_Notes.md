# Course **Agile Testing**

[Linkedin Learning Course](https://www.linkedin.com/learning/agile-testing-2)

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

## Backlog Grooming

Meeting held to discuss user stories (or tickets)  
Meeting often includes POs and stakeholders, it should include QAs  
_Any place a decision is being made about the way the product is being build is great for a tester_

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

## Sprint Planing

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

_Story Kickoff_  
Changes since planning are considered  
Tester designate an execution matrix, with final checks on each ticket detail  
Coverage approach, quality execution and automation  
Tester = Flagman

_Retrospectve_  
Feedback from the team to understand where they go.  
Analysis in what happened on the sprint

- What the team is doing well
- What failed
- What they can improve

## Bug Tracking

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

## Manual Testing

Includes automated process that needs to be executed/stewarded by a person;

- Positive Testing: Whats supposed to be present
- Negative Testing: Any misinformation or incorrect entry is calculated appropriately
- Exploratory Testing: cognitive approach to address software
  - Stretching, moving, trying and shrinking aspects of the application (reveal strenths and weakness of the system)

## Test Automation

Series of tests that need to be run in succession at rapid speed, or are redundant / excessive / extreme;  
Not necessarily tests, but checks! **Ensure all key factors af the app are working**;  
Loading Testing: understand conditions of software under extreme exposure or visitation

## Continuous Integration

The practice of regularly pushing code to a shared repository, and runing quality checks on smaller batches of code.  
Smaller iterations can lead to earlier status updates

- Continuous Integration Schedule: fully automated regression suite to identify if new code has caused specific issues

<br>

# Course **Behavior Driven Development (BDD)**

[Linkedin Learning Course](https://www.linkedin.com/learning/behavior-driven-development)

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

_Example Mapping:_  
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

> **Given** _set of initial conditions_ **when** _an event occurs_ **then** _outcome expected_

Scenario: defines initial conditions for AC; states the trigger for expected outcome

Regular meetings between envolved parts

- share understanding of work increments
- Identify issues early
- Define clear acceptance criteria for when an increment is completed
- Allow each perspective to have buy-in (explains what need to be achieved by each person)

**Three Amigos**  
_PO, Developer and Tester (QA)_  
_PO_ will tell a story envolving sales associates processing transactions  
Story:  
_"When processing transactions for coffee we want to allow customers to pay with cash or credit card. Either way, the amount charged should be the same"_  
Specific example:

- "Maria wants buy a cup of coffe, realizes she forgot the money home, but has a credit card. So she asks a sales associate if he accept a card"
- _QA_ asks "Should we test that both forms of payment are accepted? What is the outcome we should test?"
- _PO_ - "Regardless the payment, they should be charged the same amount. Also, multiple types of credit cards should be accepted (mastercard, visa)"
- _QA_ reply "We have a minimum of 2 dollars for credit card purchase, because of fees in transactions."
- So _PO_ says "We should imbed a notification in the point of sale system so that cashiers can't accept a card bellow the 2 dollar limit. So we dont lose money on those transactions
- _QA_ brings the acceptance criteria "If the customer doesnt purchase at least 2$ credit card wont be accepted"
- _Dev_ adds "Usually a client gives a tip with the payment. What if the tip is added to the total and it becomes more than 2$? Also if they wanna tip with cash and pay with card?"
- _PO_ didnt think about that, "That is an edge case" but they will address that scenario later on, since for now, it runs out of the scope.

The purpose of the meeting is NOT for PO to tell the others what to do, is so all perspectives come to a mutual understanding of the features.  
Ask questions, discuss concrete examples, propose solutions.

Dev team wants to know when the application is functioning.  
Translate the acceptance criteria into tests.  
Gherkin: language that describes the software behavior, but not how the behavior is implemented (for cucumber testing)  
[Cucumber Gherkin](https://cucumber.io/docs/gherkin/)  
Language also great for documentarion

- Feature: name and bief description of the feature being tested
- Scenario: single concrete example to test. Each scenario has a way for how a feature should behave in any situation. Written as pass/fail examples

Each Feature has from 5 to 20 Scenarios  
**Given**: context for scenario  
**When**: action being taken by the system  
**Then**: expected behavior in this example, in this context.

**Story: Customer pays with a credit card**  
_Scenario 1: Total charge is over the $2 credit card minimum_  
Given cliet orders $3 of coffe from cashier  
When client pays with a credit card  
Then cashier should process the payment

_Scenario 2: Total charge is under the $2 credit card minimum_  
Given cliet orders $1 of coffe from cashier  
When client pays with a credit card  
Then cashier should NOT process the payment

> BDD is a collection of process and techniques (not a tool)  
> Maximize comunication between stakeholders, developers and testers.  
> Some tools: [Serenity](http://thucydides.info/#/)  
> [SpecFlow](https://specflow.org/)  
> [Jasmine](https://jasmine.github.io/)  
> [minitest](http://docs.seattlerb.org/minitest/)  
> [JGiven](https://jgiven.org/)  
> [Cucumber](https://cucumber.io/)

Proactive and predicting QA paradigm

- Executable Specifications: used to define the behavior of an app in bussiness language.  
  Are executable because they link to tests that apply the software.
- Test Automation: execute tests that compare the expectations for the software with actual outcomes.
- Living Documentation: system for dynamically generating docs with information up to date and accurate (the tests themselfs)  
  Cucumber provides Gherkin language, and all the those above.

**_Practical notes_**  
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

# Course **Insights on Software Quality Engineering**

[Linkedin Learning Course](https://www.linkedin.com/learning/insights-on-software-quality-engineering)

## QA

Be able to break down a problem, and think about the most efficient ways to come to a solution  
Be able to think about the user, from the moment they start using the product, untill they stop

It helps QA people to understand the thought process when the product is still being developed.  
Being a part of the process from the begining.

## QA + Agile Dev

Greater focus on automation, because the main goal there is feaure development  
Make sure your core product still works  
Incorporate QA in the process  
Strategies to make sure everything has been developed, tested and bug fixed

## QA for different types of applications

Mobile apps need to be submited and takes time;  
Make sure the app is not submitted full of bugs!  
Must test early and often;  
Desktop nowadays are able to offer updates as a way of fixing any critical bugs;  
Sowftware web its a lot of parts being developed in paralel but you gotta make sure its connected and working properly;  
Its easier to send a hot fix, and address the problem;

<br>

# Notes **Automatiza????o de Testes**

[Os 15 Erros mais Comuns na Automatiza????o de Testes](https://www.youtube.com/watch?v=k4egg4trjgc&ab_channel=Pagar.meTalks)  

- Suportar testes (ao inv??s de replicar testes)  
N??o apenas copiar e modificar testes que j?? existem (repassando erros)
- Testabilidade (testes tamb??m s??o c??digos - precisam ser testados)
- Focar na experiencia do usu??rio (n??o a codifica????o)
- Problemas ao inv??s de ferramentas (definir o problema para depois ver se ?? necessaria/qual ferramenta)
- Foco no risco ao inv??s de cobertura (garantir que as partes mais criticas est??o cobertas)
- Observabilidade, facilitando rastreio de falhas de teste

Testes deven avisar impactos e altera????es de fluxo.

Armadilhas na automa????o de testes:
1. Testar tudo em apenas uma camada  

2. X

# Course **Introdu????o ao Teste de Software**

[Coursera Course](https://www.coursera.org/learn/intro-teste-de-software)

## Hist??ria do Teste de Software

Diferen??a entre _tirar defeitos_ e _testar software_

`"O teste mostra presen??a, n??o aus??ncia de erros"`

> 20/02 Dia Internacional do Teste de Software

A atividade de _testes_ ?? necess??ria porque humanos podem cometer erros.  
Esses erros podem ocorrerr devido a:

- complexidade do software desenvolvido,
- mudan??as necess??rias em software j?? existente e que pode levar a novas falhas,
- falta de uso de m??todos que apoiem a valida????o e verifica????o da qualidade do software,
- situa????es imprevis??veis,
- quest??es pessoais e do pr??prio ambiente de trabalho e que interferem no desempenho do testador

**O teste ?? requerido para revelar a presen??a de defeitos, aumentar a confian??a e satisfa????o do cliente com o software, e assegurar a qualidade do produto.**

?? essencial prever ou garantir que falhas n??o ocorram, ou que _pelo menos sejam minimizadas_ ou identificadas o quanto antes.

## TMMI (Test Maturity Model integration)

Guia e framework para apoiar a melhoria de processos de teste (criando n??veis).  
Estabelece requisitos necess??rios para que se tenha um processo de teste com qualidade.

> Assim como CMMI - Modelo de maturidade de software.

1. **N??vel 1**  
   N??vel ca??tico, todos os processos de teste est??o aqui, e n??o requer que qualquer coisa seja contemplada.
2. **N??vel 2**  
   Gerenciado, possui estrat??gia, planejamento, monitoramento, controle, projeto, execu????o e ambiente de teste.
3. **N??vel 3**  
   Definido, possui organiza????o, programa de treinamento, ciclo de vida e integra????o, teste n??o funcional e revis??o por partes.
4. **N??vel 4**  
   Gerenciamento quantitativo, medi????o de teste e avalia????o e revis??o avan??ada da qualidade do software.
5. **N??vel 5**  
   Em otimiza????o, o processo j?? tem muita qualidade e o objetivo ?? manter a qualidade e evluir constantemente.

Os requisitos para o processo de qualidade s??o chamados de **_??reas de processo_**.

Cada uma cont??m _objetivos espec??ficos_, _pr??ticas espec??ficas_, _subpr??ticas_, e _objetivos gen??ricos_ e _pr??ticas gen??ricas_.

Objetivos espec??ficos s??o requeridos de serem alcan??ados.  
Pr??ticas espec??ficas s??o coisas que s??o esperadas que se fa??a para que os objetivos sejam alcan??ados.  
Subpr??ticas s??o de car??ter mais informativo.

Objetivos gen??ricos e pr??ticas gen??ricas, s??o comuns a v??rias ??reas de processo.  
Descrevem caracter??sticas que podem ser utilizadas para institucionalizar o processo de teste dentro da organiza????o.

O TMMI possui 81 pr??ticas espec??ficas, ?? o modelo mais pesado em termos de requisitos para a qualidade.  
Um estudo feito concluiu que das 81 pr??ticas, 33 s??o realmente executadas e primordias.  

Refer??ncias:

- [Identifying a Subset of TMMi Practices to Establish a Streamlined Software Testing Process](https://ieeexplore.ieee.org/document/6800190)
- [Elabora????o de um processo de teste com base em um estudo de caso real](https://repositorio.ufscar.br/handle/ufscar/519)
- [Characterising the state of the practice in software testing through a TMMi-based process](https://jserd.springeropen.com/articles/10.1186/s40411-015-0019-9)

## Habilidades de um bom profissional de Atividades de Software  

Equipe com metodologia ??gil, SCRUM e KANBAN.  

- Gostar de programar (conhecimento de programa????o)  
  Para entender e saber utilizar e criar testes automatizados
- Mente criativa e curiosa (encontrar a fundo causa de problemas)
- Trabalho em equipe, com desenvolvedores, e todo o processo da empresa como um todo

- [15 Skills Every Software Tester Should be Mastered in](https://www.testing-whiz.com/blog/15-skills-every-software-tester-should-master-in-2017)
- [Formando Equipes Eficientes de Teste de Software](http://www.linhadecodigo.com.br/artigo/1419/formando-equipes-eficientes-de-teste-de-software.aspx#ixzz4tu5YXh7j)

Profissional de testes deve saber criar requisitos, casos de testes, encontrar problemas nos requisitos e testes. Deve tamb??m saber reportar as falhas encontradas.  
Al??m disso tamb??m deve saber priorizar casos de teste e bugs para que o software saia com o melhor resultado (manuten????o de risco).

- Impostante: conhecer tamb??m estrutura de redes (testes de performance)
- **Ferramenta: Sonar Cube**

> N??o existem produtos de qualidade, existem processos com qualidade!

<!-- ## Mapa Conceitual de Teste de Software

![Teste de Software](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/JQmZ_6SjEeesIgqlslw-IA_879eb74415eff3980e869ed729ac40b7_bf7591e0a4a211e78d872d02aebbf8f7.map.jpg?expiry=1627948800000&hmac=nBT_mnY823kgCpNc2NKq2M8EH8ghForqRNZpKW89Q9k) -->

## Terminologia da ??rea

**Engano**: A????o humana que produz resultado incorreto;  
**Defeito**: Passo incorreto na defini????o de dados (bug, erro, defeito);  
 Pode existir sem ser identificado (n??o se tornar?? um erro).  
**Erro**: Diferen??a entre a especifica????o e o que est?? ocorrendo, de fato;  
Se propagado para sa??da do software se torna *Falha*;  
**Falha**: Inabilidade do sistema de realizar a fun????o requerida;  
Erro que chegou a sa??da;  

![Terminologias](https://miro.medium.com/max/1400/0*-3jSXEvLyiHROefw)  

- Importante conhecer termos e jarg??es
- Engano x Defeito x Falhas x Eros
- Defini????es nem sempre s??o seguidas
- Existem padr??es internacionais que coletam e padronizeam a terminologia da ??rea

## Etapas do Teste

**1. Planejamento**: Plano de Teste

  - Funcionalidades a serem testadas
  - Riscos associados
  - Requisitos de ambiente  

**2. Projeto dos Casos de Teste**: Elaborados

  - Refinar planejamento
  - Especificar os casos de teste
  - Especifica????o do Procedimento de teste (passos para execu????o)
  - M??dulo testado, Descri????o, Roteiro, Resultado esperado, Resultado do desenvolvedor e Resultado do teste.

**3. Execu????o**: Casos de teste elaborados  

  - Di??rio de teste (detalhes cronol??gicos da execu????o)
  - Relat??rio de incidente - qualquer evento ocorrido que precisa ser analisado depois
    - Status, Respons??vel pela corre????o, Prioridade, Descri????o do erro, Data e nome de quem corrigiu
  - Relat??rio de encaminhamento de item (para desenvolvedores ou outros)

**4. An??lise**: Avalia????o do programa
  
  - Relat??rio de resumo de teste
    - Descri????o do teste, pessoas envolvidas, n??mero do teste (casos de uso criados antes, durante e depois, casos com erro, etc), Percentual de testes executados, com sucesso, com falhas e corrigidos.

**Importante:** Verificar documenta????o para cada etapa (por entidades internacionais)

## Fases da Atividade de Testes

Software confi??vel por??m inseguro - requisitos estavam errados.  
Existem tipos distintos de *engano* e n??veis diferentes de abstra????o.  
**Cada fase da atividade de teste tem um objetivo, e aborda diferentes tipos de erros e aspectos do software.**  

> 1. Teste de Unidade  
Erros simples de programa????o, pode ser feito pelo pr??prio dev
> 2. Teste de Integra????o  
Estrutura do software, encontra erros nas interfaces entre as unidades (feito ap??s testes das unidades)
> 3. Teste de Sistema  
Erros de em fun????es, desempenho, **fora da especifica????o**, ap??s o sistema ser finalizado
> 4. Teste de Regress??o  
Feito ap??s manuten????es, garantindo que modifica????es n??o interferem com o sistema previamente em funcionamento e testado.

*Independente da fase existem etapas para a execu????o da atividade de teste.*

## T??cnicas de Teste

Programa tem um dom??nio de entrada (todos os valores que podem ser usados para executar o programa).  
A partir do dom??nio seleciona um dado de teste e cria caso de teste a partir do dom??nimo.  
Verificar se para cada caso de teste a sa??da obtida ?? a esperada.

**Para dom??nios muito grandes posso definir subdominios e selecionar dados de teste que representem cada um deles.**

Regras ou T??cnicas s??o usadas para identificar quando dados de teste devem estar no mesmo sub-dom??nimo ou n??o.

## Teste Funcional

Parte da *especifica????o do software*.

- Particionamento em classes e equival??ncia
- An??lise do valor limite
- Combinatorial
- Grafo causa-efeito

Pode ser feito em todas as fases de teste (unidade, integra????o e sistema)

## Teste Estrutural

Parte do conhecimento da estrutura interna do programa (c??digo).  
Crit??rios baseados em:

- Complexidade (McCabe)
- Fluxo de controle (todos-n??s, todos-arcos, etc)
- Fluxo de dados (Rapps & Weyuker, Potenciais-usos)

Feito nas fases de teste de unidade e integra????o.

## Teste de Defeitos

Parte de defeitos t??picos, comumente vistos no sistema.  
Criar implementa????es alternativas para que o testador projete casos de teste que revelem os defeitos.

- Manuten????o
  - An??lise de mudan??as
  - Manuten????o de interface

Feito nas fases de teste de unidade e integra????o.

## Testes Funcionais

**Especifica????o dos requisitos do Software:**  
Utilizar o teste funcional para *projetar casos de teste*, *submeter casos no programa* e *verificar se a sa??da obtida* est?? de acordo com a sa??da que era esperada

- O usu??rio consegue fazer isso?
- Essa funcionalidade funciona?

Reflete a ??tica do usu??rio/stakehoder que ir?? utilizar o programa.

Podem ent??o ser reveladas inconformidades com os objetivos especificos:

- Fun????es incorretas ou ausentes
- Erros na interface
- Erros estrutura de dados
- Erros de acesso a softwares externos
- Inicializa????o e t??rmino do programa

N??o requer o c??digo fonte do sistema.  
Aplicada a todas as fases, pode ser executada manual ou automatizada.  

1. Identificar as fun????es que o sistema deve executar
2. Criar casos de teste para verificar funcionamento dessas fun????es
3. Executar casos de teste
4. Comparar resultados (obtidos e esperados)

Aplicar crit??rios para identificar os casos de teste de maior cobertura (melhores)

## **Particionamento em Classes de Equival??ncia**

Qualquer elemento em um sub-conjunto ir?? representar o conjunto todos, e ser?? usado para criar um caso de uso.  

1. Identificar classes de equival??ncia
    - Procurar termos como *intervalo*, *conjunto* ou palavras similares;  
    - Posso subdividir as classes (caso elementos similares sejam tratados de maneira diferente)
    - Verificar diretrizes pra dividir as classes
    - Definir classes v??lidas e inv??lidas

2. Gerar casos de teste para um elemento de cada classe
    - Definidos para classes v??lidas e inv??lidas

Exemplos:

Classe v??lida: Aquilo que o sistema espera

- N??meros *entre 20 e 30*
- Digitar apenas *1 n??mero*
- Valores espec??ficos em uma classe (ex: regras de imposto)

Classes inv??lidas: Fora do esperado pelo sistema

- N??meros *acima de 30* e *abaixo de 20*
- Digitar *mais de 1 n??mero* de *menos de 1 n??mero*
- Valores fora do esperado

Vari??veis analis??veis:

- Comprimento da entrada (de 2 a 6 caracteres)
- Caractere inicial (inicia com uma letra)
- Corpo da entrada (cont??m apenas letras ou d??gitos)

Crio casos de teste para cada vari??vel, e cada classe.

> Teste Funcional  
Aplica????es onde vari??veis de entrada s??o facilmente identificadas  
Reduz dom??nio de entrada  
Classes podem ser definidas a partir de diretrizes, considerando condi????es de entrada

## **An??lise do Valor Limite**

Comlementa o particionamento em classes de equival??ncia.  
Dados de teste s??o selecionados considerando os valores limitantes das classes (m??ximo e m??nimo).

Se a entrada exige intervalo de valores (10 a 20), s??o definidos dados nos limites e aqu??m a eles (9, 10, 20 e 21).  

Se a entrada exige tamanho de valores (1 a 100), s??o definidos dados de nenhum valor na entrada, os limites m??ximo e m??nimo e aqu??m (0, 1,100,101)  

Se a entrada exige for uma lista ordenada (10 a 20), s??o definidos dados nos limites (primeiro e ultimo valor da lista) e al??m (9, 10, 20 e 21).  

> Teste Funcional  
Funciona junto com as classes de equival??ncia  
Explora valores nos limites das classes (e valor unitario acima)  
Diretrizes levam a determina????o dos dados de teste

## **Automatiza????o de Testes Funcionais**

*JUnit:* Framework de teste de unidade para Java.

- Open Source
- Utiliza *Annotations para identificar m??todos de teste*  
Meta tags adicionadas ao c??digo:
    - @Test
    - @Before : dados necess??rios para execu????o do teste s??o carregados  
    (executa a cada caso de teste)
    - @After : fecha conex??o com banco de dados  
    (executa a cada caso de teste)
    - @BeforeClass : executado uma vez antes de todos os testes
    - @AfterClass : executado uma vez depois de todos os testes
    - @Ignore
- Fornece Assertions (avaliar valores esperados)
- Possibilita feedback imediato ao testador

Classes do JUnit: Assert, TestCase, TestResult, TestSuit.

> static private ByteArrayOutputStream baOut;  
static private PrintStream psOut;  
<br>
@BeforeClass  
public static void *beforeClassInit*() {  
baOut = new ByteArrayOutputStream();  
psOut = new PrintStream(baOut);  
System.setOut(psOut)  
}  
<br>
@AfterClass  
public static void *afterClassFinalize*() {  
  psOut.close();  
}  
<br>
@Before  
public static void *setUp*() {  
  baOut.reset();  
}  
<br>
@Test  
public void ***testeValido01***() {  
  ClasseMainDoProjeto.main(new String [] { "a1" });  
  String output = baOut.toString();  
  assertEquals("Valido", output)  
}
<br>
@Test  
public void ***testeInvalido01***() {  
  ClasseMainDoProjeto.main(new String [] { "##a1" });  
  String output = baOut.toString();  
  assertEquals("Invalido", output)  
}

<br>

**Selenium**: Ferramenta para testes de aplica????o Web.  

- Desenvolvido como extens??o do Firefox
- Permite gravar, editar, e depurar testes
- Permite criar manualmente ou gravar passos para execu????o de teste funcional

Vantagens da ferramenta Selenium:

- A instala????o ?? local e simples.
- ?? muito f??cil de usar.
- Permite gravar sess??es de teste para uso posterior.
- Permite exportar as sess??es de teste como arquivos fonte Java, C#, Perl, PHP, Python
e Ruby, que podem ser usados pelo Selenium RC.
- Excelente para quem inicia o uso do Selenium.
- N??o ?? preciso saber programar.

Desvantagens:

- Funciona como plugin apenas no FireFox.
- Possui algumas limita????es para testes mais complexos.

Permite testes funcionais, de regress??o e desempenho, e ?? *opensource*  
Permite integra????o com v??rias linguagens e frameworks  
OBS: Caso de teste n??o ?? salvo isoladamente, **necess??rio salvar a Suite de Testes**

## Testes Estruturais

Tem como objetivo garantir que todas as estruturas que compoe o programa est??o funcionando.  
Usa o c??digo do programa para definir os requisitos de teste, e com eles os casos de teste.

**Abstra????o da estrutura do programa**: Grafo de Fluxo de Controle  

![Exemplo de grafo](https://slideplayer.com.br/slide/3688953/12/images/49/Grafo+de+fluxo+de+controle%3A+Exemplo.jpg)

Crit??rios baseados em *Fluxo de Cotrole*: escolher casos te deste que exercitem todos os elementos do grafo

- Crit??rios "Todos-n??s"  
Casos de teste que fazem com que todos os n??s do fluxo sejam executados (pelo menos uma vez)  
Defino entradas para o programa de forma que passe por todos os n??s  
**Teste de cobertura de comandos**
- Crit??rio "Todos-arcos"  
Casos de teste que fazem com que todos as arestas (linhas) sejam executados (pelo menos uma vez)  
**Cobertura de ramos/desvios**

*Pode-se ignorar requisitos n??o-execut??veis*

Crit??rios baseados no *Fluxo de Dados*: al??m do grafo utilizam informa????es sobre a utiliza????o de vari??veis dentro da fun????o.

Defni????o de v??riavel = ponto em que ela recebe um valor  
Uso da vari??vel = ponto em que ?? utilizada, em um c??lculo (associada a n?? do grafo) ou condi????o (associada a aresta do grafo)

Identificando os usos e as defini????es das vari??veis, temos como requisitos de teste, o que chamamos de associa????es, defini????o e uso;  
**Temos que encontrar um dado de teste que fa??a com que a execu????o passe pelo n?? e alcance a aresta desesjada, sem que haja uma *redefini????o* dessa vari??vel**

Resumo geral - Crit??rios de Teste Estrutural

- Requisitos n??o execut??veis
- Exercitar c??digo
- Fluxo de controle: usa apenas GFC
- Fluxo de dados: usa GFC + vari??veis
- Todos-n??s
- Todos-arcos

Programa:

      int validateIdentifier(char* s) { 

      char achar; 

      int i, valid_id = FALSE; 

      if (strlen(s) > 0) { 

          achar = s[0]; 

          valid_id = valid_s(achar); 

          if (strlen(s) > 1) { 

            achar = s[1]; 

            i = 1; 

            while (i < strlen(s)) { 

                achar = s[i]; 

                if (!valid_f(achar)) 

                  valid_id = FALSE; 

                i++; 

            } 

          } 

      } 

      if (valid_id && (strlen(s) >= 1) && (strlen(s) < 6)) 

          return TRUE; 

      else 

          return FALSE; 

Ferramenta de apoio: Informam quais requisitos j?? foram executados e quais ainda faltam.

- [JaBUTi](http://www2.ccsl.icmc.usp.br/pt-br/projects/jabuti)
- [Eclemma](http://www.eclemma.org/)
- [Cobertura(http://cobertura.github.io/cobertura/)]
- [gcc/gcov/gcover](http://gcovr.com/)

*GCC - GNU Compiler Colection:* C??digo ?? compilado para colheta de informa????es.  
Executando o c??digo ?? poss??vel saber quais trechos foram executados.  
Cria arquivo < nomeDoPrograma >.gcno que descreve o grafo de fluxo de controle do programa.  
GCOVER recebe estes arquivos e gera um html com as informa????es (m??tricas) de cobertura, comandos (n??s) e desvios do programa.

>GCC ??? GNU COMPILER COLLECTION - Comandos para compilar:  
gcc -fprofile-arcs -ftest-coverage identifier.c -o identifier  
identifier.c identifier.gcno  
GCOVR - Visualizar o resultado  
gcovr -r . --branches --html --html-details -o identifier.html

## Testes de Muta????o

Utiliza conhecimento sobre os defeitos t??picos que podem ocorrer no programa para criar bons conjuntos de testes.  
Criamos v??rios programas que chamamos de **mutantes**  
  - possuem pequenas modifica????es rela????o ao programa original

Os casos de teste t??m que para cada um dos mutantes o sistema apresenta resultado incorreto.  

*Avaliar os Casos de Teste*: Contar quantos mutantes conseguem ser eliminados  
Score de muta????o = (mutantes mortos) / (total de mutantes)  
(taxa de mutantes mortos)

**Operadores de muta????o:** Regras que definem as altera????es necess??rias para que mutantes sejam criados.  
Relacionam com a linguagem na qual o programa foi escrito. Exemplo da linguagem C:
- aquele que alteram comandos inteiros do programa
- aqueles que alteram operadores da linguagem
- que alteram vari??veis e que alteram constantes

**Se usarmos todos os operadores de muta????o o n??mero de mutantes tende a ser muito grande**  

*Operador ORRN:* faz a troca de operador relacional por outro operador relacional (exemplo trocar > por <, ou = por !=).  
Para cada 1 operador, cria-se 5 mutantes (total de 6 operadores)  
>Operadores: >  <  >=  <=  =  !=  

Quando o resultado do mutante ?? diferente do resultado original (esperado), considera-se o mutante morto.

**Mutantes Equivalentes:** aqueles que n??o podem ser mortos (s??o descartados)  
Score de muta????o = (mutantes mortos) / (total de mutantes - mutantes equivalentes)

Esquem??tico:  
![Testes de Muta????o](https://arquivo.devmedia.com.br/revistas/es/imagens/51/07_mutacao/image001.png)  
<br>

**Proteum**: [ferramenta](http://www2.ccsl.icmc.usp.br/pt-br/projects/proteum) que d?? suporte a teste de muta????o para linguagem C  
Programa recebe como argumento String e precisa dizer se ?? identificador v??lido ou inv??lido.  
Identificador v??lido tem at?? seis caracteres e todos eles devem ser letras ou d??gitos. E o primeiro caractere deve ser uma letra.

Testar fun????o que valida o caracter para o identificador  
1. Criar sess??o de testes
2. Selecionar fun????es do programa a serem testadas
3. Selecionar operadores que ser??o usados (ORRN)
    - Posso selecionar a porcentagem de mutantes que ser?? gerada
4. Adicionar casos de teste para tentar matar os mutantes
5. Executo os mutantes e verifico se foram mortos
    - Analiso mutantes que n??o foram mortos e crio novos casos
6. Posso gerar mais mutantes

Outras ferramentas:

- [MuJava](https://cs.gmu.edu/~offutt/mujava/)
- [Major](http://mutation-testing.org/)
- [Pitest](http://pitest.org/)
Se voc?? gerar todos os mutantes, para todas as fun????es do programa identifier (1245 mutantes) e adicionar os 7 casos de teste do v??deo, quantos mutantes ser??o mortos e qual ser?? o escore de muta????o obtido (sem marcar mutantes equivalentes)?    


## Depoimento de QA

Depois da reuni??o de planejamento, come??ar a escrever os cen??rios de teste utilizando a metodologia BDD e a linguagem Gherkin.  
Para ler esses cen??rios de teste utilizar Python e Selenium, frameworks mais utilizados hoje dia para testes de automa????o.  

Para novas features: sempre realizar teste de sanidade automatizado - garante que as funcionalidades passadas do sistema n??o foram quebradas por essa nova funcionalidade;
A nova feature ?? testada manualmente;

Existem tr??s tipos base para a realiza????o dos testes: teste de **muta????es**, os testes **estruturais** e os testes **funcionais**  
O teste de **muta????o** nada mais ?? do que validar os testes no c??digo.  
Realiza muta????es cima dos testes e, *caso o teste passe o mutante esta vivo*. Quer dizer que os **testes est??o fr??geis**  
Caso o mutante esteja morto os testes falharam, o que ?? o correto.  

Testes estruturais s??o os testes caixa branca, que testam a parte interna do sistema, ou seja, o nosso c??digo-fonte:

- Testes de stress;
- Testes de carga;
- Testes de unidade;
- Testes de comportamento;
- Testes de integra????o;

Tem ent??o os testes Funcionais, do tipo caixa preta. Utiliza partes visuais, que o usu??rio vai usar.  
Entender como a aplica????o est?? se comportando e como deveria se comportar com base nas especifica????es e requisitos dados.

- Testes de regress??o, que v??o testar basicamente o que j?? existia;
- Testes de fuma??a, que v??o testar o core do sistema, ou seja, o intuito principal da nossa aplica????o;
- Teste de aceite, que ?? o teste baseado requisitos, ou seja, o valor que o cliente colocou cima da aplica????o;
- Testes automatizados que basicamente testa toda a parte visual, pensando que os outros testes j?? tenham sido realizados.
