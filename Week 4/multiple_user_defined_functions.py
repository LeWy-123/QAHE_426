# Activity 1: Multiple User Defi ned Functions

def display_ladder(steps=0):        # Defines the method which creates ASCII ladder based on argument input
    for i in range(steps):          # iterates up to X number based on argument
        print('| |')
        print('***')
    print('| |')

def create_ladder():
    steps = int(input('How many steps remain?\n->'))
    display_ladder(steps)

#create_ladder()
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

#run()
# Activity 3: Word Manipulation
def display_in_box(text):
    length = len(text)
    print('\U00002014'  *(length  +6))         # UTF-32 format character multiplied by length of the string plus 6
    print(f'|  {text : ^35}  |')               # f string formating to adjust the text to the center. and pipe as border
    print('\U0000203E' * (length + 6))

def lower_case(text):                   # built-in function to swap characters to lowercase
    return text.lower()

def upper_case(text):                   # built-in function to swap characters to uppercase
    return text.upper()

def mirrored(text):                     # mirroring the text by built-in function
    return text[::-1]

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


