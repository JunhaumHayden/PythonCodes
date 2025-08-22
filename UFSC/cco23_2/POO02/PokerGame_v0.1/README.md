# PythonCodes
Codes in Python



<h1 align="center"> Poker Game in Python </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Description

Português-Br

<h2 align = "center"> Sumário </h>

Itens a serem analisados


- Modelagem UML (diagrama de classes, com atributos, metodos, cardinalidade)

- Utilização de conceitos de Orientação a Objetos
Indiquem quais conceitos da POO foram utilizados (herança, polimorfismo, Composição, Agregação)

- Utilização de Coleções (listas, dicionários)

- Funcionamento do Sistema


<h2 align="center"> Modelo Conceitual: </h2>

É um sistema simples de simulação de um jogo de pôquer para pessoas que querem aprender a jogar.
Aqui estão os componentes básicos:

1. **Jogadores:**
   - Os jogadores podem ser representados por nomes ou números.

2. **Baralho:**
   - Um baralho de 52 cartas é usado.

3. **Mãos de Pôquer:**
   - Cada jogador recebe uma mão de pôquer com um número limitado de cartas (por exemplo, 5 cartas).

4. **Regras Básicas:**
   - O jogo segue as regras básicas do pôquer, como ranking de mãos (par, trinca, flush, etc.).
   - Os jogadores podem realizar ações de "Apostar" ou "Desistir".

5. **Vencedor:**
   - O sistema determina o vencedor com base na melhor mão de pôquer.

6. **Simples e Instrutivo:**
   - O sistema fornece informações sobre as regras à medida que o jogo avança, ajudando os jogadores a aprender.

7. **Interativo:**
   - Os jogadores podem interagir com o sistema para tomar decisões.

8. **Recursos Educacionais:**
   - O sistema pode incluir recursos educacionais, como explicações sobre as regras e o ranking de mãos.

9. **Níveis de Dificuldade:**
   - Os jogadores podem escolher níveis de dificuldade para ajustar a experiência de aprendizado.

10. **Feedback:**
   - O sistema fornece feedback sobre as ações dos jogadores, explicando o resultado das rodadas.

Essa versão simplificada do sistema de jogo de pôquer é voltada para jogadores iniciantes que desejam aprender as regras básicas e a estratégia do jogo. O foco é na educação e na experiência interativa. Você pode adicionar recursos adicionais, como tutoriais interativos e dicas estratégicas, para melhorar ainda mais a experiência de aprendizado.








<h2 align="center"> Esboço de um Diagrama de Classe: </h2>

+-----------------------------+         +----------------+
|    Jogador                  |         |     Carta      |
+-----------------------------+         +----------------+
| -Nome : String              |         | -Valor : String|
| -Fichas : Int               |         | -Naipe : String|
| -Mão : Lista<Carta>         |         +----------------+
| +Apostar(valor: Int) : Void |
| +Desistir() : Void          |
+-----------------------------+        
          |
          |
          v
+------------------------------+
|     Baralho                  |
+------------------------------+
| -Cartas : Lista<Carta>       |
| +Embaralhar() : Void         |
| +Distribuir() : Lista<Carta> |
+------------------------------+
