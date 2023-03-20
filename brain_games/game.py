import prompt
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progression
import brain_games.games.prime


def welcome(game):
    match game:
        case "even":
            welcome = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
        case "calc":
            welcome = "What is the result of the expression? "
        case "gcd":
            welcome = "Find the greatest common divisor of given numbers."
        case "progression":
            welcome = "What number is missing in the progression?"
        case "prime":
            welcome = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!\n{welcome}")
    if game_engine(game):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let\'s try again, {name}!'")


def game_engine(game):
    i = 0
    while i < 3:
        match game:
            case "even":
                (question, true_answer) = brain_games.games.even.is_even()
            case "calc":
                (question, true_answer) = brain_games.games.calc.calc()
            case "gcd":
                (question, true_answer) = brain_games.games.gcd.gcd()
            case "progression":
                (question, true_answer) = brain_games.games.progression.progression()
            case "prime":
                (question, true_answer) = brain_games.games.prime.prime()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print("Correct!")
            i += 1
        else:
            print(f"\'{user_answer}\' is wrong answer ;(. Correct answer was \'{true_answer}\'")
            return False
            i = 0
        if i == 3:
            return True
