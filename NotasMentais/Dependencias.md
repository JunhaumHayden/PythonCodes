# Requirements Files

Para criar um arquivo com as dependências do projeto em Python, você pode usar um arquivo `requirements.txt`. Esse arquivo lista todos os pacotes e suas versões que o projeto necessita para ser executado corretamente.

#### Passos para criar o arquivo `requirements.txt`
1. Instalar e Gerenciar Pacotes com pip: Primeiro, certifique-se de que você tenha todos os pacotes necessários instalados no seu ambiente de desenvolvimento.

2. Criar o Arquivo `requirements.txt`: Use o comando `pip freeze` para listar todas as dependências do seu ambiente de desenvolvimento e redirecionar essa lista para um arquivo `requirements.txt`.

#### Passo a Passo
__Passo 1__: Certifique-se de que todos os pacotes necessários estão instalados

Se o seu projeto precisa do pacote re (embora seja um módulo padrão do Python e não precise ser instalado) e regex, além de outros pacotes comuns como requests, por exemplo, você precisa instalar todos os pacotes necessários. Suponhamos que você precise dos pacotes requests e regex:

```bash
pip install requests
pip install regex
```
__Passo 2__: Gerar o arquivo requirements.txt

No terminal, dentro do diretório do seu projeto, execute o seguinte comando:

``` bash
pip freeze > requirements.txt
```
Isso criará um arquivo `requirements.txt` com todas as dependências do projeto e suas versões.

Exemplo de um Arquivo `requirements.txt`

``` plaintext
requests==2.26.0
regex==2021.8.3
```

#### Instruções Adicionais para o Usuário
__Como Instalar as Dependências__: Quando outro desenvolvedor ou você mesmo em outro ambiente precisar instalar as dependências do projeto, basta executar:

```bash
pip install -r requirements.txt
```
#### Implementação no Seu Projeto
1. Crie e edite o arquivo `requirements.txt` com as dependências listadas.

2. Use o seguinte comando para instalar todas as dependências do arquivo requirements.txt quando necessário:

```bash
pip install -r requirements.txt
```
#### Exemplo do Processo Completo
Vamos considerar que o seu projeto precisa do módulo re (embora ele seja nativo do Python e não precise ser instalado) e de um módulo adicional como requests. Veja como ficaria:

__Código Python para Validação de Número de Telefone__

```python

import re

def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    if re.match(pattern, phone_number):  
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

phone_number = input("Insira o número de telefone: ")
result = validate_numero_telefone(phone_number)
print(result)
```
#### Criação do Arquivo requirements.txt

```bash
pip freeze > requirements.txt
```
#### Conteúdo do Arquivo requirements.txt

```plaintext
Copy code
requests==2.26.0
regex==2021.8.3
```
#### Instalação das Dependências

Para instalar as dependências listadas no arquivo requirements.txt, use:

```bash
pip install -r requirements.txt
```

#### Finalizando
Com isso, você garante que qualquer pessoa (ou outro ambiente de desenvolvimento) que precise rodar seu projeto tenha todas as dependências corretas e versões especificadas, o que evita incompatibilidades e erros de execução.

