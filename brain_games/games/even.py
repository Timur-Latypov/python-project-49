import random


def task():
    return 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def game_engine():
    question = random.randrange(100)
    if question % 2 == 0:
        return (question, "yes")
    else:
        return (question, "no")
