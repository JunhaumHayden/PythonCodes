# Gerar chaves com o openssl
Para gerar um par de chaves RSA, que inclui uma chave privada e, posteriormente, pode derivar uma chave pública a partir dela.
RSA: RSA é um dos algoritmos de criptografia de chave pública mais usados e confiáveis. Ele utiliza dois tipos de chaves: uma chave privada, que deve ser mantida secreta, e uma chave pública, que pode ser compartilhada abertamente. A chave pública é usada para criptografar dados, e a chave privada é usada para descriptografá-los.
4096 bits: Este valor define o nível de segurança da chave. Um tamanho de chave de 4096 bits é considerado altamente seguro e resistente à maioria dos ataques criptográficos modernos, mas é mais lento do que tamanhos menores como 2048 bits.

## Para chaves sem senha:
_Chave privada_

Comando:
```zsh
openssl genrsa -out chaveprivada.pem 4096
```
_Explicação dos Parâmetros_:
`genrsa`: Essa é a subcomando do openssl que gera uma chave privada RSA. Este comando cria um novo par de chaves RSA (privada e pública), onde a chave privada é gerada e armazenada.
`-out`: Esse parâmetro indica o nome do arquivo de saída onde a chave privada será salva. Neste caso, o nome do arquivo é `chaveprivada.pem`.
`chaveprivada.pem`: O nome do arquivo onde a chave privada RSA será gravada. O formato .pem (Privacy Enhanced Mail) é um formato de arquivo comumente usado para armazenar chaves criptográficas e certificados, codificados em Base64.
`4096`: Este é o tamanho da chave RSA, medido em bits. No exemplo, o valor 4096 especifica que a chave privada gerada terá 4096 bits de comprimento. Um número maior de bits significa uma chave mais segura, mas também aumenta o tempo de geração e o tempo necessário para realizar operações de criptografia e descriptografia.

_Chave publica_
Para extrair a chave pública de um arquivo que contém uma chave privada RSA.
OBS: Sempre deve-se vincular a um arquivo de chave privada
Sintaxe:
openssl [algoritmo de criptografia] [comando para informar que haverá um arquivo de saida com chave publica] [comando para passar o arquivo que contém a chave privada] [nome do arquivo de entrada] [comando para informar que haverá um arquivo de saida] [nome do arquivo de saida]
Comando:
```zsh
openssl rsa -pubout -in chaveprivada.pem -out chavepublica.pem
```
Resposta:
```zsh
writing RSA key
```
_Explicação dos parâmetros_:
`openssl rsa`: O comando rsa no OpenSSL é utilizado para manipular chaves RSA. Ele permite várias operações como extrair uma chave pública a partir de uma chave privada, converter entre diferentes formatos de chave, ou verificar a validade de uma chave.
`-pubout`: Esse parâmetro indica que se deseja extrair a chave pública da chave privada fornecida. O OpenSSL vai ler a chave privada e gerar a chave pública correspondente, que será escrita no arquivo especificado no parâmetro `-out`.
`-in chaveprivada.pem`: O parâmetro `-in` especifica o arquivo de entrada. Neste caso, o arquivo `chaveprivada.pem` contém a __chave privada__ que foi gerada previamente usando o comando `openssl genrsa`. O OpenSSL irá usar essa chave privada para gerar a __chave pública__ correspondente.
`-out chavepublica.pem`: O parâmetro `-out` define o arquivo de saída onde a chave pública extraída será salva. Neste caso, o nome do arquivo de saída será `chavepublica.pem`, e o formato do arquivo também será `.pem`.

_Exemplo de arquivo de chave pública_:
    O arquivo de saída chavepublica.pem geralmente terá o seguinte formato (Base64 codificado):

    ```zsh
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr5FNeXq...
    ... (mais linhas de chave codificada)
    -----END PUBLIC KEY-----
    ```
    Esta chave pública pode ser usada para criptografar dados, que só podem ser descriptografados usando a chave privada correspondente.

#### Criptografar um arquivo
A partir da versão 3.0 do OpenSSL, o comando `rsautl` foi deprecado e substituído por `pkeyutl` para operações de criptografia e assinatura. Para criptografar com uma chave pública usando `pkeyutl`, seguir a sintaxe abaixo.

```bash
openssl pkeyutl -encrypt -inkey chavepublica.pem -pubin -in test.txt -out testCriptografado.bin
```
  _Explicação dos parâmetros_:
    `pkeyutl`: O novo comando recomendado para operações criptográficas com chaves assimétricas.
    `-encrypt`: Indica que você quer realizar uma operação de criptografia.
    `-inkey` chavepublica.pem: Especifica a chave pública que será usada para criptografar.
    `-pubin`: Indica que o arquivo especificado em -inkey é uma chave pública (e não uma chave privada).
    `-in test.txt`: O arquivo de entrada contendo os dados que você deseja criptografar.
    `-out testCriptografado.bin`: O arquivo de saída onde os dados criptografados serão armazenados.

