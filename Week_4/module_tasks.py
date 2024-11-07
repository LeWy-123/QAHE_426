import random
import Week_1.output_tasks as o
import Week_1.input_tasks as inp

# Activity 1: Importing Modules
def guess_game():
    print('Please enter the minimum value: ')
    min_value = int(input())
    print('Please enter the maximum value: ')
    max_value = int(input())
    guess_me = random.randint(min_value, max_value)
    print(f'I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?')
    while True:
        guess = int(input())
        if guess == guess_me:
            print(f'Congrats! You guessed the correct number! {guess_me}')
            break
        elif guess < guess_me:
            print(f'Sorry {guess} is too low!')
        elif guess > guess_me:
            print(f'Sorry {guess} is too high!')
        elif guess > max_value or guess < min_value:
            print(f'Sorry but you guess out of range, range is ({min_value}-{guess_me})')
        else:
            print('error!')
            break

#guess_game() commented out not to run

# Activity 2: Multiple Module
def run_week_one():
    print('Which program in "Week 1" do you wish to run?')
    print(f'\t⦿ simple_message \tout\n',
          f'\t⦿ simple_message2 {"> output_tasks" :>25}\n',
          f'\t⦿ multiline_text {"> output_tasks" :>25}\n',
          f'\t⦿ escape_chars {"> output_tasks" :>25}\n',
          f'\t⦿ robot {"> output_tasks" :>25}',)
    response = input()
    if response == 'simple_message':
        o.simple_message()
    elif response == 'multiline_text':
        o.multiline_text()
    elif response == 'escape_chars':
        o.escape_chars()
    elif response == 'robot':
        o.robot()
    elif response == 'simple_message2':
        o.simple_message2()

def run():
    while True:
        print('What would you like to do?')
        print('[a] Run "Week 1" programs')
        print('[b] Quit')
        response = input()

        if response == 'a':
            run_week_one()
        elif response == 'q':
            break
        else:
            print('Invalid option! Please try again.')


run()