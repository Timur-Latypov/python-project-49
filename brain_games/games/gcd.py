import random


def gcd():
    a = random.randrange(5, 30)
    b = random.randrange(5, 60)
    question = f'{a} {b}'
    # find gcd
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    true_answer = str(a)
    return (question, true_answer)