__Possíveis Tipos de Arquivos de Saída__
_Arquivo Binário (mais comum)_:
Extensão: `.bin`, `.dat`, ou sem extensão.
O arquivo de saída é um bloco de dados binários. Este é o formato padrão de saída quando se usa o comando `openssl pkeyutl` sem nenhum argumento adicional para codificação.
Exemplo:
```bash
openssl pkeyutl -encrypt -inkey chavepublica.pem -pubin -in test.txt -out testCriptografado.bin
```
O arquivo `testCriptografado.bin` será um arquivo binário, que pode conter bytes não imprimíveis.
_Arquivo Base64 (codificado em texto)_:
Extensão: `.txt`, `.b64`, `.pem`
Se precisar de um arquivo de saída codificado em texto (Base64), pode aplicar o comando `openssl base64` após a criptografia. Isso transforma o conteúdo binário em caracteres ASCII, o que facilita o armazenamento ou transmissão em sistemas que não suportam binários diretamente.
Exemplo:
```bash
openssl pkeyutl -encrypt -inkey chavepublica.pem -pubin -in test.txt -out testCriptografado.bin
openssl base64 -in testCriptografado.bin -out testCriptografado_base64.txt
``` 
Isso gerará um arquivo `testCriptografado_base64.txt` com o conteúdo em formato Base64, adequado para leitura humana e fácil transporte.
_Outros Formatos Específicos_:
Certificados ou Chaves PEM: Se estivesse gerando chaves ou certificados (não aplicável neste comando de criptografia), poderia usar arquivos com a extensão `.pem` (PEM codificado).
Outros formatos de armazenamento como DER: Usado para chaves e certificados, mas não é o formato de saída comum para este tipo de criptografia.
_Resumo_:
Binário (padrão, `.bin` ou sem extensão) é o formato mais comum para o arquivo de saída em operações de criptografia.
Base64 (`.txt`, `.pem`, `.b64`) pode ser usado se você quiser codificar o resultado em um formato de texto legível.

> Para ler e converter arquivos binários em um formato de texto legível (Base64) e vice-versa, você pode usar o comando openssl base64. Este comando permite codificar e decodificar arquivos binários para que possam ser armazenados ou transmitidos como texto.

#### 1. Codificar um arquivo binário em Base64
    Se tiver um arquivo binário e deseja convertê-lo para Base64, use o seguinte comando:

    ```bash
    openssl base64 -in arquivo.bin -out arquivo_base64.txt
    ```
_Explicação dos parâmetros_:
    `-in arquivo.bin`: O arquivo binário que deseja codificar.
    `-out arquivo_base64.txt`: O arquivo de saída que conterá os dados codificados em Base64.
    O arquivo `arquivo_base64.txt` conterá o conteúdo do arquivo binário em formato Base64, que será legível como texto.

#### 2. Decodificar um arquivo Base64 de volta para binário
    Se tiver um arquivo em Base64 e quiser convertê-lo de volta para o formato binário original, use o seguinte comando:

    ```bash
    openssl base64 -d -in arquivo_base64.txt -out arquivo.bin
    ```
_Explicação dos parâmetros_:
    `-d`: Indica que você deseja decodificar o arquivo Base64 de volta para o formato binário.
    `-in arquivo_base64.txt`: O arquivo com o conteúdo codificado em Base64.
    `-out arquivo.bin`: O arquivo de saída, que será o conteúdo binário original.

__Usando o comando base64 nativo no Unix/macOS__
1. Codificar um arquivo binário para Base64:
O comando base64 nativo faz a mesma coisa, mas sem o uso do OpenSSL:
```bash
base64 -i testCriptografado.bin -o testCriptografado_base64.txt
```
ou
```bash
base64 < testCriptografado.bin > testCriptografado.txt
```
_Explicação dos parâmetros_:
`-i` ou `--input`: Especifica o arquivo de entrada (neste caso, testCriptografado.bin).
`-o` ou `--output`: Especifica o arquivo de saída onde o conteúdo codificado será salvo (neste caso, testCriptografado.txt).
Este comando funciona porque ele lê o conteúdo do arquivo `testCriptografado.bin` como entrada (`<`) e redireciona a saída para `testCriptografado.txt` usando `>`.


2. Decodificar um arquivo Base64 de volta para binário:
Você pode também reverter o processo e voltar o arquivo Base64 ao binário:
```bash
base64 -d -i testCriptografado.txt -o testCriptografado.bin
```
ou
```bash
base64 -d < testCriptografado.txt > testCriptografado.bin
```

3. Verificando o conteúdo Base64 diretamente no terminal
Se você quiser simplesmente visualizar o conteúdo Base64 sem salvar em um arquivo de texto, você pode usar o comando:

