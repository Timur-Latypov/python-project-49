import random


RANGE = 100
GAME_TASK = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def make_question_and_true_answer():
    question = random.randrange(RANGE)
    if is_even(question):
        return (question, "yes")
    else:
        return (question, "no")


def is_even(number):
    return number % 2 == 0

