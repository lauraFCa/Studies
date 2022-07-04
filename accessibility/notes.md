# Test Automation For Accessibility

[Curso - Test Automation for Accessibility](https://testautomationu.applitools.com/accessibility-testing-tutorial/)

Melhor acessibilidade leva a melhor experiência do usuário;  
Melhor acessibilidade leva a aumento de público;

## Web Content Accessibility Guidelines 2.0 e 2.1

- Perceivable: informação deve se adaptar a diferentes usuários (perceptível);
- Operable: uuários devem ser capazes de operar o website de maneiras diferentes (operável);
- Understandable: usuários devem conseguir entender a informação na tela (compreensível);
- Robust: website deve ser usável por tecnologias assistivas de terceiros (robusto);
- Mobile accessibility: Acessível em modo paisagem e modo retrato;
- Low vision: Deve ser possível dar zoom;
- Cognitive and Learning abilities: Se houver animações, deve ser possível desabilitá-las;

## Web Accessibility Testing Checks

- Tag título da página
- Alt de imagens
- Headings (cabeçalhos)
- Contraste de cores
- Estrutura do HTML
- ARIA labels (atributo usado para nomear elementos não-visíveis na tela)

Lembrar:
- Feedback na submissão de formulários
- Clareza nos sub-titulos
- Animações permitem ser desativadas
- Conteúdo acessível com teclado
- Elementos são focáveis
- Fontes claras
- Níveis de áudio podem ser modificados
- Layout responsivo

### Ferramentas de acessibilidade

Ferramentas comuns, manuais:
- Teclado
- Leitores de tela
- Zoom

Ferramentas de teste semi-automatizado:
- Axe: extensão do navegador, que gera relatório de acessibilidade
- WAVE: outra extensão, permite também analisar problemas de contraste
- Google Lighthouse: Ferramenta nativa do Chrome, verifica *acessibiliade*, performance, melhores práticas e SEO (para versão mobile e desktop)

Ferramentas de teste automatizado:  
- Axe Core:
    - Axe CLI
    - Jest Axe
    - Cypress-Axe
    - Axe Selenium
    - Axe WebdriverIO
    - Axe TestCafe
- Applitools Contrast Advisor

### Usando Axe CLI

Requisitos: *node*  
Instalação: *npm install -g axe-cli*  
Inspeção headless: *axe < url >*  
Inspeção abrindo o navegador: *axe < url > --browser chrome*

Para analisar **mais de uma página** basta separar as URLs por vírgula:  
*axe < url1 >,  < url2 >*

Para **desabilitar** a analise de um parametro:  
*axe < url> --disable < parametro>*

Para **salvar** os resultados (em json):  
*axe < url> --save nome_arquivo.json*