```bash
openssl base64 -in testCriptografado.bin
```
ou

```bash
base64 testCriptografado.bin
```
Isso imprimirá a versão codificada em Base64 diretamente no terminal.

_Exemplo Completo_:
Criptografar um arquivo em binário:
```bash
openssl pkeyutl -encrypt -inkey chavepublica.pem -pubin -in test.txt -out testCriptografado.bin
```
Converter o arquivo binário para Base64:
```bash
openssl base64 -in testCriptografado.bin -out testCriptografado.txt
```
Visualizar o conteúdo Base64:
```bash
cat testCriptografado.txt
```
Reverter o arquivo Base64 para binário:
```bash
openssl base64 -d -in testCriptografado.txt -out testCriptografado.bin
```

Assim, você pode transitar facilmente entre arquivos binários e Base64 dependendo da necessidade.
#### Retornando ã mensagem original
Para retornar a mensagem original a partir de um arquivo codificado em Base64, o procedimento envolve a decodificação do arquivo Base64 de volta ao formato binário e, em seguida, descriptografar o arquivo binário usando a chave privada que foi originalmente usada para criptografá-lo. Aqui está um passo a passo detalhado para realizar isso:

_Cenário_:
- Arquivo Base64 codificado: testCriptografado.txt
- Arquivo binário original criptografado: testCriptografado.bin
- Arquivo de texto original (antes da criptografia): test.txt
- Chave privada para descriptografia: chaveprivada.pem
  
1. Decodificar o arquivo Base64 de volta ao formato binário
Primeiro, precisa decodificar o arquivo Base64 (`testCriptografado_base64.txt`) de volta ao arquivo binário (`testCriptografado.bin`).

Comando:

```bash
base64 -d -i testCriptografado_base64.txt -o testCriptografado.bin
```

`-d` ou `--decode`: Especifica que o Base64 deve ser decodificado.
`-i` ou `--input`: Especifica o arquivo de entrada (`testCriptografado.txt`).
`-o` ou `--output`: Especifica o arquivo de saída onde o conteúdo decodificado será salvo (`testCriptografado.bin`).
Agora, você tem o arquivo binário (`testCriptografado.bin`) que foi originalmente gerado pelo comando de criptografia.

2. Descriptografar o arquivo binário com a chave privada
Agora que se tem o arquivo binário decodificado, precisa descriptografá-lo usando a chave privada para recuperar a mensagem original.

Comando:
O comando para descriptografia, utilizando o openssl com a chave __privada__, será algo assim:

```bash
openssl pkeyutl -decrypt -inkey chaveprivada.pem -in testCriptografado.bin -out mensagemOriginal.txt
```
`pkeyutl`: O utilitário correto para operações com chave pública e privada no OpenSSL 3.0.
`-decrypt`: Indica que você deseja descriptografar o arquivo.
`-inkey chaveprivada.pem`: Especifica a chave privada que será usada para descriptografar (no caso, `chaveprivada.pem`).
`-in testCriptografado.bin`: O arquivo binário que foi criptografado.
`-out mensagemOriginal.txt`: Especifica o arquivo onde a mensagem descriptografada será salva (nesse caso, o conteúdo original da `test.txt` será salvo em `mensagemOriginal.txt`).

3. Verificar o conteúdo da mensagem original
Após a execução do comando acima, o arquivo mensagemOriginal.txt conterá a mensagem original que foi criptografada.

Pode-se visualizar o conteúdo desse arquivo com um editor de texto ou usar o comando `cat`:

```bash
cat mensagemOriginal.txt
```
_Resumo do Processo_:
Codificação Base64: `testCriptografado.bin` foi convertido para `testCriptografado_base64.txt` (Base64).
Decodificação Base64: Decodificar `testCriptografado_base64.txt` de volta para `testCriptografado.bin`.
Descriptografia: Usar a chave privada (`chaveprivada.pem`) para descriptografar `testCriptografado.bin` e obter a mensagem original (`mensagemOriginal.txt`).
Isso retorna o texto original, que foi criptografado inicialmente!

