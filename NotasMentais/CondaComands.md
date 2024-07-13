https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

### Comandos de Ambiente
1. Criar um novo ambiente:

```sh
conda create --name meuoambiente
```

```sh
python -m venv .meuoambiente
```
Você pode especificar a versão do Python ou outros pacotes na criação:

```sh
conda create --name meuoambiente python=3.8
```
Ativar um ambiente:

```sh
conda activate meuoambiente
```
Desativar o ambiente atual:

```sh
conda deactivate
```
Listar todos os ambientes:

```sh
conda env list
```
Excluir um ambiente:

```sh
conda remove --name meuoambiente --all
```
### Comandos de Pacotes
1. Instalar um pacote:

```sh
conda install nome_do_pacote
```
Instalar uma versão específica de um pacote:

```sh
conda install nome_do_pacote=2.1.0
```
Atualizar um pacote:

```sh
conda update nome_do_pacote
```
Remover um pacote:

```sh
conda remove nome_do_pacote
```
Listar todos os pacotes no ambiente atual:

```sh
conda list
```
### Comandos de Gestão do Conda
1 . Atualizar o Conda:

```sh
conda update conda
```
Mostrar informações sobre o Conda:

```sh
conda info
```
Mostrar informações sobre um pacote específico:

```sh
conda info nome_do_pacote
```
### Exemplos de Uso
1. Criar um ambiente com um nome específico e uma versão do Python:

```sh
conda create --name data_analysis python=3.9
```
2. Instalar o pacote NumPy em um ambiente ativado:

```sh
conda activate data_analysis
conda install numpy
``` 
3. Atualizar todos os pacotes em um ambiente:

```sh
conda update --all
```
