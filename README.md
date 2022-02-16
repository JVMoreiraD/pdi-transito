# Trabalho para a cadeira de Processamento de Imagens

### Autores desse Portfolio:
    João Victor de França Leitão
    João Vitor Moreira Duarte

## Este trabalho é uma adaptação do artigo Processamento Digital de Imagens Aplicado a Identificação Automática de Placas de Trânsito.

## Autores do Artigo original:
    Thiago de Jesus Oliveira Duraes
    Lucas Soares Maciel
    Wagner Ferreira de Barros

# Metodologia Original:
### 1. Segmentar a imagem de entrada com o objetivo de ressaltar uma porção desta imagem que se encontre na mesma faixa de cores da placa a ser localizada.

### 2. Processar o objeto identificado para verificar se ele pode ser caracterizado como uma placa de pare.

### Para realização do primeiro passo, primeiro é necessário converter a imagem de entrada para um espaço de cores mais adequado e, posteriormente, analisar os histogramas que caracterizam as cores da imagem para extrair da imagem a informação desejada. De posse do resultado obtido no passo inicial, deve-se agora processar a informação obtida para identificar a forma geométrica do objeto identificado. Para isto, optou-se por identificar os diversos segmentos de retas que contornam o objeto identificado por meio da Transformada de Hough.

<br>

# Links importantes:
    Artigo original: http://ojs.unirg.edu.br/index.php/1/article/view/2280
    dataset original: https://github.com/mbasilyan/Stop-Sign-Detection

## O que foi feito de diferente ?

### Diferente do artigo original usamos Python e OpenCV no lugar de Toolbox de Processamento de Imagens do Matlab, MATHWORKS (2017), no Matlab R2015. Evitamos fazer o algo parecido com o imfill para preencher o interior das placas e no lugar de verificar objetos com tamanho igual a 10% da imagem verificamos objetos com area de no minimo 1% da imagem.

### Primeiro fizemos um rezise das imagens antes de fazer o processamento, em seguida aplicamos um blur na imagem original visando diminuir o ruido, fazendo a transformação para HSV buscando separar os pixels vermelhos da imagem, feito isso fazemos um contorno e aplicamos a transformada de Hough, para contar as retas que formam o formato da placa de pare dessa forma identificando o objeto.


## Resultados Obtidos:

| Tipo                 | Quantidade |
| -------------------- | ---------- |
| Resultado Esperado   | 59         |
| Resultado Com Glitch | 7          |
| Resultado Parcial    | 2          |
| Falhas               | 29         |
| Total                | 97         |


    Resultado esperado: Quando conseguimos exatamente a placa.
    Resultado com glitch: Quando conseguimos a placa mas algo no contorno não saiu como esperado.
    Resultado parcial: Quando existe mais de uma placa na imagem e nem todas são identificadas.
    Falhas: Quando nenhum objeto é contornado e nenhuma placa é identificada.