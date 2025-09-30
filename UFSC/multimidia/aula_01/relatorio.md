Procedimentos:

1) Entre no colab https://colab.research.google.com/ e abra um notebook com o código abaixo e faça o upload do arquivo audio.wav. Este arquivo tem uma taxa de amostragem de 44.1Khz, 16 bits/amostra e é mono. 

2) Estude o código python

3) Responda as questões abaixo:

A) Vá no notebook e altere o som para manter os parâmetros próximos do original: 40kHz e 16 bits por amostra. Em seguida responda:

i) Qual é a maior frequência de som no arquivo?

ii) Indique o maior componente de frequência (em Hertz) possível quando estes parâmetros de digitalização são utilizados.

iii) Qual é o tamanho teórico do áudio (parte de dados);

iv) O tamanho do arquivo em bytes (ver propriedades do arquivo, ou Linux utilize o comando "ls -l audio.wav) e indique o motivo da diferença entre este tamanho e o calculado em ii).

v) O tamanho do arquivo em disco em bytes, observando as propriedades do arquivo, ou no linux utilize "du -s -B1 audio.wav", e indique o motivo da diferença entre este tamanho e o tamanho do arquivo em ii).

vi) Indique o o tamanho deste arquivo em disco se  o seu HD fosse formatado para um tamanho de bloco (unidade de alocação em disco) de 2048 B.

B) Utilize agora o notebook para alterar a taxa de amostragem para 10kHz,   e mantendo 16-bits por amostra, e responda: 

i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?

ii) Qual é o tamanho em bytes da parte de dados do áudio após esta conversão?

C) Utilize agora o notebook para alterar a taxa de amostragem para 4kHz   e mantendo 4-bits por amostra, e responda: 

i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?

ii) Qual é o tamanho teórico em bytes da parte de dados do áudio após esta conversão?

iii) O arquivo de áudio gerado no notebook mantém 4 bits por amostra no arquivo?