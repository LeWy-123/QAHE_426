# Activity 1: Nested Decision
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

# Activity 2: Multiple Nested Decisions
# Start of the program
def look_for_phone():
    print("Where should I look?")
    location = input()

    if location == "in the bedroom":
        print("Where in the bedroom should I look?")
        specific_location = input()
        if specific_location == "under the bed":
            print("Found some shoes but no phone.")
        else:
            print("Found some mess but no phone.")

    elif location == "in the bathroom":
        print("Where in the bathroom should I look?")
        specific_location = input()
        if specific_location == "in the bathtub":
            print("Found a rubber duck but no phone.")
        else:
            print("Found bathroom stuff but no phone.")

    elif location == "in the living room":
        print("Where in the living room should I look?")
        specific_location = input()
        if specific_location == "on the table":
            print("Yes! I found my phone!")
        else:
            print("Found some stuff but no phone.")

    else:
        print("I do not know where that is but I will keep looking.")

# Run the program
look_for_phone()
# Task 1
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
# Task 2
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
# Task 3
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