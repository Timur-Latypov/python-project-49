import random


RANGE = 100
BEGIN = 2
END = 20
GAME_TASK = "What number is missing in the progression?"


def make_question_and_true_answer():
    progression_begin = random.randrange(RANGE)
    progression_step = random.randrange(BEGIN, END)
    progression_lenght = random.randrange(BEGIN, END)
    hidden_position = random.randrange(progression_lenght)
    progression = create_progression(progression_begin, progression_step, progression_lenght)
    true_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'
    question = make_question(progression)
    return (question, true_answer)


def create_progression(start, step, lenght):
    result = []
    for i in range(lenght):
        result.append(start)
        start += step
    return result


def make_question(progression):
    return ''.join(str(progression))

