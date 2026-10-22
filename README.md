# Introduction to Programming Nanodegree (nd000) — Udacity

This repository contains the exercises and projects I built during Udacity's **Introduction to Programming Nanodegree**. The program covers programming fundamentals across three languages: HTML/CSS for the web, Python, and JavaScript.

## Repository structure

```
nd000/
├── licoes/      # exercises from the Python lessons
├── notas/       # study notes
└── projetos/    # graded nanodegree projects
```

## Projects

| # | Project | Course | Technologies | Status |
|---|---------|--------|--------------|--------|
| 1 | [Animal Trading Cards](#1-animal-trading-cards) | Introduction to Web Development | HTML, CSS | Completed |
| 2 | [Adventure Game](#2-adventure-game) | Introduction to Programming with Python I | Python | Completed |
| 3 | [Rock Paper Scissors](#3-rock-paper-scissors) | Introduction to Programming with Python II | Python (OOP) | Completed |
| 4 | [Shopping Cart](#4-shopping-cart) | Introduction to JavaScript | JavaScript, Jest | Completed |

### 1. Animal Trading Cards

📁 [`projetos/animal trading card/`](projetos/animal%20trading%20card/)

A web-based trading card about a favorite animal, in this case a small dog. The card shows the animal's name, a photo, a fun fact, a list of characteristics (scientific name, weight, lifespan and habitat) and a description.

**What I practiced:** HTML page structure, semantic tags and lists, and styling with CSS in a separate stylesheet.

**How to view:** open `animal trading card.html` in a browser.

### 2. Adventure Game

📁 [`projetos/new_adventure_game.py`](projetos/new_adventure_game.py)

A text-based adventure game played in the terminal. The player stands in a field between a house and a cave and must decide where to go. A different enemy is randomly chosen each game (troll, pirate, dragon...). Players who explore the cave find the Sword of Ogoroth and can defeat the enemy. At the end, the game asks whether the player wants to play again.

**What I practiced:** functions, conditionals, loops, user input validation, randomness with `random`, and PEP 8 style checked with `pycodestyle`.

**How to play:**

```bash
python projetos/new_adventure_game.py
```

> `projetos/adventure_game.py` is the first version of the game, kept to show how the code evolved into the final version.

### 3. Rock Paper Scissors

📁 [`projetos/rps.py`](projetos/rps.py)

Rock, paper, scissors in the terminal against the computer. The player picks an opponent and the number of rounds, and the score is shown after each round. Each opponent is a class with its own strategy:

- **RockPlayer**: always plays rock.
- **RandomPlayer**: plays randomly.
- **ReflectPlayer**: repeats the opponent's previous move.
- **CyclePlayer**: cycles through the three moves in order.

**What I practiced:** object-oriented programming (classes, inheritance and method overriding), separating player and game responsibilities, and input validation.

**How to play:**

```bash
python projetos/rps.py
```

### 4. Shopping Cart

📁 [`projetos/Shopping Cart/`](projetos/Shopping%20Cart/)

The core logic of a shopping cart for a cash-only fruit stand at a street market. Udacity provided the interface and the code connecting it to the page. My work is in [`starter/src/assets/script.js`](projetos/Shopping%20Cart/starter/src/assets/script.js):

- a product list built from object literals;
- adding products to the cart, increasing and decreasing quantities, and removing items;
- calculating the cart total;
- accepting partial cash payments and reporting the remaining balance or the change due.

**What I practiced:** arrays, objects, functions, array methods (`find`, `forEach`, `splice`) and automated testing with Jest.

**How to run** (requires [Node.js](https://nodejs.org)):

```bash
cd "projetos/Shopping Cart/starter"
npm install
npm start    # opens the store at http://localhost:3000
npm test     # runs the tests
```

## Program content

### 1. Welcome and Orientation
An introduction to the program, the instructors and the support channels.

### 2. Introduction to Web Development
How the web works, the role of the browser, building pages with HTML and styling them with CSS.
**Project:** Animal Trading Cards.

### 3. Introduction to Programming with Python I
First Python programs. The exercises from these lessons are in [`licoes/`](licoes/):

| Lesson | Content | Folder |
|--------|---------|--------|
| Turtles and Code | Core programming concepts by drawing shapes with the `turtle` module | [`02-turtle`](licoes/02-turtle/) |
| Python Functions | Functions, parameters and conditionals | [`03-python_funcions`](licoes/03-python_funcions/) |
| Shell Workshop | Basic use of the Unix terminal | — |
| Python at Home | Installing Python on your own computer | — |
| Strings and Lists | Working with text and lists, including slicing | [`06-strings_and_lists`](licoes/06-strings_and_lists/) |
| Style and Structure | Longer programs, code organization and PEP 8 style | [`07-style_and_structure`](licoes/07-style_and_structure/) |

**Project:** Adventure Game.

### 4. Introduction to Programming with Python II
Files, APIs and object-oriented programming.
**Project:** Rock Paper Scissors.

### 5. Introduction to JavaScript
Data types and variables, conditionals, loops, functions, arrays and objects.
**Project:** Shopping Cart.

### 6. Congratulations! What's next?
Program wrap-up and next steps.

### 7. Git and GitHub (optional)
Version control with Git, creating repositories, commit history, collaborating on GitHub and writing READMEs.
