import random


FIRST_PRIME = 2
RANGE = 30
GAME_TASK = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def make_question_and_true_answer():
    question = random.randrange(FIRST_PRIME, RANGE)
    if is_prime:
        return (question, "yes")
    else:
        return (question, "no")


def is_prime(number):
    for i in range(FIRST_PRIME, number):
        if number % i == 0:
            return False
    return True
