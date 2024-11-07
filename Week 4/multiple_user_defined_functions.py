# Activity 1: Multiple User Defi ned Functions

def display_ladder(steps=0):        # Defines the method which creates ASCII ladder based on argument input
    for i in range(steps):          # iterates up to X number based on argument
        print('| |')
        print('***')
    print('| |')

def create_ladder():
    steps = int(input('How many steps remain?\n->'))
    display_ladder(steps)

#create_ladder()            i comment out not to run the code
# Activity 2: Return Values
def sum_weights(weight_npc, weight_inv):                    # summing up two arguments
    try:                                                    # error handling if not integer then returns an error
        return int(weight_npc) + int(weight_inv)
    except ValueError: return 0


def calc_avg_weight(weight_npc, weight_inv):
    try:
        return sum_weights(weight_npc, weight_inv) / 2      # this uses the previous method to add up the numbers then
    except ValueError: return 0

def run():
    print('Enter the weight of the character: ', end='')    # display a prompt
    weight_npc = input()
    print('Enter the weight of the inventory: ', end='')
    weight_inv = input()
    print('What would you like to calculate? (sum or average).')
    answer = input('-> ')
    if answer == 'sum':                                     # if the answer was sum it executes the sum_weight method
        print(f'The sum of weights is: ', sum_weights(weight_npc, weight_inv))
    elif answer == 'average' or 'avg':                      # if the user chose average its calculates its average
        print(f'The average weights is: ', calc_avg_weight(weight_npc, weight_inv)) # this returns a float number
    else:
        print('Please enter either sum or average.')        # if the options was wrong its displays a message and quits

#run()          i comment out not to run the code
# Activity 3: Word Manipulation
def display_in_box(text):
    formated = f'|  {text : ^35}  |'
    length = len(formated)
    print('\U00002014'  *(length))         # UTF-32 format character multiplied by length of the string plus 6
    print(formated)                            # f string formating to adjust the text to the center. and pipe as border
    print('\U0000203E' * (length))

def lower_case(text):                   # built-in function to swap characters to lowercase
    print(text.lower())

def upper_case(text):                   # built-in function to swap characters to uppercase
    print(text.upper())

def mirrored(text):                     # mirroring the text by built-in function
    print(text[::-1])

def repeat(text):
    i = 0
    try:
        rep = int(input('How many times would you like to repeat?\n-> '))
        while i < rep:
            if i % 2 == 0:              # this statement makes the lines to alternate
                print(text.lower())     # prints at lowercase letter
            else:
                print(text.upper())     # prints at uppercase letter
            i += 1
    except ValueError:                  # error handling if types ar missmatch
        pass
    except TypeError:                   # A TypeError means that you're trying to combine values of different types that
                                        # are not compatible
        pass

def word_manipulation():
    while True:
        print("""                 
1) Display in a Box – display the word in an ASCII art box
2) Display Lower-case – display the word in lower-case e.g. hello
3) Display Upper-case – display the word in upper-case e.g. HELLO
4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
5) Repeat – ask the user how many times to display the word and then display the word that many times alternating
   between upper-case and lower-case.""")       # copied and pasted from the task the prompt
        option = input('-> ')                   # the options prompt there are 6 options one is for fun.
        if option == '1':
            text = input('Enter a word: ')
            display_in_box(text)
        elif option == '2':
            text = input('Enter a word: ')
            lower_case(text)
        elif option == '3':
            text = input('Enter a word: ')
            upper_case(text)
        elif option == '4':
            text = input('Enter a word to mirror: ')
            mirrored(text)
        elif option == '5':
            text = input('Enter a word to repeat: ')
            repeat(text)
        elif option == '6':
            print('Hehe no options 6. :D')
        else:
            print('program quit!...')
            break

#word_manipulation()                i comment out not to run the code
