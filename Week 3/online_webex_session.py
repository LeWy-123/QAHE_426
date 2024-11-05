def char_to_ascii():
    print('Program Started!')
    char = input('Please enter a character: ')
    if len(char) == 1:
        print(f'The ascii code for {char} is {ord(char)}')
    else:
        print(f'Error: Enter a single character, please')

    print('Program Ended!')

def ascii_to_char():
    code = int(input('Please enter a code: '))
    if 32<=code<=126:
        print(f'The ascii code for {code} is {chr(code)}')
    else:
        print(f'Error: Enter a valid code is out of range')

    print('Program Ended!')

def greet_user():
    # something
    user = input('Please enter your name: ')
    print(f'Hello, {user}')

greet_user()