## Para gerar com senha:
- _Chave privada_
Para gerar uma chave privada RSA com criptografia simétrica AES-256 (algiritmo de encriptação da senha) aplicada ao arquivo que contém a chave privada.
O OpenSSL irá gerar a chave privada com 4096 bits de comprimento e criptografá-la com AES-256.
Comando:
```zsh
openssl genrsa -out chave-privada.key -aes256 4096
```
_Explicação dos parâmetros_:
    `openssl genrsa`: O comando `genrsa` é utilizado para gerar um par de chaves RSA (chave privada e chave pública). Nesse caso, se está gerando uma chave privada que pode posteriormente ser usada para extrair uma chave pública.
    `-out chave-privada.key`: O parâmetro `-out` especifica o arquivo de saída onde a chave privada gerada será salva. Neste exemplo, o arquivo de saída será `chave-privada.key`. O formato do arquivo será `.key`, mas você pode nomeá-lo como quiser.
    `-aes256:` Este parâmetro indica que a chave privada será criptografada usando o algoritmo de criptografia simétrica AES-256. AES (Advanced Encryption Standard) é um algoritmo de criptografia muito seguro, e a versão de 256 bits é uma das mais fortes.
    Ao utilizar este parâmetro, o OpenSSL pedirá que você insira uma senha para proteger a chave privada. Sem essa senha, ninguém poderá descriptografar o arquivo e acessar a chave privada diretamente.
    `4096`: Este número define o tamanho da chave em bits. Uma chave de 4096 bits é bastante forte, fornecendo um nível alto de segurança. O tamanho mínimo recomendado é 2048 bits, mas 4096 oferece uma segurança muito maior, apesar de ser mais lenta para operações de criptografia e descriptografia.

_Resposta do comando_:
Em seguida, será solicitado que seja inserido uma senha para proteger o arquivo da chave privada.
A senha que se escolher é crucial para a segurança da chave privada. Sem essa senha, não será possível descriptografar o arquivo da chave privada, o que protege a chave contra acessos não autorizados, mesmo que alguém tenha acesso ao arquivo `chave-privada.key`.
```zsh
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
```

Após inserir e confirmar a senha, o arquivo `chave-privada.key` será gerado.

- _Chave publica_
Para extrair a chave pública a partir de uma chave privada RSA. Aqui está a explicação de cada parte do comando:
Sempre deve-se vincular a um arquivo de chave privada

```bash
openssl rsa -in chave-privada.key -pubout -out chave-publica.key
```
_Explicação dos parâmetros_:
    `openssl rsa`: Esse comando é utilizado para processar chaves privadas RSA, permitindo que você extraia a __chave pública__ a partir de uma __chave privada__ existente, além de realizar outras operações com chaves RSA.
    `-in chave-privada.key`: O parâmetro `-in` especifica o arquivo de entrada que contém a chave privada. Neste caso, é `chave-privada.key`, que foi gerado anteriormente (com o comando `openssl genrsa`).
    `-pubout`: O parâmetro `-pubout` diz ao OpenSSL que se deseja extrair a chave pública da chave privada fornecida. Esse comando transforma a chave privada em sua respectiva chave pública, que pode ser compartilhada ou usada para criptografar dados.
    `-out chave-publica.key`: O parâmetro `-out` especifica o arquivo de saída onde a chave pública extraída será salva. Neste exemplo, a chave pública será salva no arquivo `chave-publica.key`.

_Resposta do comando_:
O OpenSSL solicitará a senha que se definiu ao criar a chave privada (caso tenha usado criptografia como AES-256). A senha é necessária para descriptografar a chave privada e extrair a chave pública.
```zsh
Enter pass phrase for chave-privada.key:
writing RSA key
```

Após fornecer a senha, a chave pública será extraída da chave privada e salva no arquivo `chave-publica.key`.
O arquivo `chave-publica.key` conterá a chave pública em formato `.PEM`, que pode ser usado para compartilhar com outros ou para realizar criptografia assimétrica, como a criptografia de mensagens que só podem ser descriptografadas com a chave privada correspondente.
Exemplo do conteúdo da chave pública:
Após o processo, o arquivo `chave-publica.key` terá um conteúdo semelhante a este:

```zsh 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7...
...resto da chave pública...
-----END PUBLIC KEY-----
```


### Para visualizar o conteúdo de um arquivo
Sintaxe:
openssl [algoritmo de criptografia] [comando para informar que será passado um arquivo] [nome do arquivo de entrada] [comando para informar que a saida deverá ser em modo texto] [comando para informar que não haverá arquivo de saida]
Para exibir o conteúdo da chave privada RSA em formato legível, sem gerar qualquer saída de chave no formato PEM:
```zsh
openssl rsa -in chave-privada.key -text -noout
```
_Explicação dos parâmetros_ :
    `openssl rsa`: Esse comando é usado para processar chaves privadas RSA.
    `-in chave-privada.key`: O parâmetro `-in` especifica o arquivo que contém a chave privada RSA. Neste caso, o arquivo `chave-privada.key` é a chave privada gerada previamente.
    `-text`: Esse parâmetro faz com que o OpenSSL imprima a chave privada em um formato de texto legível (human-readable), mostrando seus componentes internos, como o expoente público, os coeficientes e outros detalhes matemáticos da chave RSA.
    `-noout`: O parâmetro `-noout` impede que a chave privada seja impressa em formato PEM (o formato padrão codificado em Base64). Isso evita a impressão da chave PEM completa no terminal e mantém apenas as informações legíveis.

