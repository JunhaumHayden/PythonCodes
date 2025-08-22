
# 2 avaliação POO 02

Aluno: Carlos Benedito Hayden de Albuquerque Junior
INE5404-02208A (20232)


Desenvolva um aplicativo de noticias.

Requisitos

1. Deverá ter um login (user e senha) para acessar o sistema

2. A tela principal deverá apresentar um filtro de notícias com;

Data Início e Data Fim;

Assunto,

Categoria: pode aceitar noticias de esportes, economia e política.

Campo com a notícia (texto)

1. Orientação á objetos, o código deverá ser organizado em classes, utilização de herança e composição (2 pontos)

2. Utilização de Arquivos para armazenamento das noticias (utilização de API de notícias ganhará um ponto extra) (2 pontos)

3. Utilização de Listas ou dicionários (1 ponto)

4. Utilização de Interface Gráfica (2 pontos)

5. Atendimento aos requisitos (3 pontos)

A interface gráfica deve ser em Tkinter e a a API de notícias de livre escolha.



<h1 align="center"> App Noticias </h1>




# Description

Para realizar login exitem 3 usuarios.
- login: user1 senha: senha
- login: user2 senha: senha
- login: admin senha: senha



**STEP01 install Python framework**


***Foram utilizado as bibliotecas:***
- Tkinter
- TTk
- Pandas
- JSON

***Foi utilizado a API GoolgeNews***
Instalaçao atraves do comando:
        pip install --upgrade GoogleNews

Materias de consulta:
  https://pypi.org/project/GoogleNews/



**STEP02 Modo de uso**

É uma interface simples, com o objetivo de utilizar programação orientada a objetos para construir um aplicativo utilizando uma API de terceiros.

***Primeira tela realiza-se o login***
    Os usuarios estão armazenados em um arquivo no formato JSON que é consultado ao realizar o login.
    Caso o login não seja autenticado retorna uma mensagem de erro.
    Caso login seja autenticado inicia a tela de consulta das noticias.
***Segunda tela realiza as consultas das noticias***
    As consultas são realizadas entrando com os dados nos campos e clicando no botão Buscar Noticias.
    Há um campo para postar noticias que são armazenadas em um arquivo no formato JSON.









# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |
