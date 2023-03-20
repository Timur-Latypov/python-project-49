import random


def is_even():
    question = random.randrange(100)
    if question % 2 == 0:
        return (question, "yes")
    else:
        return (question, "no")
