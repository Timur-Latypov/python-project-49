import random


RANGE = 10
TASK = "What is the result of the expression?"


def make_question_and_true_answer():
    a = random.randrange(RANGE)
    b = random.randrange(RANGE)
    operation = random.choice('+*-')
    true_answer = str(calculate_result(a, b, operation))
    question = f'{a} {operation} {b}'
    return (question, true_answer)


def calculate_result(a, b, operation):
    match operation:
        case '*':
            return a * b
        case '+':
            return a + b
        case '-':
            return a - b
