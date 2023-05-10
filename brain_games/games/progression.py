import random


RANGE = 100
BEGIN = 5
END = 20
GAME_TASK = "What number is missing in the progression?"


def make_question_and_true_answer():
    begin = random.randrange(RANGE)
    step = random.randrange(BEGIN, END)
    lenght = random.randrange(BEGIN, END)
    hidden_position = random.randrange(lenght)
    progression = create_progression(begin, step, lenght)
    true_answer = str(progression[hidden_position])
    progression[hidden_position] = "\'..\'"
    question = make_question(progression)
    return (question, true_answer)


def create_progression(progression_begin, progression_step, progression_lenght):
    result = []
    for i in range(progression_lenght):
        result.append(str(progression_begin))
        progression_begin += progression_step
    return result


def make_question(progression):
    return ', '.join(progression)
