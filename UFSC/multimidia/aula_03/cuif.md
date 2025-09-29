Exemplo de CUI.1, representado em um arquivo CUIF
Vamos supor uma imagem com 2 ×2 pixels:
- red = (FF 00 00)16
- blue = (00 00 FF)16
- green = (00 FF 00)16
- gray = (B7 B7 B7)16

Para este exemplo, há apenas um estudante no grupo, cuja matrícula é 23100455.
Vejamos como fica a organização de um arquivo CUIF para armazenar essa 
imagem seguindo o padrão CUI.1:

| byte  |       valor    | significado |
|           | 3  |   2   |    1   |  0    |                    |
|-----|-----|-----|-----|-----|-------------------------------|
| 0     |  –     |  CUIF                | assinatura CUIF |
| 4     |  –     |   –    |  –    |  1    | versão do padrão CUI (CUI.1) |
| 5     |  –     |   –    |   –   |  1    |  número de estudantes no grupo |
|  6    |              2(10)              |       largura  |
| 10    |             2(10)              |       altura     |
| 14    |  99132042(10)          |  matrícula do aluno no grupo | 
| 18    |  –     |   –    |   –   | F F(16)  |  R pixel 0,0 | 
| 19    |  –     |   –    | –     | 0016     |R pixel 0,1 |
| 20    |  –     |   –    | –     | 0016     | R pixel 1,0 |
| 21    |  –     |   –    | –     |  B716     | R pixel 1,1 |
| 22    |  –     |   –    | –     |  0016    | G pixel 0,0 |
| 23    |  –     |   –    | –     |  F F16   |  G pixel 0,1 |
| 24    |  –     |   –    | –     |  0016    | G pixel 1,0 |
| 25    |  –     |   –    | –     |  B716    | G pixel 1,1 |
| 26    |  –     |   –    | –     |  0016    | B pixel 0,0 |
| 27    |  –     |   –    | –     |  0016    | B pixel 0,1 |
| 28    |  –     |   –    | –     |  F F16   |  B pixel 1,0 |
| 29    |  –     |   –    | –     |  B716    | B pixel 1,1 | 