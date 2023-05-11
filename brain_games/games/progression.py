import random


RANGE = 100
BEGIN = 5
END = 20
TASK = "What number is missing in the progression?"


def make_question_and_true_answer():
    initial_term = random.randrange(RANGE)
    common_difference = random.randrange(BEGIN, END)
    lenght = random.randrange(BEGIN, END)
    hidden_position = random.randrange(lenght)
    progression = create_progression(initial_term, common_difference, lenght)
    true_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'
    question = make_question(progression)
    return (question, true_answer)


def create_progression(initial_term, common_difference, lenght):
    result = []
    for i in range(lenght):
        result.append(str(initial_term))
        initial_term += common_difference
    return result


def make_question(progression):
    return ' '.join(progression)
