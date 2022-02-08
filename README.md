# Trabalho de PDI

## Implementação do artigo Processamento Digital de Imagens Aplicado a Identificação Automática de Placas de Trânsito.

## Metodologia

### 1. Segmentar a imagem de entrada com o objetivo de ressaltar uma porção desta imagem que se encontre na mesma faixa de cores da placa a ser localizada.

### 2. Processar o objeto identificado para verificar se ele pode ser caracterizado como uma placa de pare.

### **To-do**

- [x] Converter imagem para de RGB para HSV.
- [x] Verificar aonde existe predominacia de pixels vermelhos.
- [ ] Recortar a imagem gerada aonde existe os pixels vermelhos se comporem, no minimo 10% da imagem original.
- [ ] Descartar objetos vermelhos de dimensão inferior a 10% da imagem.
- [ ] Aplicar filtro de Sobel para identificar as bordas do objeto.
- [ ] Dilatar imagem gerada para realizar junção das bordas de um mesmo objeto.
- [ ] Preencher o interior da placa.
- [ ] Remover qualquer objeto conectado que esteja em contato com qualquer extremidade da imagem de entrada.
- [ ] Aplicar erosão com auxilio de uma funçao similar a imerode, visando uma imagem mais bem definida do objeto de intersse.
- [ ] Aplicar imagem gerada nas etapas anteriores em um algoritmo de retas pela transformada de Hough.
- [ ] Usar detector de bordas ótimo de Canny
- [ ] Fazer o resto da To-Do