_Resposta do comando_:
O OpenSSL solicitará a senha (se a chave privada foi criptografada com uma senha, como no exemplo com AES-256), e depois mostrará as informações sobre a chave privada no terminal. Entre os detalhes exibidos, temos:

`Modulus (modulus)`: O módulo RSA, que é o número chave na criptografia RSA. É o produto de dois grandes números primos gerados durante a criação da chave privada.
`Public exponent (publicExponent)`: O expoente público, normalmente é um valor pequeno como 65537. Este é o valor usado na parte pública do processo de criptografia RSA.
`Private exponent (privateExponent)`: O expoente privado, que é o inverso modular do expoente público com relação ao módulo. Ele é parte crucial da chave privada.
`Prime1 e Prime2`: São os dois números primos gerados ao criar a chave RSA. O módulo é o produto desses dois números.
`Exponent1 e Exponent2`: São expoentes calculados a partir dos números primos, usados para acelerar a criptografia/descriptografia RSA.
`Coefficient (coefficient)`: Também conhecido como "fator CRT" (Chinese Remainder Theorem), usado para acelerar as operações RSA.

Essas informações são matematicamente usadas na geração da chave privada e no processo de criptografia RSA.

Exemplo de saída:
A saída típica do comando seria algo assim (simplificado):

```zsh
Private-Key: (4096 bit)
modulus:
    00:b8:ab:34:4f:b3:c8:5e:c7...
publicExponent: 65537 (0x10001)
privateExponent:
    00:92:36:f8:22:8e:8a:32:5b...
prime1:
    00:ed:cc:24:22:a8:e5:ef:b6...
prime2:
    00:ce:fd:8a:97:8e:54:3a:b6...
exponent1:
    00:9c:ed:1b:af:c9:67:de:25...
exponent2:
    00:ac:6e:29:1c:87:fc:47:ef...
coefficient:
    00:97:ee:12:f7:89:35:3c:9d...
```
_Resumo_:
O comando é útil para visualizar os detalhes internos da chave privada RSA em um formato legível, sem exibir a chave completa em formato PEM.

## Criptografar um arquivo existente com uma senha.
Para criptografar um arquivo de texto usando o algoritmo de criptografia AES com uma chave de 256 bits. Aqui está uma explicação detalhada dos parâmetros e do funcionamento desse comando:
```zsh
openssl enc -aes256 -in test.txt -out test_criptografado.enc
```
_Explicação dos parâmetros_:
    `openssl enc`: O subcomando `enc` é específico para operações de codificação (encrypt).
    `-aes256`: Este parâmetro especifica o algoritmo de criptografia a ser utilizado. Neste caso, aes256 refere-se ao AES (Advanced Encryption Standard) com uma chave de 256 bits. Isso significa que a criptografia será feita utilizando 256 bits de chave, o que proporciona um alto nível de segurança.
    `-in test.txt`: O parâmetro `-in` especifica o arquivo de entrada que será criptografado. Aqui, `test.txt` é o arquivo que contém os dados em texto simples.
    `-out test_criptografado.enc`: O parâmetro `-out` especifica o arquivo de saída que conterá os dados criptografados. Neste caso, `test_criptografado.enc` é o arquivo que armazenará o resultado da criptografia.
Como funciona o comando:
Quando você executa o comando, o OpenSSL irá solicitar que você insira uma senha (passphrase). Esta senha será usada para derivar a chave de criptografia. A segurança da criptografia depende fortemente da força dessa senha.
Após inserir a senha, o OpenSSL criptografa o conteúdo de `test.txt` usando o algoritmo AES de 256 bits e a senha fornecida, e o resultado é salvo no arquivo `test_criptografado.enc`.
Exemplo de uso:
Para criptografar o arquivo, você pode usar o seguinte comando no terminal:

```zsh
openssl enc -aes256 -in test.txt -out test_criptografado.enc
```
Após a execução, você verá um prompt solicitando a senha:

```zsh 
enter aes-256-cbc encryption password:
```
Depois de inserir a senha e confirmar, o arquivo `test_criptografado.enc` será criado e conterá os dados criptografados.

_Descriptografar_
 Para descriptografar o arquivo, você pode usar o comando:
```zsh 
openssl enc -d -aes256 -in test_criptografado.enc -out test_decriptografado.txt
```
`-d` indica que você está realizando a operação de descriptografia.

__Segurança__: Lembre-se de que a segurança da criptografia depende da força da senha utilizada. É recomendado usar senhas longas e complexas.

_Formatos de saída_: O arquivo de saída será um arquivo binário e pode não ser legível. Para visualizar ou manipular os dados, você deve descriptografá-los primeiro.
Esse comando é bastante útil para proteger dados sensíveis, garantindo que apenas pessoas com a senha correta possam acessar o conteúdo original.

