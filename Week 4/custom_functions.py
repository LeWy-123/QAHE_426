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

# Activity 3: Parameters
def escape_by(plan=None):
    if plan == 'jumping over':
        print('We cannot escape that way! The boulder is too big!')
    elif plan == 'running around':
        print('We cannot escape that way! The boulder is moving too fast!')
    elif plan == 'cross bridge ahead':
        print('That might just work! Let\'s go!')
    elif plan is None:
        return 0
    else:
        print('We cannot escape that way! The boulder is in the way!')

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
