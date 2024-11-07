# Activity 1: ASCII Value
def char_to_ascii():
    print('Program Started!')
    char = input('Please enter a character: ')
    if len(char) == 1:
        print(f'The ascii code for {char} is {ord(char)}')
    else:
        print(f'Error: Enter a single character, please')

    print('Program Ended!')

# Activity 2: ASCII character
def ascii_to_char():
    code = int(input('Please enter a code: '))
    if 32<=code<=126:
        print(f'The ascii code for {code} is {chr(code)}')
    else:
        print(f'Error: Enter a valid code is out of range')

    print('Program Ended!')