## Criar um Pedido de Assinatura de Certificado (CSR)
Com a chave privada gerada, pode-se criar um CSR com o comando:

```zsh 
openssl req -new -key chaveprivada.pem -out pedido.csr
```
`req`: Indica que você está gerando um pedido de assinatura de certificado.
`-new`: Especifica que você está criando um novo CSR.
`-key chaveprivada.pem`: Especifica a chave privada que será usada para assinar o CSR.
`-out pedido.csr`: Define o nome do arquivo de saída para o CSR.

> Durante esse processo, você será solicitado a fornecer informações como país, estado, cidade, nome da organização, etc.

- Criar um Certificado Autoassinado
Após gerar o CSR, você pode criar um certificado autoassinado com o seguinte comando:

``` zsh 
openssl x509 -req -in pedido.csr -signkey chaveprivada.pem -out certificado.pem -days 365
```
`x509`: Indica que você está gerando um certificado no formato X.509.
`-req`: Indica que você está usando um CSR como entrada.
`-in pedido.csr`: Especifica o arquivo CSR que você criou.
`-signkey chaveprivada.pem`: Especifica a chave privada que será usada para assinar o certificado.
`-out certificado.pem`: Define o nome do arquivo de saída para o certificado.
`-days 365`: Especifica o número de dias que o certificado será válido.

- Verificar o Certificado
Você pode verificar o conteúdo do certificado gerado com o seguinte comando:

```zsh
openssl x509 -in certificado.pem -text -noout
```

`-text`: Mostra a saída em formato legível por humanos.
`-noout`: Evita a saída da versão codificada do certificado.

- _Resumo_
Agora você terá os seguintes arquivos:

`chaveprivada.pem`: Sua chave privada.
`pedido.csr`: O pedido de assinatura de certificado.
`certificado.pem`: O certificado autoassinado.

Esses passos devem ajudá-lo a gerar certificados usando o OpenSSL em um MacBook ou em qualquer sistema onde o OpenSSL esteja instalado.



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Artigo original: OpenSSL command cheatsheet
https://www.freecodecamp.org/portuguese/news/dicas-de-comandos-do-openssl/

Quando se trata de tarefas relacionadas à segurança, como gerar chaves, CSRs, certificados, calcular resumos (digests), depurar conexões TLS e outras tarefas relacionadas a PKI e HTTPS, você provavelmente acabaria usando a ferramenta OpenSSL.

O OpenSSL inclui milhares de recursos que cobrem uma ampla variedade de casos de uso, sendo difícil lembrar de sua sintaxe para todos eles e muito fácil de se perder. As páginas man não são tão úteis aqui. Muitas vezes, apenas procuramos no Google "openssl how to [caso de uso aqui]" ou procuramos algum tipo de "openssl cheatsheet" para relembrar o uso de um comando e ver exemplos.

Este artigo é minha coleção pessoal de trechos e exemplos de comandos do OpenSSL, agrupados por caso de uso.

Casos de uso
Aqui está a lista dos casos de uso dos quais eu vou tratar:

Trabalhando com chaves RSA e ECDSA
Criar solicitações de assinatura de certificados (CSR)
Criar certificados X.509
Verificar CSRs ou certificados
Calcular resumos de mensagens e codificação base64
Cliente TLS para conectar a um servidor remoto
Medir o tempo da conexão TLS e da negociação
Conversão entre formatos de codificação (PEM, DER) e recipientes (PKCS12, PKCS7)
Listar conjuntos de cifras
Verificar manualmente o estado de revogação de certificados a partir do respondedor OCSP
Certamente, esta não é uma lista completa, mas abrange os casos de uso mais comuns e inclui aqueles com os quais tenho trabalhado. Por exemplo, eu pulo a criptografia e a descriptografia ou uso openssl para gerenciamento de CA. O openssl é como um universo. Você nunca sabe onde termina.

Trabalhando com chaves RSA e ECDSA
Nos comandos abaixo, substitua [bits] com o tamanho da chave (Por exemplo, 2048, 4096, 8192).

Gerar uma chave RSA:
openssl genrsa -out example.key [bits]

Exibir apenas a chave pública ou modulus:
openssl rsa -in example.key -pubout
openssl rsa -in example.key -noout -modulus

Exibir a representação textual da chave RSA:
openssl rsa -in example.key -text -noout

Gerar uma nova chave RSA e criptografá-la com uma senha baseada na criptografia AES CBC 256:
openssl genrsa -aes256 -out example.key [bits]

Verificar sua chave privada. Se a chave tem uma senha, você será solicitado a informá-la:
openssl rsa -check -in example.key

Remover a senha da chave:
openssl rsa -in example.key -out example.key

Criptografar a chave privada com a senha:
openssl rsa -des3 -in example.key -out example_with_pass.key

