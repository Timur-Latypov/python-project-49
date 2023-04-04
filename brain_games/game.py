import prompt


def start_game(game_name):
    user_name = prompt.string("Welcome to the Brain Games!\n"
                              "May I have your name? ")
    print(f"Hello, {user_name}!\n{game_name.task()}")
    i = 0
    while i < 3:
        (question, true_answer) = game_name.game_engine()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print("Correct!")
            i += 1
        else:
            print(f"\'{user_answer}\' is wrong answer ;(. "
                  f"Correct answer was \'{true_answer}\'")
            print(f"Let\'s try again, {user_name}!")
            i = 4
        if i == 3:
            print(f"Congratulations, {user_name}!")
            break
