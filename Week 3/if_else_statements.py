# Task 1 in week 2 > :D
print('Would you like to read books? ', end='>> ')
user_input = input().lower()

if user_input == 'adventure':
    print(f'I like {user_input} books!')
elif user_input == 'action':
    print(f'I like {user_input} books!')
elif user_input == 'science':
    print(f'I like {user_input} books!')
elif user_input == 'quit':
    print('Thank you for playing!')
else:
    print(f'What did you type man? :D ({user_input}), that\'s not included! in the program')


# Taks 2 in week 2
print('Enter the activity to be performed: ')
user_input = input('Answer> ').lower()
if user_input == 'calculate' or 'calc' or 'calculation':
    print('Calculating...')
    user_input = input('math equation> ').lower()
    try:
        print('your result: ', eval(user_input))
    except:
        print('It wasn\'t valid mathematical')

print('Activity completed!')