Gerar a chave ECDSA. curve deve ser substituído por: prime256v1, secp384r1, secp521r1 ou outra curva elíptica suportada:
openssl ecparam -genkey -name [curve] | openssl ec -out example.ec.key

Exibir a representação textual da chave ECDSA:
openssl ec -in example.ec.key -text -noout

Listar as curvas EC disponíveis às quais a biblioteca OpenSSL oferece suporte:
openssl ecparam -list_curves

Gerar os parâmetros de DH com um comprimento dado:
openssl dhparam -out dhparams.pem [bits]

Criar solicitações de assinatura de certificados (CSR)
Nos comandos abaixo, substitua [digest] com o nome da função de hash suportada: md5, sha1, sha224, sha256, sha384 ou sha512 etc. É melhor evitar funções fracas, como md5 e sha1, e se ater a sha256 ou superior.

Criar uma CSR a partir da chave privada.
openssl req -new -key example.key -out example.csr -[digest]

Criar uma CSR e uma chave privada sem uma senha em um único comando:
openssl req -nodes -newkey rsa:[bits] -keyout example.key -out example.csr

Fornecer informações do assunto da CSR em uma linha de comando, em vez de um prompt interativo.
openssl req -nodes -newkey rsa:[bits] -keyout example.key -out example.csr -subj "/C=UA/ST=Kharkov/L=Kharkov/O=Super Secure Company/OU=IT Department/CN=example.com"

Criar uma CSR a partir do certificado e chave privada existentes:
openssl x509 -x509toreq -in cert.pem -out example.csr -signkey example.key

Gerar uma CSR para certificado SAN multidomínio fornecendo um arquivo de configuração openssl:
openssl req -new -key example.key -out example.csr -config req.conf

sendo req.conf:

[req]prompt=nodefault_md = sha256distinguished_name = dnreq_extensions = req_ext
[dn]CN=example.com
[req_ext]subjectAltName=@alt_names
[alt_names]DNS.1=example.comDNS.2=www.example.comDNS.3=ftp.example.com
Criar certificados X.509
Criar um certificado autoassinado e nova chave privada do zero:
openssl req -nodes -newkey rsa:2048 -keyout example.key -out example.crt -x509 -days 365

Criar um certificado autoassinado usando CSR e chave privada existentes:
openssl x509 -req -in example.csr -signkey example.key -out example.crt -days 365

Assinar certificado filho usando o certificado de sua autoridade certificadora ou AC ("CA", em inglês) e sua chave privada. Se você fosse uma AC, este é um exemplo bem básico de como você poderia emitir novos certificados.
openssl x509 -req -in child.csr -days 365 -CA ca.crt -CAkey ca.key -set_serial 01 -out child.crt

Exibir a representação textual do certificado
openssl x509 -in example.crt -text -noout

Exibir a impressão digital (fingerprint) do certificado como resumo md5, sha1, sha256:
openssl x509 -in cert.pem -fingerprint -sha256 -noout

Verificar CSRs ou certificados
Verificar uma assinatura de CSR:
openssl req -in example.csr -verify

Verificar se a chave privada corresponde a um certificado e uma CSR:
openssl rsa -noout -modulus -in example.key | openssl sha256
openssl x509 -noout -modulus -in example.crt | openssl sha256
openssl req -noout -modulus -in example.csr | openssl sha256

Verificar o certificado, presumindo que você tenha o certificado raiz e quaisquer outros intermediários configurados como confiáveis em sua máquina:
openssl verify example.crt

Verificar o certificado, quando você tem a cadeia de certificação intermediária. O certificado raiz não é parte do pacote, devendo ser configurado como um confiável em sua máquina.
openssl verify -untrusted intermediate-ca-chain.pem example.crt

Verificar o certificado, quando você tem a cadeia de certificação intermediária e o certificado raiz, o qual não está configurado como confiável.
openssl verify -CAFile root.crt -untrusted intermediate-ca-chain.pem child.crt

Verificar se o certificado servido por um servidor remoto cobre o nome de máquina dado. Isso é útil para verificar se seu certificado multidomínio cobre adequadamente todos os nomes de máquina.
openssl s_client -verify_hostname www.example.com -connect example.com:443

Calcular resumos de mensagens e codificação base64
Calcular resumos md5, sha1, sha256, sha384, sha512:
openssl dgst -[hash_function] <input.file>
cat input.file | openssl [hash_function]

Codificação e decodificação de Base64:
cat /dev/urandom | head -c 50 | openssl base64 | openssl base64 -d

Cliente TLS para conectar a um servidor remoto
Conectar a um servidor que ofereça suporte a TLS:
openssl s_client -connect example.com:443
openssl s_client -host example.com -port 443

