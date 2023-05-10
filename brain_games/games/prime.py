import random


FIRST_PRIME = 2
RANGE = 30
GAME_TASK = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def make_question_and_true_answer():
    question = random.randrange(FIRST_PRIME, RANGE)
    enumeration_range = range(FIRST_PRIME, question)
    if is_prime(question, enumeration_range):
        return (question, "yes")
    else:
        return (question, "no")


def is_prime(number, enumeration_range):
    if number == 2:
        return True
    for i in enumeration_range:
        if number % i == 0:
            return False
    return True
