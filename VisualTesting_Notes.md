# Learning Visual Testing with Applitools

[Test Automation University - Automated Viual Testing with C#](https://testautomationu.applitools.com/automated-visual-testing-in-csharp/)

## Starting

Pacotes necessários:
- *NUnit* (charlie poole)
- *NUnit Test Adapter* (chralie poole)
- *Selenium Webdriver Chromedriver* (jsakamoto)
- *Eyes.Slenium* (applitools)

Colocar o chromedriver no *bin*:  
1. Propriedades do projeto
2. Compilar (Build) 
3. Simbolos de combinação condicional (conditional compilation)
4. "*_PUBLISH_CHROMEDRIVER*"

## Applitools

Baseline = resultado esperado - como a UI deve aparecer (visualmente) em um ambiente

- Resultado esperado: screenshot da página em algum ambiente  
- Ação: screenshot da página non momento atual

Baseline é a união dos parâmetros:
- Browser
- OS
- Viewport size
- Test name
- App name

Applitools pode determinar esses parametros automaticamente.  
Applitools compara a primeira vez que viu a página ás execuções.

![Applitools flow](flow.png)

[Applitools course repository](https://github.com/nadvolod/applitools-csharp)

#### Tests

Match Level Settings:
- Exact: compara pixel a pixel (não é recomendado - o algorítico ignora mudanças não vistas por olho humano);
- Strict: Marca mudanças percetíveis ao olho humano (método padrão);  
  Ajuda a prevenir falsos positivos
- Content: Não marca diferenças em estilo (cores) apenas conteúdo(texto);  
  >Eyes.MatchLevel
- Layout: Confere o layout, se elementos estão nas posições corretas (ignora cor, conteúdo, etc)