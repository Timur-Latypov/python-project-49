import random


def task():
    return "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def game_engine():
    question = random.randrange(3, 30)
    for i in range(2, question):
        if question % i == 0:
            return (question, "no")
    return (question, "yes")
