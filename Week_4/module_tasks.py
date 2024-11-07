import random
import Week_1.input_tasks
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