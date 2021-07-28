# Courses

## Cursos

docs.cypress.io (documentação completa)  
**Assertiva:** o que garante que a ação resulta no comportamento esperado  
Assertivas ficam sendo feitas até o Timeout (enquanto resultado não for positivo)

JQUERY selector: se quero pegar elemento pela tag pego só a tag  
OBS: necessário instalar para rodar (mesmo já tendo a pasta)  
PARA GRAVAR TESTE: cypress run --record --key  f46218ff-2d98-4e42-ac0cfc97f1c8b891  
Cypress framework de testes automatizados  

- Junta framework, biblioteca pra integração e comunicação  
- Cypress faz sem o selenium

Cypress **não suporta multiplas abas** (alguns testes são rodados com algumas abas)  
Time Reckets - usar o protec (conseguiram fazer o login por request)  
POC Cypress: Regra de cobrança, Faturamento, Boleto;  
Desenhar fluxo do workflow no Cypress (tem suporte pra action de mouse) 

- Comunidade está muito ativa  
- Execução em paralelo é boa:
- Única linha de comando para executar na minha máquina
- Selenium: pega, joga pro Hub e distribui pra todos os testes

Executo a linha, ela tem um ID, se eu pedir pra rodar em outra maquina com outro ID ela já é considerada em paralelo (tem um time-out, para esperar quantas maquinas vão executar aquele ID) - depois que sabe quantas pessoas.  
**Não executa por método de testes, executa por arquivos.**  
Recomendam dividir bastante as ações pra cada arquivo (1 pra cadastrar processo, 1 pra pesquisa simples, etc).  
> Executa 1 vez, 1 arquivo leva 1h e outro 3min: define que na próxima execução a máquina 1 fica só com esse tipo de arquivo, e máquina 2 pega esse outro arquivo.  
> Não terão 200 testes em 1 arquivo só.  
> Pegar smoke test com playlist gigante e separar.  

O próprio cypress consegue fazer o gerenciamento de processamento.  

**Relatório no cypress:** consegue filtrar muito (status, duração, suit size, top failures)  
Flaky tests (os que variam muito se passa ou não passa)  
Cypress vê o clique na tela e grava pra vc (pega o básico) – uma macro.  

Não trabalha com Page Object, trabalha com Action! Dá pra usar, aceita, MAS não 
é o que trabalha (mudar pra action pode ser ruim para arquivos muito grandes) 

Ao invés de mapear a tela numa classe e deixar separada, implemento ela em uma 
action - e consigo fazer virar comandos

Cypress utiliza muito promises (comunicação assincrona)!  
Cypress funciona de maneira ASSINCRONA

Para receber dicas apropriadas do VS Code:  

> /// < reference types = "cypress" />  

https://www.cypress.io/blog/2019/01/03/stop-using-page-objects-and-start-using-app-actions/#final-thoughts  
  
**Observações**
Extensão: Cypress.helper -- VSCode  

> Selenium: wait (ou sleep) MUITO usado  
> Cypress: ele mesmo consegue esperar requisição, etc (foi desenv em cima das dificuldades do selenium)

Debug Cypress: traz todas as requisições, todas as ações - vejo exatamente qual requisição esta falhando, onde falhou ele grava todos os testes, que falharam e passaram  
Cypress aceita *TypeSript* e *JavaSrcript*  

- *Typescript* tem tipos (tipo num, array, string)
- *JavaScript* aceita tudo na declaração da variavel (pode bagunçar mas facilita)

Trazer vanagens do Cypress vs Selenium  
Cypress é todo free mas a execução paralela FREE só 400 testes por mês
(precisaremos pagar)  

- Comparativo entre as regressões (sem POC nao da)
- Positivos e negativos
- Custos

Tudo é feito no browser, por isso muito mais rápido!  
SELENIUM GRID - Executa em paralelo  
AKS = Serviço da microsoft trabalha com Docker  
ambiente de testes  
chego na pipeline: quero executar 200 testes em paralelo  
ele gera maquina (linux)  
tenho tudo do selenium grid NO oks  
aerofunction (node.js) - passa só o parenteses  