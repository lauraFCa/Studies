# Robot Framework in Python

## Resumo

[Robot Framework](https://www.google.com/url?q=https://robotframework.org/&sa=D&source=editors&ust=1648407329979438&usg=AOvVaw23jcKJnJps1-m7ILRNbhSa) para Testes de API

Pré-requisitos

1.  Instalar [Python](https://www.google.com/url?q=https://www.python.org/downloads/&sa=D&source=editors&ust=1648407329979830&usg=AOvVaw2N9XOfgzacjGWgWqut4wAO)

2.  Adicionar às variáveis de ambiente  
    ![Example](https://docs.blender.org/manual/pt/dev/_images/about_contribute_install_windows_installer.png)

3.  Sugestão: criar um [ambiente virtual](https://www.google.com/url?q=https://youtu.be/Yp9EWlKfyqc&sa=D&source=editors&ust=1648407329980153&usg=AOvVaw3MPoOdsRveO4iZ07wbW_-_)

4.  Instalar [Robot Framework](https://www.google.com/url?q=https://robotframework.org/&sa=D&source=editors&ust=1648407329980346&usg=AOvVaw23Fe0VCfx7gk9koL9GX4k3)  
    >pip install robotframework  
    >robot --version  (para checar a instalação)

5.  Instalar biblioteca de requests - [Requests Library](https://www.google.com/url?q=https://github.com/MarketSquare/robotframework-requests&sa=D&source=editors&ust=1648407329980657&usg=AOvVaw3Y09JcyYkWvc_ZHV1xEI1s)  
    >pip install robotframework-requests

6.  Para execuções em paralelo - instalar [Pabot](https://www.google.com/url?q=https://pabot.org/&sa=D&source=editors&ust=1648407329980913&usg=AOvVaw2YrUCjm80-0vyzivDDBFmF)  
    >pip install -U robotframework-pabot

Estrutura do Robot

*   Arquivo dividido em seções: **Settings**, **Variables**, **Test Cases** e **Keywords**;
*   *Keywords* são os "métodos" criados para execução dos testes;
*   Baseia-se totalmente no espaçamento: sempre dar um mínimo de dois espaços entre os argumentos;


```
*** Settings ***

Documentation    Descrição deste arquivo (ou desta Suite de testes)

Library    RequestsLibrary    # biblioteca para realizar os requests da API
Library    Collections    # biblioteca que permite as validações em JSON

Suite Setup       Ação que será executada antes de toda a classe de testes
Suite Teardown    Ação que será executada ao final de toda a classe de testes
Test Setup        Ação que será executada antes de cada um dos testes
Test Teardown     Ação que será executada ao final de cada um dos testes

*** Variables ***

${VARIAVEL}    Valor da variável

*** Test Cases ***

Caso de teste 01
    [Documentation]    Descrição do método
    [Tags]    tag1    tag2    Incluir
    Primeira ação a ser executada    ${VARIAVEL}    # variável de input para o teste
    Segunda ação a ser executada


Caso de teste 01
    [Documentation]    Descrição do método
    [Tags]    tag1    Excluir
    Primeira outra ação a ser executada
    Segunda ação a ser executada


*** Keywords ***

# SETUPS E TEARDOWS

Ação que será executada antes de toda a classe de testes
    [Documentation]    Descrição da keyword (método)
    Log    Este é o Suite Setup    # printa o valor no Log de execução do Robot
    Create Session    ${ALIAS}    https://endpoint.com

Ação que será executada ao final de toda a classe de testes
    [Documentation]    Descrição da keyword (método)
    Log    Este é o Suite Teardown
    Delete All Sessions

Ação que será executada antes de cada um dos testes
    [Documentation]    Descrição da keyword (método)
    Log    Este é o Test Setup

Ação que será executada ao final de cada um dos testes
    [Documentation]    Descrição da keyword (método)
    Log    Este é o Test Teardown


# METODOS

Primeira ação a ser executada
    [Documentation]    Descrição da keyword (método)
    [Arguments]    ${parametro}
    Log to Console    ${parametro}    #printa o valor no terminal

Segunda ação a ser executada
    [Documentation]    Descrição da keyword (método)
    ${RESPOSTA}        GET On Session    ${ALIAS}    Books    # GET na sessão criada previamente, no endpoint https://endpoint.com/Books
    # resposta do GET é salva na variável ${RESPOSTA}

Primeira outra ação a ser executada
    [Documentation]    Descrição da keyword (método)
    Log    \nOutra ação

```

>Usando o **VSCode**, instalar apenas a extensão: *Robot Framework Language Server (Robocorp)*

_

Documentações:

*   [Requests Library](https://www.google.com/url?q=https://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html&sa=D&source=editors&ust=1648407329988079&usg=AOvVaw1BiPMLHJoVNA9Ruy2lu5nU)
*   [BuiltIn Library](https://www.google.com/url?q=https://robotframework.org/robotframework/latest/libraries/BuiltIn.html&sa=D&source=editors&ust=1648407329988442&usg=AOvVaw0I6ad6Fk6n1V97R6bOcHkc) (padrão - importada automaticamente)
*   [Collections Library](https://www.google.com/url?q=https://robotframework.org/robotframework/latest/libraries/Collections.html&sa=D&source=editors&ust=1648407329988733&usg=AOvVaw3Ro_ooauo6brW35hP6DUAk) (padrão, mas precisa ser importada)
*   [Robot Framework](https://www.google.com/url?q=https://robotframework.org/?tab%3D2%23getting-started&sa=D&source=editors&ust=1648407329988935&usg=AOvVaw0zSMiIiekQGHTYac-upsye)
*   [Pabot](https://www.google.com/url?q=https://github.com/mkorpela/pabot&sa=D&source=editors&ust=1648407329989115&usg=AOvVaw1i2Nmdy5z7FeSGJbrDcrJ6)

[Robot Framework CI/CD with Azure DevOps](https://www.google.com/url?q=https://milannovovic.medium.com/robot-framework-ci-cd-with-azure-devops-cf708a64b389&sa=D&source=editors&ust=1648407329989317&usg=AOvVaw0GZ8SkAde2JVX23VB03vUr)

Curso - [Automação de Testes com Robot Framework - Básico](https://www.google.com/url?q=https://www.udemy.com/course/automacao-de-testes-com-robot-framework-basico/&sa=D&source=editors&ust=1648407329989542&usg=AOvVaw3DgVGzxTrXMm1DwTZuLUI9)

Exemplos de requests - [HTTP request method examples](https://www.google.com/url?q=https://robocorp.com/docs/development-guide/http/http-examples&sa=D&source=editors&ust=1648407329989767&usg=AOvVaw0InHUQiCKadQHsR1JWlPl6)

Linkedin Learning:

1.  [Robot Framework Test Automation: Level 1 (Selenium)](https://www.google.com/url?q=https://www.linkedin.com/learning/robot-framework-test-automation-level-1-selenium?u%3D102064650&sa=D&source=editors&ust=1648407329990036&usg=AOvVaw3OOnRWSzyriTci4EOz1QEq)
2.  [Robot Framework Test Automation: Level 2](https://www.google.com/url?q=https://www.linkedin.com/learning/robot-framework-test-automation-level-2?u%3D102064650&sa=D&source=editors&ust=1648407329990249&usg=AOvVaw1bjRW_dCIHvIfqyHMyKf7X)
3.  [Robot Framework Test Automation: Jenkins CI and Git Version Control](https://www.google.com/url?q=https://www.linkedin.com/learning/robot-framework-test-automation-jenkins-ci-and-git-version-control?u%3D102064650&sa=D&source=editors&ust=1648407329990493&usg=AOvVaw1C1yCn9_OijgXjG059iTbQ)
4.  [Robot Framework Test Automation: Sauce Labs](https://www.google.com/url?q=https://www.linkedin.com/learning/robot-framework-test-automation-sauce-labs?u%3D102064650&sa=D&source=editors&ust=1648407329990710&usg=AOvVaw1yq_WJ2F3nCqO9OKgiFvNi)  
_
>Quick tip - [Você quer Paralelismo, Métricas e Histórico? Venha para o RobotFramework](https://www.google.com/url?q=https://medium.com/@reuelja/voce-quer-paralelismo-m%25C3%25A9tricas-e-hist%25C3%25B3rico-venha-para-o-robotframework-3be916b622d5&sa=D&source=editors&ust=1648407329991043&usg=AOvVaw3-TOLGY04d6Lx-gupSi1pz)

<br>

## General Notes
Generic open source automation framework. It can be used for test automation and robotic process automation (RPA).  
Robot Framework is open and extensible, can be integrated with virtually any other tool to create powerful and flexible automation solutions and is free to use without licensing costs.

![Robot Framework Architecture](imgs//robotArchitecture.png)  
[More Info](https://youtu.be/d-KWz7euLlc)

- **Libraries**

  - **Builtin**: basic commands. Is imported automatically.  
    Assertions; Convert or Set variables; Logs; 
  - **Collections**: List or Dictionaries assertions
  - **DateTime**  
    Allows for simple calculations, like subtract time from date, and add time from time;
  - **Dialogs**: provides means for pausing test execution
  - **OperatingSystem**
  - **Process**: Running process in a system, starting processs, waiting for process
  - **Screenshot** (requires virtual or physical display for test)
  - **String** (manipulation and verification)
  - **Telnet**: connect telnet servers and execute commands
  - **XML**: verify and modify XML documents

- **Build-In Tools**

  1. Testdoc
  2. Rebot
  3. Libdoc
  4. Tidy

- **Test Cases**

  Robot framework test data defined in different sections.

    1ª. Settings
        Importing resource file librarires, variable files and defining metadata for test cases and test suits;  
    2ª. Variables
    3ª. Test Cases
    4ª. Pass
    5ª. Keywords
    6ª. Comments

  Can follow Workflow Tests, Data-Driven tests and High Level tests.

- **Keywords**

  Library keywords: Lowest level keywords, from the language used;  
  User keywords: One of the featuresof robot framework - making custom, high level keywords;

- **Variables**

  Defining and Using

- **Organizing Test Cases**

  - *Setups and Teardowns*

    Specif keyword to be executed before or after a test - use "*Test Setup*" and "*Test Teardown*".  
    To eecute before or after a test suit use "*Suit Setup*" and "*Suit Teardown*"

  - *Tags*

    Force tags and Default tags.  
    After execution the report will have tags with the test cases associated with them, and statistics based on the tags.

- **Selenium Library**

  Install *selenium library* and *browser drivers*

# [Automação de Testes com Robot Framework - Básico](https://www.udemy.com/course/automacao-de-testes-com-robot-framework-basico/)

Estruturado em Desenvolvimento Dirigido a Testes de Aceitação (ATDD);  
Baseado em *keyword driven* (escrita de testes alto nível);  
- Librarires: Selenium, Request (API), etc;
É possível desenvolver ou customizar libraries;

Camada "Test data" - onde entram as keywords (dados, ações) para desenvolver os testes;  
Robot busca as Librarires para interpretar os testes;

Executar *robot* e salvar resultados em uma pasta específica (cmd):

    robot -d pastaDosResults pastaComArquivosDeTestesParaExecutar

OU

    robot -d pastaResults pasta/arquivoEspecifico.robot

Exemplo de Log:  
![Robot - Exemplo de Log](imgs/RobotexLog.png)  
Exemplo de Report:  
![Robot - Exemplo de Report](imgs/RobotexReport.png)

> robot -d resultsAPI .

As Keywords são abstrações de suas implementações:

    Open Browser https://www.site.com chrome
Abstração de um script em Python (com Selenium WebDriver): 

    def open_browser(self): 
        self.driver = webdriver.Chrome()
        self.driver.implicity_wait(20)
        self.base_url = "https://www.site.com"
        self.verificationErrors = []
        self.accept_next_alert = True

- Fácil leitura, entendimento e **manutenção**;
- Sequencia de *keywords* pode se tornar a documentação;
- Bom para testadores não técnicos;

Libraries usadas:  
Acessar em [RobotFramework](https://robotframework.org/#libraries)  

Instalar - [Selenium Library](https://github.com/robotframework/SeleniumLibrary/#installation)  
[SeleniumLibrary Keywords](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)

Instalar - [API Library - *Requests*](https://github.com/MarketSquare/robotframework-requests#install-stable-version)

**Suite de Testes**: Todo o arquivo com todos os Test Cases.

**Setttings**: Configuração da Suite

- Documentation (keyword)
- Test Setup (keyword) *antes de cada teste*
- Test Teardown (keyword) *após cada teste*

> taskkill /im chromedriver.exe /f

Extensão do Chrome: [TruePath](https://qaworld.ga/truepath/)

Executar apenas um teste (um caso de teste):  
> robot -t "Titulo do caso de teste" nomeDoArquivo.robot

Ajuda do Robot:  
> robot --help

Executando com base em Tags

Executa apenas testes com a tag:  
> robot -i nomeTag nomedoArquivo.robot

Executa todos os testes exceto com a tag:
> robot -e nomeTag nomedoArquivo.robot

Substituir valor de uma variavel global:  
> robot -v VARIAVEL:valor nomedoArquivo.robot

## Execução em Paralelo

Utilizando [Pabot](https://pabot.org/)

> pip install -U robotframework-pabot

