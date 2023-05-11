import prompt


ROUNDS_COUNT = 3


def play(game):
    user_name = prompt.string("Welcome to the Brain Games!\n"
                              "May I have your name? ")
    print(f"Hello, {user_name}!\n{game.TASK}")
    i = 0
    while i < ROUNDS_COUNT:
        (question, true_answer) = game.make_question_and_true_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print("Correct!")
            i += 1
        else:
            print(f"\'{user_answer}\' is wrong answer ;(. "
                  f"Correct answer was \'{true_answer}\'")
            print(f"Let\'s try again, {user_name}!")
            i = ROUNDS_COUNT + 1
        if i == ROUNDS_COUNT:
            print(f"Congratulations, {user_name}!")
            break