“[Requirements files](https://pip.pypa.io/en/latest/user_guide/#requirements-files)” are files containing a list of items to be installed using `pip install` like so:


Unix/macOS
```sh
python -m pip install -r requirements.txt
```

Details on the format of the files are here: Requirements File Format.

Logically, a Requirements file is just a list of pip install arguments placed in a file. Note that you should not rely on the items in the file being installed by pip in any particular order.

Requirements files can also be served via a URL, e.g. http://example.com/requirements.txt besides as local files, so that they can be stored and served in a centralized place.

In practice, there are 4 common uses of Requirements files:

1. Requirements files are used to hold the result from pip freeze for the purpose of achieving Repeatable Installs. In this case, your requirement file contains a pinned version of everything that was installed when pip freeze was run.

Unix/macOS
```sh
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

2. Requirements files are used to force pip to properly resolve dependencies. pip 20.2 and earlier doesn’t have true dependency resolution, but instead simply uses the first specification it finds for a project. E.g. if pkg1 requires pkg3>=1.0 and pkg2 requires pkg3>=1.0,<=2.0, and if pkg1 is resolved first, pip will only use pkg3>=1.0, and could easily end up installing a version of pkg3 that conflicts with the needs of pkg2. To solve this problem, you can place pkg3>=1.0,<=2.0 (i.e. the correct specification) into your requirements file directly along with the other top level requirements. Like so:
```sh
 pkg1
 pkg2
 pkg3>=1.0,<=2.0
```
3. Requirements files are used to force pip to install an alternate version of a sub-dependency. For example, suppose ProjectA in your requirements file requires ProjectB, but the latest version (v1.3) has a bug, you can force pip to accept earlier versions like so:
``` sh
ProjectA
ProjectB<1.3
```
4. Requirements files are used to override a dependency with a local patch that lives in version control. For example, suppose a dependency SomeDependency from PyPI has a bug, and you can’t wait for an upstream fix. You could clone/copy the src, make the fix, and place it in VCS with the tag sometag. You’d reference it in your requirements file with a line like so:
```sh
git+https://myvcs.com/some_dependency@sometag#egg=SomeDependency
```
If _SomeDependency_ was previously a top-level requirement in your requirements file, then replace that line with the new line. If _SomeDependency_ is a sub-dependency, then add the new line.

It’s important to be clear that pip determines package dependencies using install_requires metadata, not by discovering `requirements.txt` files embedded in projects.

## Especificar dependências no Python

#### [Artigo Google](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python?hl=pt-br)

Há duas maneiras de especificar dependências para o Cloud Functions gravadas no Python: com o uso do arquivo `requirements.txt` do gerenciador de pacotes `pip` ou o com o empacotamento de dependências locais com a função.

A especificação de dependência que usa o padrão Pipfile/Pipfile.lock não é compatível. Seu projeto não deve incluir esses arquivos.

### Como especificar dependências com `pip`

Dependências no Python são gerenciadas com `pip` e expressas em um arquivo de metadados chamado `requirements.txt`. 
> ⚠️ O arquivo precisa estar no mesmo diretório que o arquivo `main.py` que contém o código da função.

Quando você implanta ou reimplanta a função, o Cloud Functions usa o pip para fazer o download e instalar a versão mais recente das dependências, conforme declarado no arquivo `requirements.txt`. O arquivo `requirements.txt` contém uma linha por pacote. Cada linha contém o nome do pacote e, como opção, a versão solicitada. Para mais detalhes, consulte a referência do `requirements.txt`.

Para evitar que seu build seja afetado por mudanças na versão de dependência, fixe os pacotes de dependência em uma versão específica.

A seguir, um exemplo de arquivo `requirements.txt`:

```python
functions-framework
requests==2.20.0
numpy
```

O Functions Framework é uma dependência necessária para todas as funções. Embora o Cloud Functions o instale em seu nome quando a função é criada, recomendamos que você a inclua como uma dependência explícita para maior clareza.

Se a função depende de dependências particulares, recomendamos que você espelhe functions-framework no registro particular. Inclua o functions-framework espelhado como uma dependência da sua função para evitar a instalação do pacote pela Internet pública.

### Como empacotar dependências locais

Também é possível empacotar e implantar dependências junto com sua função. Essa abordagem é útil se sua dependência não estiver disponível por meio do gerenciador de pacotes pip ou se o acesso à Internet do ambiente do Cloud Functions for restrito.

> ✪ Observação: ainda é possível usar um arquivo `requirements.txt` para especificar dependências complementares que não foram empacotadas com sua função.
Por exemplo, é possível usar uma estrutura de diretório como a seguinte:

```sh
myfunction/
├── main.py
└── localpackage/
    ├── __init__.py
    └── script.py
```

Você pode importar o código normalmente de localpackage usando a seguinte instrução import.


```python
# Code in main.py
from localpackage import script
````

Observe que essa abordagem não executará nenhum arquivo setup.py. Pacotes com esses arquivos ainda podem ser agrupados, mas podem não ser executados corretamente no Cloud Functions.