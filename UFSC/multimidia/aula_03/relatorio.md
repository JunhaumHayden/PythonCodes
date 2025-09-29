# Relatório
Entregue via Moodle o relatório contendo as respostas das questões abaixo e o código modificado:

### **Questão 1**. 
Abra o arquivo lena.bmp no editor hexadecimal em https://hexed.it/ e, analisando o formato
do cabeçalho BMP apresentado na Seção 2, indique no relatório: qual é o valor dos campos offset e tamanho do
arquivo? Quais são os valores dos componentes de cor R, G e B do primeiro pixel armazenado no arquivo?

- `3600 0c00`: Tamanho do arquivo BMP em bytes (786486 bytes).
  - Como o formato é BGR em um BMP de 24 bits, os primeiros três bytes após o offset são:

      - Byte 54 (offset 0x36): 39 (Hexadecimal) -> Componente Azul (B)
      - Byte 55 (offset 0x37): 16 (Hexadecimal) -> Componente Verde (G)
      - Byte 56 (offset 0x38): 52 (Hexadecimal) -> Componente Vermelho (R)
      - Portanto, os valores dos componentes de cor do primeiro pixel (em hexadecimal) são:

        - B: 39
        - G: 16
        - R: 52
### **Questão 2**
Qual é o tamanho do cabeçalho do arquivo lena1.cuif para seu grupo?
- 4 bytes (assinatura) + 1 byte (versão) + 1 byte (número de estudantes) + 4 bytes (largura) + 4 bytes (altura) + (1 estudante * 4 bytes/estudante)

Calculando: 4 + 1 + 1 + 4 + 4 + (1 * 4) = 18 bytes.

Resp= O tamanho do cabeçalho do arquivo lena1.cuif é de 18 bytes.
   ### **Questão 3**
No arquivo praticaIII.py tem um função PSNR incompleta. Implemente esta função de maneira a
  calcular o PSRN passando como parâmetro a imagem original e uma decodificada. Implemente o cálculo do
  MAE e PSNR com base nas fórmulas da seção 5 .
- Ver anexo
   ### **Questão 4**
Indique o PSNR comparando a imagem original lena.bmp (original) com a imagem obtida a
  partir do arquivo CUIF.1 (lena1.bmp). Explique porque do resultado do PSNR para o caso do CUIF.1.
- Resp= O PSNR (Peak Signal-to-Noise Ratio) para este exemplo é infinito.
- Significa que o $MSE$ é zero portanto não há diferença entre a imagem original e a imagem decodificada, ou seja, quando as duas imagens são identicas pixel a pixel. Isso indica uma decodificação perfeita sem nenhuma perda de informação ou introdução de ruído.
   ### **Questão 5**
> Compacte as imagens lena.bmp e lena1.cuif com zip. 

Qual a taxa de compressão obtida para os dois arquivos? Qual arquivo compactou mais? Explique porque deste resultado, ou seja, indique a vantagem de
  organizar os pixels nesta sequência definida pelo CUIF.1 (primeiro os valores de R, depois de G e finalmente de B) para a compressão baseada em RLE ou DPCM? 
> Dica: relembre os princípios da compressão RLE e DPCM e
compare a parte de dados de imagem do arquivo lena.bmp e lena1.cuif no editor hexadecimal.
- A taxa de compressão (tamanho compactado / tamanho original) para `lena.bmp` foi de aproximadamente 0.9324.
- A taxa de compressão para `lena1.cuif` foi de aproximadamente 0.8179.
- O arquivo `lena1.cuif` obteve uma taxa de compressão melhor (menor valor) do que o arquivo `lena.bmp`.
- Isso ocorreu porque o formato CUIF.1 armazena os canais de cor (R, G, B) separadamente. Essa organização agrupa valores de pixels semelhantes dentro de cada canal, criando mais oportunidades para algoritmos de compressão lossless como RLE (Run-Length Encoding) e DPCM (Differential Pulse-Code Modulation) encontrarem padrões e redundâncias para reduzir o tamanho do arquivo. O formato BMP, que geralmente intercala os valores dos canais, não oferece a mesma vantagem para esses algoritmos.

 ### **Questão 6**
Agora altere o código em PraticaIII.py para que seja gerado o arquivo lena2.cuif, que utiliza a
  versão CUIF.2 (usar 2 em vez de 1 para indicação da versão) e lena2.bmp. Visualiza as imagens lena1.bmp e
  lena2.bmp para ver se existem diferenças visíveis. Analise o código que gera o arquivo CUIF.2 (em Cuif.py) e
  explique o princípio da compressão adotada no CUIF.2
- O CUIF.2 adota um princípio de compressão com perdas (lossy compression). Ele reduz a profundidade de cor de cada pixel de 24 bits (8 bits para cada canal R, G, B) para 8 bits totais por pixel. Isso é feito alocando 3 bits para o canal Vermelho, 3 bits para o canal Verde e 2 bits para o canal Azul. Os bits menos significativos de cada canal original são descartados, e os bits restantes são compactados em um único byte por pixel usando operações bitwise e shifts.
  
- ### **Questão 7**
Indique as taxas de compressão obtidas pelos CUIF.1 e CUIF.2 para a imagem lena.bmp? Para este
  cálculo determine a razão entre um arquivo cuif e a imagem lena.bmp. Qual versão do CUIF compactou mais?
- Taxa de Compressão CUIF.1: 
  -     Taxa = Tamanho lena1.cuif / Tamanho lena.bmp 
  -     Taxa = 787456 bytes / 787456 bytes = 1.0

- Taxa de Compressão CUIF.2: 
  -     Taxa = Tamanho lena2.cuif / Tamanho lena.bmp 
  -     Taxa = 263168 bytes / 787456 bytes ≈ 0.3342

Comparando as taxas de compressão (quanto menor o valor, maior a compressão):

- CUIF.1: 1.0
- CUIF.2: ≈ 0.3342

Resp= A versão do CUIF que compactou mais foi a CUIF.2.

### **Questão 8**
Indique o PSNR comparando a imagem original lena.bmp (original) com a imagem obtida a partir
  do arquivo CUIF.2 (lena2.bmp). Justifique a resposta do PSNR indicando a fonte do ruído.
- O PSNR (Peak Signal-to-Noise Ratio) entre a imagem original `lena.bmp` e a imagem decodificada `lena2.bmp` é:
  -     Cálculo do PSNR para CUIF.2: 19.780741729886877

- O PSNR de aproximadamente 19.78 dB indica que há uma diferença perceptível entre a imagem original e a imagem decodificada do CUIF.2. O PSNR não é infinito, o que significa que o MSE não é zero e, portanto, as imagens não são idênticas.

Justificativa da Resposta do PSNR e Fonte do Ruído:

- A fonte do "ruído" (ou, mais precisamente, a diferença que leva a um PSNR finito) no caso do CUIF.2 é a compressão com perdas utilizada neste formato.
Essa perda irreversível de informação durante a codificação introduz erros nos valores dos pixels decodificados em `lena2.bmp` em comparação com os pixels originais em lena.bmp. Essas diferenças pixel a pixel são o que a métrica MSE (Mean Squared Error) quantifica. Um MSE maior (indicando maiores diferenças) resulta em um PSNR menor.