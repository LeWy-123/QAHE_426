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