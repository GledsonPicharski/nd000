# Introduction to Programming Nanodegree (nd000) — Udacity

**[English](#english) · [Português](#português)**

---

## English

This repository contains the exercises and projects I built during Udacity's **Introduction to Programming Nanodegree**. The program covers programming fundamentals across three languages: HTML/CSS for the web, Python, and JavaScript.

### Repository structure

```
nd000/
├── licoes/      # exercises from the Python lessons
└── projetos/    # graded nanodegree projects
```

### Projects

| # | Project | Course | Technologies | Status |
|---|---------|--------|--------------|--------|
| 1 | [Animal Trading Cards](#1-animal-trading-cards) | Introduction to Web Development | HTML, CSS | Completed |
| 2 | [Adventure Game](#2-adventure-game) | Introduction to Programming with Python I | Python | Completed |
| 3 | [Rock Paper Scissors](#3-rock-paper-scissors) | Introduction to Programming with Python II | Python (OOP) | Completed |
| 4 | [Shopping Cart](#4-shopping-cart) | Introduction to JavaScript | JavaScript, Jest | Completed |

#### 1. Animal Trading Cards

📁 [`projetos/animal trading card/`](projetos/animal%20trading%20card/)

A web page styled as a trading card about a favorite animal, in this case a small dog.
It shows the animal's name, photo, a fun fact, a list of characteristics and a short description.

- **Technologies and concepts:** HTML page structure, semantic tags, lists, and CSS in a separate stylesheet.
- **How to run:** open `animal trading card.html` in a browser.

#### 2. Adventure Game

📁 [`projetos/new_adventure_game.py`](projetos/new_adventure_game.py)

A text-based adventure game in the terminal where the player chooses between a house and a cave to face a randomly chosen enemy.
Finding the Sword of Ogoroth in the cave is the key to winning, and the player can restart at the end.

- **Technologies and concepts:** Python, functions, conditionals, loops, input validation, the `random` module, and PEP 8 style checked with `pycodestyle`.
- **How to run:**

  ```bash
  python projetos/new_adventure_game.py
  ```

> `projetos/adventure_game.py` is the first version of the game, kept to show how the code evolved.

#### 3. Rock Paper Scissors

📁 [`projetos/rps.py`](projetos/rps.py)

Rock, paper, scissors in the terminal against a computer opponent, over as many rounds as the player chooses.
Each opponent is a class with its own strategy: always rock, random, reflecting the player's last move, or cycling through the moves.

- **Technologies and concepts:** Python, object-oriented programming (classes, inheritance, method overriding), separation of responsibilities, and input validation.
- **How to run:**

  ```bash
  python projetos/rps.py
  ```

#### 4. Shopping Cart

📁 [`projetos/Shopping Cart/`](projetos/Shopping%20Cart/)

The core logic of a shopping cart for a cash-only fruit stand: adding, increasing, decreasing and removing products, and calculating the total.
Checkout accepts payments in installments and reports the remaining balance or the change due. My work is in [`starter/src/assets/script.js`](projetos/Shopping%20Cart/starter/src/assets/script.js); the interface was provided by Udacity.

- **Technologies and concepts:** JavaScript, arrays, object literals, functions, variable scope, array methods (`find`, `forEach`, `splice`), and unit tests with Jest.
- **How to run** (requires [Node.js](https://nodejs.org)):

  ```bash
  cd "projetos/Shopping Cart/starter"
  npm install
  npm start    # opens the store at http://localhost:3000
  npm test     # runs the tests
  ```

### Program content

1. **Welcome and Orientation:** an introduction to the program, the instructors and the support channels.
2. **Introduction to Web Development:** how the web works, building pages with HTML and styling them with CSS. **Project:** Animal Trading Cards.
3. **Introduction to Programming with Python I:** first Python programs. **Project:** Adventure Game. The lesson exercises are in [`licoes/`](licoes/):

   | Lesson | Content | Folder |
   |--------|---------|--------|
   | Turtles and Code | Core programming concepts by drawing shapes with the `turtle` module | [`02-turtle`](licoes/02-turtle/) |
   | Python Functions | Functions, parameters and conditionals | [`03-python_funcions`](licoes/03-python_funcions/) |
   | Shell Workshop | Basic use of the Unix terminal | — |
   | Python at Home | Installing Python on your own computer | — |
   | Strings and Lists | Working with text and lists, including slicing | [`06-strings_and_lists`](licoes/06-strings_and_lists/) |
   | Style and Structure | Longer programs, code organization and PEP 8 style | [`07-style_and_structure`](licoes/07-style_and_structure/) |

4. **Introduction to Programming with Python II:** files, APIs and object-oriented programming. **Project:** Rock Paper Scissors.
5. **Introduction to JavaScript:** data types and variables, conditionals, loops, functions, arrays and objects. **Project:** Shopping Cart.
6. **Congratulations! What's next?:** program wrap-up and next steps.
7. **Git and GitHub (optional):** version control with Git, commit history, collaborating on GitHub and writing READMEs.

---

## Português

Este repositório reúne os exercícios e projetos que desenvolvi no **Introduction to Programming Nanodegree** da Udacity. O programa cobre os fundamentos da programação em três linguagens: HTML/CSS para a web, Python e JavaScript.

### Estrutura do repositório

```
nd000/
├── licoes/      # exercícios das aulas de Python
└── projetos/    # projetos avaliados do nanodegree
```

### Projetos

| # | Projeto | Curso | Tecnologias | Status |
|---|---------|-------|-------------|--------|
| 1 | [Animal Trading Cards](#1-animal-trading-cards-1) | Introduction to Web Development | HTML, CSS | Concluído |
| 2 | [Adventure Game](#2-adventure-game-1) | Introduction to Programming with Python I | Python | Concluído |
| 3 | [Rock Paper Scissors](#3-rock-paper-scissors-1) | Introduction to Programming with Python II | Python (POO) | Concluído |
| 4 | [Shopping Cart](#4-shopping-cart-1) | Introduction to JavaScript | JavaScript, Jest | Concluído |

#### 1. Animal Trading Cards

📁 [`projetos/animal trading card/`](projetos/animal%20trading%20card/)

Uma página web no formato de carta colecionável sobre um animal favorito, no caso um cachorro de pequeno porte.
A carta mostra o nome, a foto, uma curiosidade, uma lista de características e uma breve descrição do animal.

- **Tecnologias e conceitos:** estrutura de página HTML, tags semânticas, listas e CSS em arquivo separado.
- **Como executar:** abra `animal trading card.html` no navegador.

#### 2. Adventure Game

📁 [`projetos/new_adventure_game.py`](projetos/new_adventure_game.py)

Um jogo de aventura em texto no terminal, em que o jogador escolhe entre uma casa e uma caverna para enfrentar um inimigo sorteado.
Encontrar a Espada de Ogoroth na caverna é a chave para vencer, e ao final o jogador pode recomeçar.

- **Tecnologias e conceitos:** Python, funções, condicionais, loops, validação de entrada, o módulo `random` e estilo PEP 8 verificado com `pycodestyle`.
- **Como executar:**

  ```bash
  python projetos/new_adventure_game.py
  ```

> `projetos/adventure_game.py` é a primeira versão do jogo, mantida para mostrar a evolução do código.

#### 3. Rock Paper Scissors

📁 [`projetos/rps.py`](projetos/rps.py)

Pedra, papel e tesoura no terminal contra um adversário controlado pelo computador, com o número de rodadas escolhido pelo jogador.
Cada adversário é uma classe com estratégia própria: sempre pedra, aleatório, repetir a última jogada do jogador ou alternar entre as jogadas.

- **Tecnologias e conceitos:** Python, programação orientada a objetos (classes, herança, sobrescrita de métodos), separação de responsabilidades e validação de entrada.
- **Como executar:**

  ```bash
  python projetos/rps.py
  ```

#### 4. Shopping Cart

📁 [`projetos/Shopping Cart/`](projetos/Shopping%20Cart/)

A lógica de um carrinho de compras para uma banca de frutas que só aceita dinheiro: adicionar, aumentar, diminuir e remover produtos, além de calcular o total.
O pagamento aceita parcelas e informa o saldo restante ou o troco. A minha parte está em [`starter/src/assets/script.js`](projetos/Shopping%20Cart/starter/src/assets/script.js); a interface foi fornecida pela Udacity.

- **Tecnologias e conceitos:** JavaScript, arrays, objetos literais, funções, escopo de variáveis, métodos de array (`find`, `forEach`, `splice`) e testes unitários com Jest.
- **Como executar** (requer [Node.js](https://nodejs.org)):

  ```bash
  cd "projetos/Shopping Cart/starter"
  npm install
  npm start    # abre a loja em http://localhost:3000
  npm test     # roda os testes
  ```

### Conteúdo do programa

1. **Welcome and Orientation:** apresentação do programa, dos instrutores e dos canais de suporte.
2. **Introduction to Web Development:** como a web funciona, criação de páginas com HTML e estilização com CSS. **Projeto:** Animal Trading Cards.
3. **Introduction to Programming with Python I:** os primeiros programas em Python. **Projeto:** Adventure Game. Os exercícios das lições estão em [`licoes/`](licoes/):

   | Lição | Conteúdo | Pasta |
   |-------|----------|-------|
   | Turtles and Code | Conceitos básicos de programação desenhando formas com o módulo `turtle` | [`02-turtle`](licoes/02-turtle/) |
   | Python Functions | Funções, parâmetros e condicionais | [`03-python_funcions`](licoes/03-python_funcions/) |
   | Shell Workshop | Uso básico do terminal Unix | — |
   | Python at Home | Instalação do Python no computador | — |
   | Strings and Lists | Manipulação de textos e listas, incluindo fatiamento (*slicing*) | [`06-strings_and_lists`](licoes/06-strings_and_lists/) |
   | Style and Structure | Programas mais longos, organização do código e estilo PEP 8 | [`07-style_and_structure`](licoes/07-style_and_structure/) |

4. **Introduction to Programming with Python II:** arquivos, APIs e programação orientada a objetos. **Projeto:** Rock Paper Scissors.
5. **Introduction to JavaScript:** tipos de dados e variáveis, condicionais, loops, funções, arrays e objetos. **Projeto:** Shopping Cart.
6. **Congratulations! What's next?:** encerramento do programa e próximos passos.
7. **Git and GitHub (opcional):** controle de versão com Git, histórico de commits, colaboração no GitHub e escrita de READMEs.
