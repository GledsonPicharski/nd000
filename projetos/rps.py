#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    """The Player class is the parent class for all of the Players
    in this game. Each subclass implements its own strategy."""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    """Always plays 'rock'."""

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    """Chooses its move at random."""

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """Asks the human user which move to make."""

    def move(self):
        while True:
            choice = input("Rock, paper, scissors? > ").strip().lower()
            if choice in moves:
                return choice
            print("Invalid move. Please type rock, paper or scissors.")


class ReflectPlayer(Player):
    """Plays the move the opponent played in the previous round.
    Plays at random on the first round."""

    def __init__(self):
        self.their_last_move = None

    def move(self):
        if self.their_last_move is None:
            return random.choice(moves)
        return self.their_last_move

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    """Cycles through rock, paper and scissors.
    Starts with a random move on the first round."""

    def __init__(self):
        self.my_last_move = None

    def move(self):
        if self.my_last_move is None:
            return random.choice(moves)
        index = moves.index(self.my_last_move)
        return moves[(index + 1) % len(moves)]

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


class Game:
    def __init__(self, p1, p2, rounds=3):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds
        self.rounds_played = 0
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            self.score1 += 1
            print("** PLAYER ONE WINS **")
        else:
            self.score2 += 1
            print("** PLAYER TWO WINS **")
        print(f"Score: Player One {self.score1}, "
              f"Player Two {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.rounds_played += 1

    def play_game(self):
        print("Rock Paper Scissors, Go!\n")
        for round in range(1, self.rounds + 1):
            print(f"Round {round}:")
            self.play_round()
        self.announce_winner()

    def announce_winner(self):
        print(f"Game over! Rounds played: {self.rounds_played}")
        print(f"Final score: Player One {self.score1}, "
              f"Player Two {self.score2}")
        if self.score1 > self.score2:
            print("** PLAYER ONE WINS THE GAME! **")
        elif self.score2 > self.score1:
            print("** PLAYER TWO WINS THE GAME! **")
        else:
            print("** THE GAME IS A TIE! **")


def choose_opponent():
    opponents = {
        '1': ('Rock player', RockPlayer),
        '2': ('Random player', RandomPlayer),
        '3': ('Reflect player', ReflectPlayer),
        '4': ('Cycle player', CyclePlayer),
    }
    print("Choose your opponent:")
    for key, (name, _) in opponents.items():
        print(f"  {key}. {name}")
    while True:
        choice = input("> ").strip()
        if choice in opponents:
            return opponents[choice][1]()
        print("Please enter a number from 1 to 4.")


def choose_rounds():
    while True:
        choice = input("How many rounds? > ").strip()
        if choice.isdigit() and int(choice) > 0:
            return int(choice)
        print("Please enter a positive whole number.")


def main():
    try:
        opponent = choose_opponent()
        rounds = choose_rounds()
        game = Game(HumanPlayer(), opponent, rounds)
        game.play_game()
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Goodbye!")


if __name__ == '__main__':
    main()
