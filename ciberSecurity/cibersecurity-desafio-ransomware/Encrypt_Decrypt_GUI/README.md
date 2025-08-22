<div align="center">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Logo Python" width="110">
</div>

## 


<h1 align="center"> Encrypt and Decrypt Files </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>


## Description

![Static Badge](https://img.shields.io/badge/STATUS-Em_Conclu%C3%ADdo-green)

![Static Badge](https://img.shields.io/badge/Powered_by-Python-green) ![Static Badge](https://img.shields.io/badge/Powered_by-Tkinter-A9A9A9) 

![Static Badge](https://img.shields.io/badge/Hash-red) ![Static Badge](https://img.shields.io/badge/AES-blue) 



# Encrypt/Decrypt System

Este repositório contém uma aplicação Python com interface gráfica desenvolvida com `Tkinter`, que permite criptografar e descriptografar arquivos de texto. Além disso, gera e valida códigos hash para verificar a integridade dos arquivos.

## ⚙️ Funcionalidades

1. **Criptografia de Arquivos**
   - Criptografa o conteúdo fornecido pelo usuário.
   - Salva o arquivo criptografado no sistema.
   - Gera um código hash SHA-256 do conteúdo criptografado e o armazena em um arquivo `hash_code.txt`.

2. **Descriptografia de Arquivos**
   - Descriptografa um arquivo previamente criptografado.
   - Verifica se o código hash do arquivo corresponde ao código informado pelo usuário antes de descriptografar.

3. **Atualização do Código Hash**
   - Atualiza o código hash de um arquivo criptografado existente.

4. **Carregar Conteúdo de Arquivos**
   - Lê o conteúdo de um arquivo de texto e exibe na interface.

## 🖥️ Interface Gráfica

A aplicação possui uma interface intuitiva com os seguintes componentes:
- **Campo de entrada para o nome do arquivo:** Permite especificar o arquivo para operação. Por padrão, utiliza `texto.txt`.
- **Área de texto para conteúdo:** Permite ao usuário visualizar ou editar o conteúdo do arquivo.
- **Campo para código hash:** Exibe ou recebe o código hash para validação.
- **Botões para executar operações:** Como carregar conteúdo, criptografar, descriptografar e atualizar o código hash.

## 📥 Entradas

1. **Arquivo:**
   - Nome do arquivo a ser manipulado. O padrão é `texto.txt`.

2. **Conteúdo:**
   - Texto que será criptografado ou descriptografado.

3. **Hash Code:**
   - Código hash SHA-256 usado para verificar a integridade do arquivo durante a descriptografia.

## 📤 Comportamento Esperado

1. **Criptografia (`Encrypt`):**
   - Se o campo de conteúdo estiver vazio, uma mensagem de erro será exibida.
   - Gera um arquivo criptografado no formato binário.
   - Gera um arquivo `hash_code.txt` contendo o hash do conteúdo criptografado.

2. **Descriptografia (`Decrypt`):**
   - Se o hash informado não corresponder ao hash do arquivo, a descriptografia será abortada.
   - O conteúdo original será exibido na área de texto e salvo no arquivo especificado.

3. **Atualização de Hash (`Update Hash Code`):**
   - Gera e exibe o hash do conteúdo do arquivo criptografado.

4. **Carregar Conteúdo (`Load File Content`):**
   - Exibe o conteúdo do arquivo no campo de texto, se o arquivo existir.

## 📋 Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas no ambiente:
- **Python 3.6+**
- **Bibliotecas:**
  - `cryptography`
  - `tkinter`

Instale as dependências com o comando:
```bash
pip install cryptography
```

## 🚀 Como Executar

Clone o repositório:
```bash
git clone https://github.com/seu-usuario/encrypt-decrypt-system.git
cd encrypt-decrypt-system
```
Execute o script:
```bash
python main.py
```

## 🛠️ Personalizações

- Chave de criptografia: Atualmente, a chave é gerada automaticamente a cada execução. Para reutilizar a mesma chave, salve-a em um arquivo ou variável persistente.

## Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e sugestões.

# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |