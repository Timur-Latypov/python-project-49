import random


RANGE = 10
GAME_TASK = "What is the result of the expression?"


def make_question_and_true_answer():
    a = random.randrange(RANGE)
    b = random.randrange(RANGE)
    operation = random.choice('+*-')
    true_answer = str(result_calculation(a, b, operation))
    question = f'{a} {operation} {b}'
    return (question, true_answer)


def result_calculation(a, b, operation):
    match operation:
        case '*':
            return a * b
        case '+':
            return a + b
        case '-':
            return a - b
