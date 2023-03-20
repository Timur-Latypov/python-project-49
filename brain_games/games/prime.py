import random


def prime():
    question = random.randrange(3, 30)
    for i in range(2, question):
        if question % i == 0:
            return (question, "no")
    return (question, "yes")
