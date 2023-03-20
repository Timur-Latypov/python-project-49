import random


def calc():
    a = random.randrange(10)
    b = random.randrange(10)
    operation = random.choice('+*-')
    true_answer = str(random_operation(a, b, operation))
    question = f'{a} {operation} {b}'
    return (question, true_answer)


def random_operation(a, b, operation):
    match operation:
        case '*':
            return a * b
        case '+':
            return a + b
        case '-':
            return a - b
