import random


def progression():
    arithmetic_progression_lenght = random.randrange(5, 15)
    hidden_position = random.randrange(arithmetic_progression_lenght)
    step = random.randrange(2, 9)
    start = random.randrange(30)
    arithmetic_progression = []
    for i in range(arithmetic_progression_lenght):
        arithmetic_progression.append(start)
        start += step
    true_answer = str(arithmetic_progression[hidden_position])
    arithmetic_progression[hidden_position] = '..'
    question = ''
    for i in arithmetic_progression:
        question += f'{i} '
    return (question, true_answer)
