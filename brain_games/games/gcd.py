import random

BEGIN = 1
END = 30
TASK = "Find the greatest common divisor of given numbers."


def make_question_and_true_answer():
    number_1 = random.randrange(BEGIN, END)
    number_2 = random.randrange(BEGIN, END)
    question = f'{number_1} {number_2}'
    true_answer = str(find_gcd(number_1, number_2))
    return (question, true_answer)


def find_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
