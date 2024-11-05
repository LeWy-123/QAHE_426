# Activity 1: Simple User Defi ned Function
def listen():
    sound = ''          # define a variable
    while True:         # use a while loop to prompt the user endlessly until no input
        sound = input('What sound did you hear?\n-> ')
        print(f'That was a loud {sound}')
        if sound == '' or sound == ' ':
            break       # break out the loop and program terminates


# Activity 2: Nesting
def identify():
    object_seen = input('What lies before us? ')
    if object_seen == 'a large boulder' or 'boulder':
        print('It\'s time to run!')
    else:
        print(f'We will be fi ne. coz it\'s {object_seen}.')
