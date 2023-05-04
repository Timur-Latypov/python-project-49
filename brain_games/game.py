import prompt


NUMBERS_OF_ROUND = 3


def game_engine(game_name):
    user_name = prompt.string("Welcome to the Brain Games!\n"
                              "May I have your name? ")
    print(f"Hello, {user_name}!\n{game_name.GAME_TASK}")
    i = 0
    while i < NUMBERS_OF_ROUND:
        (question, true_answer) = game_name.make_question_and_true_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print("Correct!")
            i += 1
        else:
            print(f"\'{user_answer}\' is wrong answer ;(. "
                  f"Correct answer was \'{true_answer}\'")
            print(f"Let\'s try again, {user_name}!")
            i = NUMBERS_OF_ROUND + 1
        if i == NUMBERS_OF_ROUND:
            print(f"Congratulations, {user_name}!")
            break
