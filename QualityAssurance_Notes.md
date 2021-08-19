# Courses

## Course **Agile Testing**

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

### Backlog Grooming

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

## Course **Insights on Software Quality Engineering**

[Linkedin Learning Course](https://www.linkedin.com/learning/insights-on-software-quality-engineering)

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

## Notes **Automatização de Testes**

[Os 15 Erros mais Comuns na Automatização de Testes](https://www.youtube.com/watch?v=k4egg4trjgc&ab_channel=Pagar.meTalks)  

- Suportar testes (ao invés de replicar testes)  
Não apenas copiar e modificar testes que já existem (repassando erros)
- Testabilidade (testes também são códigos - precisam ser testados)
- Focar na experiencia do usuário (não a codificação)
- Problemas ao invés de ferramentas (definir o problema para depois ver se é necessaria/qual ferramenta)
- Foco no risco ao invés de cobertura (garantir que as partes mais criticas estão cobertas)
- Observabilidade, facilitando rastreio de falhas de teste

Testes deven avisar impactos e alterações de fluxo.

Armadilhas na automação de testes:
1. Testar tudo em apenas uma camada  

2. X

## Course **Introdução ao Teste de Software**

[Coursera Course](https://www.coursera.org/learn/intro-teste-de-software)

### História do Teste de Software

Diferença entre _tirar defeitos_ e _testar software_

`"O teste mostra presença, não ausência de erros"`

> 20/02 Dia Internacional do Teste de Software

A atividade de _testes_ é necessária porque humanos podem cometer erros.  
Esses erros podem ocorrerr devido a:

- complexidade do software desenvolvido,
- mudanças necessárias em software já existente e que pode levar a novas falhas,
- falta de uso de métodos que apoiem a validação e verificação da qualidade do software,
- situações imprevisíveis,
- questões pessoais e do próprio ambiente de trabalho e que interferem no desempenho do testador

**O teste é requerido para revelar a presença de defeitos, aumentar a confiança e satisfação do cliente com o software, e assegurar a qualidade do produto.**

É essencial prever ou garantir que falhas não ocorram, ou que _pelo menos sejam minimizadas_ ou identificadas o quanto antes.

### TMMI (Test Maturity Model integration)

Guia e framework para apoiar a melhoria de processos de teste (criando níveis).  
Estabelece requisitos necessários para que se tenha um processo de teste com qualidade.

> Assim como CMMI - Modelo de maturidade de software.

1. **Nível 1**  
   Nível caótico, todos os processos de teste estão aqui, e não requer que qualquer coisa seja contemplada.
2. **Nível 2**  
   Gerenciado, possui estratégia, planejamento, monitoramento, controle, projeto, execução e ambiente de teste.
3. **Nível 3**  
   Definido, possui organização, programa de treinamento, ciclo de vida e integração, teste não funcional e revisão por partes.
4. **Nível 4**  
   Gerenciamento quantitativo, medição de teste e avaliação e revisão avançada da qualidade do software.
5. **Nível 5**  
   Em otimização, o processo já tem muita qualidade e o objetivo é manter a qualidade e evluir constantemente.

Os requisitos para o processo de qualidade são chamados de **_áreas de processo_**.

Cada uma contém _objetivos específicos_, _práticas específicas_, _subpráticas_, e _objetivos genéricos_ e _práticas genéricas_.

Objetivos específicos são requeridos de serem alcançados.  
Práticas específicas são coisas que são esperadas que se faça para que os objetivos sejam alcançados.  
Subpráticas são de caráter mais informativo.

Objetivos genéricos e práticas genéricas, são comuns a várias áreas de processo.  
Descrevem características que podem ser utilizadas para institucionalizar o processo de teste dentro da organização.

O TMMI possui 81 práticas específicas, é o modelo mais pesado em termos de requisitos para a qualidade.  
Um estudo feito concluiu que das 81 práticas, 33 são realmente executadas e primordias.  

Referências:

- [Identifying a Subset of TMMi Practices to Establish a Streamlined Software Testing Process](https://ieeexplore.ieee.org/document/6800190)
- [Elaboração de um processo de teste com base em um estudo de caso real](https://repositorio.ufscar.br/handle/ufscar/519)
- [Characterising the state of the practice in software testing through a TMMi-based process](https://jserd.springeropen.com/articles/10.1186/s40411-015-0019-9)

### Habilidades de um bom profissional de Atividades de Software  

Equipe com metodologia ágil, SCRUM e KANBAN.  

- Gostar de programar (conhecimento de programação)  
  Para entender e saber utilizar e criar testes automatizados
- Mente criativa e curiosa (encontrar a fundo causa de problemas)
- Trabalho em equipe, com desenvolvedores, e todo o processo da empresa como um todo

- [15 Skills Every Software Tester Should be Mastered in](https://www.testing-whiz.com/blog/15-skills-every-software-tester-should-master-in-2017)
- [Formando Equipes Eficientes de Teste de Software](http://www.linhadecodigo.com.br/artigo/1419/formando-equipes-eficientes-de-teste-de-software.aspx#ixzz4tu5YXh7j)

Profissional de testes deve saber criar requisitos, casos de testes, encontrar problemas nos requisitos e testes. Deve também saber reportar as falhas encontradas.  
Além disso também deve saber priorizar casos de teste e bugs para que o software saia com o melhor resultado (manutenção de risco).

- Impostante: conhecer também estrutura de redes (testes de performance)
- **Ferramenta: Sonar Cube**

> Não existem produtos de qualidade, existem processos com qualidade!

<!-- ### Mapa Conceitual de Teste de Software

![Teste de Software](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/JQmZ_6SjEeesIgqlslw-IA_879eb74415eff3980e869ed729ac40b7_bf7591e0a4a211e78d872d02aebbf8f7.map.jpg?expiry=1627948800000&hmac=nBT_mnY823kgCpNc2NKq2M8EH8ghForqRNZpKW89Q9k) -->

### Terminologia da Área

**Engano**: Ação humana que produz resultado incorreto;  
**Defeito**: Passo incorreto na definição de dados (bug, erro, defeito);  
 Pode existir sem ser identificado (não se tornará um erro).  
**Erro**: Diferença entre a especificação e o que está ocorrendo, de fato;  
Se propagado para saída do software se torna *Falha*;  
**Falha**: Inabilidade do sistema de realizar a função requerida;  
Erro que chegou a saída;  

![Terminologias](https://miro.medium.com/max/1400/0*-3jSXEvLyiHROefw)  

- Importante conhecer termos e jargões
- Engano x Defeito x Falhas x Eros
- Definições nem sempre são seguidas
- Existem padrões internacionais que coletam e padronizeam a terminologia da área

### Etapas do Teste

**1. Planejamento**: Plano de Teste

  - Funcionalidades a serem testadas
  - Riscos associados
  - Requisitos de ambiente  

**2. Projeto dos Casos de Teste**: Elaborados

  - Refinar planejamento
  - Especificar os casos de teste
  - Especificação do Procedimento de teste (passos para execução)
  - Módulo testado, Descrição, Roteiro, Resultado esperado, Resultado do desenvolvedor e Resultado do teste.

**3. Execução**: Casos de teste elaborados  

  - Diário de teste (detalhes cronológicos da execução)
  - Relatório de incidente - qualquer evento ocorrido que precisa ser analisado depois
    - Status, Responsável pela correção, Prioridade, Descrição do erro, Data e nome de quem corrigiu
  - Relatório de encaminhamento de item (para desenvolvedores ou outros)

**4. Análise**: Avaliação do programa
  
  - Relatório de resumo de teste
    - Descrição do teste, pessoas envolvidas, número do teste (casos de uso criados antes, durante e depois, casos com erro, etc), Percentual de testes executados, com sucesso, com falhas e corrigidos.

**Importante:** Verificar documentação para cada etapa (por entidades internacionais)

### Fases da Atividade de Testes

Software confiável porém inseguro - requisitos estavam errados.  
Existem tipos distintos de *engano* e níveis diferentes de abstração.  
**Cada fase da atividade de teste tem um objetivo, e aborda diferentes tipos de erros e aspectos do software.**  

> 1. Teste de Unidade  
Erros simples de programação, pode ser feito pelo próprio dev
> 2. Teste de Integração  
Estrutura do software, encontra erros nas interfaces entre as unidades (feito após testes das unidades)
> 3. Teste de Sistema  
Erros de em funções, desempenho, **fora da especificação**, após o sistema ser finalizado
> 4. Teste de Regressão  
Feito após manutenções, garantindo que modificações não interferem com o sistema previamente em funcionamento e testado.

*Independente da fase existem etapas para a execução da atividade de teste.*

### Técnicas de Teste

Programa tem um domínio de entrada (todos os valores que podem ser usados para executar o programa).  
A partir do domínio seleciona um dado de teste e cria caso de teste a partir do domínimo.  
Verificar se para cada caso de teste a saída obtida é a esperada.

**Para domínios muito grandes posso definir subdominios e selecionar dados de teste que representem cada um deles.**

Regras ou Técnicas são usadas para identificar quando dados de teste devem estar no mesmo sub-domínimo ou não.

#### Teste Funcional

Parte da *especificação do software*.

- Particionamento em classes e equivalência
- Análise do valor limite
- Combinatorial
- Grafo causa-efeito

Pode ser feito em todas as fases de teste (unidade, integração e sistema)

#### Teste Estrutural

Parte do conhecimento da estrutura interna do programa (código).  
Critérios baseados em:

- Complexidade (McCabe)
- Fluxo de controle (todos-nós, todos-arcos, etc)
- Fluxo de dados (Rapps & Weyuker, Potenciais-usos)

Feito nas fases de teste de unidade e integração.

#### Teste de Defeitos

Parte de defeitos típicos, comumente vistos no sistema.  
Criar implementações alternativas para que o testador projete casos de teste que revelem os defeitos.

- Manutenção
  - Análise de mudanças
  - Manutenção de interface

Feito nas fases de teste de unidade e integração.

### Testes Funcionais

**Especificação dos requisitos do Software:**  
Utilizar o teste funcional para *projetar casos de teste*, *submeter casos no programa* e *verificar se a saída obtida* está de acordo com a saída que era esperada

- O usuário consegue fazer isso?
- Essa funcionalidade funciona?

Reflete a ótica do usuário/stakehoder que irá utilizar o programa.

Podem então ser reveladas inconformidades com os objetivos especificos:

- Funções incorretas ou ausentes
- Erros na interface
- Erros estrutura de dados
- Erros de acesso a softwares externos
- Inicialização e término do programa

Não requer o código fonte do sistema.  
Aplicada a todas as fases, pode ser executada manual ou automatizada.  

1. Identificar as funções que o sistema deve executar
2. Criar casos de teste para verificar funcionamento dessas funções
3. Executar casos de teste
4. Comparar resultados (obtidos e esperados)

Aplicar critérios para identificar os casos de teste de maior cobertura (melhores)

#### **Particionamento em Classes de Equivalência**

Qualquer elemento em um sub-conjunto irá representar o conjunto todos, e será usado para criar um caso de uso.  

1. Identificar classes de equivalência
    - Procurar termos como *intervalo*, *conjunto* ou palavras similares;  
    - Posso subdividir as classes (caso elementos similares sejam tratados de maneira diferente)
    - Verificar diretrizes pra dividir as classes
    - Definir classes válidas e inválidas

2. Gerar casos de teste para um elemento de cada classe
    - Definidos para classes válidas e inválidas

Exemplos:

Classe válida: Aquilo que o sistema espera

- Números *entre 20 e 30*
- Digitar apenas *1 número*
- Valores específicos em uma classe (ex: regras de imposto)

Classes inválidas: Fora do esperado pelo sistema

- Números *acima de 30* e *abaixo de 20*
- Digitar *mais de 1 número* de *menos de 1 número*
- Valores fora do esperado

Variáveis analisáveis:

- Comprimento da entrada (de 2 a 6 caracteres)
- Caractere inicial (inicia com uma letra)
- Corpo da entrada (contém apenas letras ou dígitos)

Crio casos de teste para cada variável, e cada classe.

> Teste Funcional  
Aplicações onde variáveis de entrada são facilmente identificadas  
Reduz domínio de entrada  
Classes podem ser definidas a partir de diretrizes, considerando condições de entrada

#### **Análise do Valor Limite**

Comlementa o particionamento em classes de equivalência.  
Dados de teste são selecionados considerando os valores limitantes das classes (máximo e mínimo).

Se a entrada exige intervalo de valores (10 a 20), são definidos dados nos limites e aquém a eles (9, 10, 20 e 21).  

Se a entrada exige tamanho de valores (1 a 100), são definidos dados de nenhum valor na entrada, os limites máximo e mínimo e aquém (0, 1,100,101)  

Se a entrada exige for uma lista ordenada (10 a 20), são definidos dados nos limites (primeiro e ultimo valor da lista) e além (9, 10, 20 e 21).  

> Teste Funcional  
Funciona junto com as classes de equivalência  
Explora valores nos limites das classes (e valor unitario acima)  
Diretrizes levam a determinação dos dados de teste

#### **Automatização de Testes Funcionais**

*JUnit:* Framework de teste de unidade para Java.

- Open Source
- Utiliza *Annotations para identificar métodos de teste*  
Meta tags adicionadas ao código:
    - @Test
    - @Before : dados necessários para execução do teste são carregados  
    (executa a cada caso de teste)
    - @After : fecha conexão com banco de dados  
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
  ClasseMainDoProjeto.main(new String [] { "###a1" });  
  String output = baOut.toString();  
  assertEquals("Invalido", output)  
}

<br>

**Selenium**: Ferramenta para testes de aplicação Web.  

- Desenvolvido como extensão do Firefox
- Permite gravar, editar, e depurar testes
- Permite criar manualmente ou gravar passos para execução de teste funcional

Vantagens da ferramenta Selenium:

- A instalação é local e simples.
- É muito fácil de usar.
- Permite gravar sessões de teste para uso posterior.
- Permite exportar as sessões de teste como arquivos fonte Java, C#, Perl, PHP, Python
e Ruby, que podem ser usados pelo Selenium RC.
- Excelente para quem inicia o uso do Selenium.
- Não é preciso saber programar.

Desvantagens:

- Funciona como plugin apenas no FireFox.
- Possui algumas limitações para testes mais complexos.

Permite testes funcionais, de regressão e desempenho, e é *opensource*  
Permite integração com várias linguagens e frameworks  
OBS: Caso de teste não é salvo isoladamente, **necessário salvar a Suite de Testes**

### Testes Estruturais

Tem como objetivo garantir que todas as estruturas que compoe o programa estão funcionando.  
Usa o código do programa para definir os requisitos de teste, e com eles os casos de teste.

**Abstração da estrutura do programa**: Grafo de Fluxo de Controle  

![Exemplo de grafo](https://slideplayer.com.br/slide/3688953/12/images/49/Grafo+de+fluxo+de+controle%3A+Exemplo.jpg)

Critérios baseados em *Fluxo de Cotrole*: escolher casos te deste que exercitem todos os elementos do grafo

- Critérios "Todos-nós"  
Casos de teste que fazem com que todos os nós do fluxo sejam executados (pelo menos uma vez)  
Defino entradas para o programa de forma que passe por todos os nós  
**Teste de cobertura de comandos**
- Critério "Todos-arcos"  
Casos de teste que fazem com que todos as arestas (linhas) sejam executados (pelo menos uma vez)  
**Cobertura de ramos/desvios**

*Pode-se ignorar requisitos não-executáveis*

Critérios baseados no *Fluxo de Dados*: além do grafo utilizam informações sobre a utilização de variáveis dentro da função.

Defnição de váriavel = ponto em que ela recebe um valor  
Uso da variável = ponto em que é utilizada, em um cálculo (associada a nó do grafo) ou condição (associada a aresta do grafo)

Identificando os usos e as definições das variáveis, temos como requisitos de teste, o que chamamos de associações, definição e uso;  
**Temos que encontrar um dado de teste que faça com que a execução passe pelo nó e alcance a aresta desesjada, sem que haja uma *redefinição* dessa variável**

Resumo geral - Critérios de Teste Estrutural

- Requisitos não executáveis
- Exercitar código
- Fluxo de controle: usa apenas GFC
- Fluxo de dados: usa GFC + variáveis
- Todos-nós
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

Ferramenta de apoio: Informam quais requisitos já foram executados e quais ainda faltam.

- [JaBUTi](http://www2.ccsl.icmc.usp.br/pt-br/projects/jabuti)
- [Eclemma](http://www.eclemma.org/)
- [Cobertura(http://cobertura.github.io/cobertura/)]
- [gcc/gcov/gcover](http://gcovr.com/)

*GCC - GNU Compiler Colection:* Código é compilado para colheta de informações.  
Executando o código é possível saber quais trechos foram executados.  
Cria arquivo < nomeDoPrograma >.gcno que descreve o grafo de fluxo de controle do programa.  
GCOVER recebe estes arquivos e gera um html com as informações (métricas) de cobertura, comandos (nós) e desvios do programa.

>GCC – GNU COMPILER COLLECTION - Comandos para compilar:  
gcc -fprofile-arcs -ftest-coverage identifier.c -o identifier  
identifier.c identifier.gcno  
GCOVR - Visualizar o resultado  
gcovr -r . --branches --html --html-details -o identifier.html

### Testes de Mutação

Utiliza conhecimento sobre os defeitos típicos que podem ocorrer no programa para criar bons conjuntos de testes.  
Criamos vários programas que chamamos de **mutantes**  
  - possuem pequenas modificações relação ao programa original

Os casos de teste têm que para cada um dos mutantes o sistema apresenta resultado incorreto.  

*Avaliar os Casos de Teste*: Contar quantos mutantes conseguem ser eliminados  
Score de mutação = (mutantes mortos) / (total de mutantes)  
(taxa de mutantes mortos)

**Operadores de mutação:** Regras que definem as alterações necessárias para que mutantes sejam criados.  
Relacionam com a linguagem na qual o programa foi escrito. Exemplo da linguagem C:
- aquele que alteram comandos inteiros do programa
- aqueles que alteram operadores da linguagem
- que alteram variáveis e que alteram constantes

**Se usarmos todos os operadores de mutação o número de mutantes tende a ser muito grande**  

*Operador ORRN:* faz a troca de operador relacional por outro operador relacional (exemplo trocar > por <, ou = por !=).  
Para cada 1 operador, cria-se 5 mutantes (total de 6 operadores)  
>Operadores: >  <  >=  <=  =  !=  

Quando o resultado do mutante é diferente do resultado original (esperado), considera-se o mutante morto.

**Mutantes Equivalentes:** aqueles que não podem ser mortos (são descartados)  
Score de mutação = (mutantes mortos) / (total de mutantes - mutantes equivalentes)

Esquemático:  
![Testes de Mutação](https://arquivo.devmedia.com.br/revistas/es/imagens/51/07_mutacao/image001.png)  
<br>

**Proteum**: [ferramenta](http://www2.ccsl.icmc.usp.br/pt-br/projects/proteum) que dá suporte a teste de mutação para linguagem C  
Programa recebe como argumento String e precisa dizer se é identificador válido ou inválido.  
Identificador válido tem até seis caracteres e todos eles devem ser letras ou dígitos. E o primeiro caractere deve ser uma letra.

Testar função que valida o caracter para o identificador  
1. Criar sessão de testes
2. Selecionar funções do programa a serem testadas
3. Selecionar operadores que serão usados (ORRN)
    - Posso selecionar a porcentagem de mutantes que será gerada
4. Adicionar casos de teste para tentar matar os mutantes
5. Executo os mutantes e verifico se foram mortos
    - Analiso mutantes que não foram mortos e crio novos casos
6. Posso gerar mais mutantes

Outras ferramentas:

- [MuJava](https://cs.gmu.edu/~offutt/mujava/)
- [Major](http://mutation-testing.org/)
- [Pitest](http://pitest.org/)
Se você gerar todos os mutantes, para todas as funções do programa identifier (1245 mutantes) e adicionar os 7 casos de teste do vídeo, quantos mutantes serão mortos e qual será o escore de mutação obtido (sem marcar mutantes equivalentes)?    