Conectar a um servidor e mostrar a cadeia de certificação completa:
openssl s_client -showcerts -host example.com -port 443 </dev/null

Extrair o certificado:
openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certificate.pem

Substituir  a extensão SNI (Indicação de Nome do Servidor ou Server Name Indication, em inglês) com outro nome de servidor. Isso é útil para testar quando vários sites seguros estão hospedados no mesmo endereço IP:
openssl s_client -servername www.example.com -host example.com -port 443

Testar a conexão TLS usando de forma forçada um conjunto específico de cifras como, por exemplo, ECDHE-RSA-AES128-GCM-SHA256. Isso é útil para verificar se um servidor pode conversar adequadamente por meio de conjuntos de cifras configurados diferentes, em vez daqueles que ele prefere.
openssl s_client -host example.com -port 443 -cipher ECDHE-RSA-AES128-GCM-SHA256 2>&1 </dev/null

Medir o tempo da conexão TLS e da negociação
Medir o tempo de conexão SSL sem/com reuso de sessão:
openssl s_time -connect example.com:443 -new
openssl s_time -connect example.com:443 -reuse

Examinar aproximadamente os tempos de handshake TCP e SSL usando o curl:
curl -kso /dev/null -w "tcp:%{time_connect}, ssldone:%{time_appconnect}\n" https://example.com

Medir a velocidade de vários algoritmos de segurança:
openssl speed rsa2048
openssl speed ecdsap256

Conversão entre formatos de codificação (PEM, DER) e recipientes
Converter um certificado entre formatos DER e PEM:
openssl x509 -in example.pem -outform der -out example.der
openssl x509 -in example.der -inform der -out example.pem

Combinar vários certificados em um arquivo PKCS7 (P7B):
openssl crl2pkcs7 -nocrl -certfile child.crt -certfile ca.crt -out example.p7b

Converter do PKCS7 de volta para PEM. Se o arquivo PKCS7 tiver vários certificados, o arquivo PEM vai conter todos os itens nele.
openssl pkcs7 -in example.p7b -print_certs -out example.crt

Combinar um arquivo de certificado PEM e uma chave privada no PKCS#12 (.pfx .p12). Você também pode adicionar uma cadeia de certificados ao arquivo PKCS12.
openssl pkcs12 -export -out certificate.pfx -inkey privkey.pem -in certificate.pem -certfile ca-chain.pem

Converter um arquivo PKCS#12 (.pfx .p12) contendo uma chave privada e certificados de volta no PEM:
openssl pkcs12 -in keystore.pfx -out keystore.pem -nodes

Listar conjuntos de cifras
Listar os conjuntos de cifras TLS disponíveis aos quais o cliente openssl oferece suporte:
openssl ciphers -v

Enumerar todos os conjuntos de cifras individuais, que são descritos por uma string de lista de cifras OpenSSL abreviada. Isso é útil quando você está configurando o servidor (como o Nginx) e precisa testar sua string ssl_ciphers.
openssl ciphers -v 'EECDH+ECDSA+AESGCM:EECDH+aRSA+SHA256:EECDH:DHE+AESGCM:DHE:!RSA!aNULL:!eNULL:!LOW:!RC4'

Verificar manualmente o estado de revogação de certificados a partir do respondedor OCSP
Este é um processo com vários passos:

Obter o certificado de um servidor remoto
Obter a cadeia de certificação AC intermediária
Ler o URI do endpoint OCSP do certificado
Solicitar a um respondedor OCSP remoto que informe o estado de revogação do certificado
Primeiramente, obtenha o certificado de um servidor remoto:
openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > cert.pem

Você também precisa obter a cadeia de certificação AC intermediária. Use o sinalizador -showcerts para mostrar a cadeia de certificação completa e salvar manualmente todos os certificados intermediárias no arquivo chain.pem:
openssl s_client -showcerts -host example.com -port 443 </dev/null

Leia o URI do endpoint OCSP a partir do certificado:
openssl x509 -in cert.pem -noout -ocsp_uri

Solicite um respondedor OCSP remoto para o estado de revogação do certificado usando o URI da etapa acima (por exemplo, http://ocsp.stg-int-x1.letsencrypt.org).
openssl ocsp -header "Host" "ocsp.stg-int-x1.letsencrypt.org" -issuer chain.pem -VAfile chain.pem -cert cert.pem -text -url http://ocsp.stg-int-x1.letsencrypt.org

Recursos
Reuni alguns recursos sobre OpenSSL que você pode achar úteis (em inglês).

OpenSSL Essentials: Working with SSL Certificates, Private Keys and CSRs | DigitalOcean — https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs

The Most Common OpenSSL Commands — https://www.sslshopper.com/article-most-common-openssl-commands.html

OpenSSL: Working with SSL Certificates, Private Keys and CSRs — https://www.dynacont.net/documentation/linux/openssl/


