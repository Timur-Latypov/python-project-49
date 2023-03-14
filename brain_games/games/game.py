import prompt
import random


def welcome(game):
    match game:
        case "even":
            welcome = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
        case "calc":
            welcome = "What is the result of the expression? "
        case "gcd":
            welcome = "Find the greatest common divisor of given numbers."
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
                (question, true_answer) = is_even()
            case "calc":
                (question, true_answer) = calc()
            case "gcd":
                (question, true_answer) = gcd()
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


def is_even():
    question = random.randrange(100)
    if question % 2 == 0:
        return (question, "yes")
    else:
        return (question, "no")


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


def gcd():
    a = random.randrange(30)
    b = random.randrange(30)
    question = f'{a} {b}'
    # find gcd
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    true_answer = str(a)
    return (question, true_answer)
