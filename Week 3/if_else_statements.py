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

print('-----------------------------')
# Task 2 in week 2
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
print('-----------------------------')
# Task 3 week 2
print('Please enter whole number: ')
try:
    user_input = int(input('→ '))
    if user_input % 2 == 0:
        print(f'your number is even my friend: {user_input}')
    elif user_input % 2 != 0:
        print(f'your number is odd my friend: {user_input}')
    else:
        print('It was not what i am expecting')
except ValueError:
    print('It was not integer may you type a text?')
finally:
    print('activity completed! my friend')

print('-----------------------------')
#task 4
# Ask user for book details
print("What type of cover does this book have?")
cover_type = input ()


# Display appropriate message
if cover_type == "soft":
    print("Is the book perfect-bound?")
    perfect_bound = input()
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")