import random
import os

moves = ['rock', 'paper', 'scissors']

SCORE1 = 0
SCORE2 = 0


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):  # 记住上一轮对手的招数，并在这一轮出此招数
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move == '':
            return super().move()
        else:
            return self.their_move


class RandomPlayer(Player):  # 随机地返回 'rock'、'paper' 或 'scissors' 之一
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        answer = input("Whats your choice in 'rock','scissors',and 'paper'?")
        if answer == "quit":  # 验证用户输入
            print("BYE~")
            os._exit(0)
        while answer not in moves:
            answer = input("I can't get your idea.Please try again.")
        return answer


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = ''

    def move(self):
        if self.my_move == '':
            return super().move()
        else:
            return self.my_move

    def learn(self, my_move, their_move):  # 记住它在上一轮的招数，并循环采用不同的招数
        if my_move == "rock":
            self.my_move = "scissors"
        if my_move == "scissors":
            self.my_move = "paper"
        if my_move == "paper":
            self.my_move = "rock"


def beats(one, two):  # 判断某个招数是否打败另一个招数
    global SCORE1
    global SCORE2
    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        SCORE1 = SCORE1 + 1
        return f"YOU WIN! Your score: {SCORE1}  Computer's SCORE: {SCORE2}"
    elif one == two:
        return f"No winner.Your score: {SCORE1}  Computer's SCORE: {SCORE2}"
    else:
        SCORE2 = SCORE2 + 1
        return f"TRY AGAIN.Your score: {SCORE1}  Computer's SCORE: {SCORE2}"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.end = False

    def play_round(self):
        move1 = self.p1.move()
        print(move1)
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(beats(move1, move2))

    def play_game(self):
        print("Game start!")
        for round in range(100):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    score = 0
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
