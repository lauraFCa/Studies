# Notes

## Biblioteca Pillow

(0,0) = canto superior esquerdo (primeiro pixel)  

- Image.getpixel((x,y)) : Retorna valor (RGB) do pixel em uma posição (input eh uma tuple)
- Image.putpixel((x,x),(r,g,b)) : substituir o valor de cor que está no pixel
Imagens em PNG resultam em 4 digitos de tupla (R,G,B,opacidade)

### Criando nova imagem do zero

Pillow docs -> Image -> New Image  
Image.new(mode = tipo de sistema de cor (RGB),  
            size = (Pixels Largura, Pixels Altura),  
            color = (default = 0 // tupla (R,G,B)))  

**Bandeira do Brasil:**  
largura = 20cm  
altura = 14cm  
raio = 3,5cm  
distancia losango as bordas = 1,7cm  

abertura.py

### Cores

Preto e branco ficam com exatamente mesmos valores para RGB  

- Brilho máximo = Branco
- Brilho mínimo = Preto
No preto e branco a informação dada é o brilho - intensidade.  
- Luminancia = quantidade para descrever um pixel na escala de cinza

Os pesos para considerar no RGB são padrão (30% Red, 59% Green, 11% Blue)  
Feito média ponderada para ter a Luminancia  

**Luz Visível**  
Toda cor enxergavel a olho humano está numa faixa específica de freqência  
Quando ela tem uma única frequência (não é mistura ou combinação de freqência) é cor MONOCROMATICA (ou Espectral Pura)  
Branco -> mistura de varias cores espectrais puras (com a mesma intensidade)  

Os 3 tipos de cones dos olhos:  

1. Faz amostragem em baixa frequência (verde)
2. Faz amostragem em alta frequência (azul)
3. Faz amostragem na zona intermediária (vermelho)
  
**Metamerismo:** quando duas cores tem frequências diferentes mas são percebidas como iguais (visão humana)  
Comprimeintos de onda: RED 700nm, GREEN 546nm, BLUE 435,8nm  

OUTRA CLASSE DE SISTEMA DE CORES  
Crominância e Luminancia: Separam iluminação do núcleo da cor (crominância)  
Para clarear ou escurecer no RGB, é necessário mexer em todas as cores.  
  
escala_cinza.py  
utils.py  
sinteticas.py  

### Filtros de Imagens

- Filtro: transformação UNÁRIA - não pode usar um elemento externo pra fazer modificações (utilza apenas valores que já estão presentes)
- Filtros convolucionais: Filtros lineares espacialmente invariante (mesmo comportamento em qualquer parte da imagem)

Regiões mais lisas são de baixa frequência.  
Filtro de borramento é de PASSA-BAIXA (filtra as frequencias altas / detalhes e contornos)  
Filtro de realce das bordas é de PASSA-ALTA (filtra as regiões homogenias/frequencias baixas)  

#### Filtros Convolucionais

- Linear: Causa modificação em imagem, que podemos calcular a partir de valores de pixel na região da imagem
Novo valor do pixel é média ponderada dos pixels no entorno.
- Espacialmente invariante: Se comporta da mesma maneira em todas as regiões da imagem
Combinação linear!  
- Filtro BOX: Todos os pesos da média ponderada são iguais - causa borramento
  
Borramento =~= espalhamento da quantiade de luz chegando na camera (aumenta regiões mais lisas)  
Matriz do filtro passa em cima da matriz da imagem (Padding: definir como zeros os valores da matriz nas extremidades)  

ImageFilter.BoxBlur(tamanho da matriz - numero de pixels para o lado)  
  
Aresta: regiões onde tem variação nos tons, fronteira entre objetos ou variação de textura.  

filtros.py

**Máscara Binária**: Criar outra imagem constituida de 0 e 1, que vai indicar onde deve fazer a substituição (CHROMA KEY)  

Sistema de Cor: HSV (Sistema circular, em graus e porcentagem) - color picker  
Hue: Cor (matiz - graus)  
Saturation  
Value  
