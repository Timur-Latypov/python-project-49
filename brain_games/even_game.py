import prompt
import random


def welcome():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    if game():
        print(f'Congratulations, {name}!')


def game():
    i = 0
    while i < 3:
        number = random.randrange(100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer:')

        if answer == is_even(number):
            print('Correct!')
            i += 1
        elif answer == 'yes':
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'no\'')
            i = 0
        elif answer == 'no':
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'yes\'')
            i = 0
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{is_even(number)}\'')
            i = 0
        if i == 3:
            return True


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
