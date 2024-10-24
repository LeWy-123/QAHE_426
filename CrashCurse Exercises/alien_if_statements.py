# exercises for IF statements
# 5-3 Alien colors #1
def alien_colors():
    alien_color = input('Type a colore in\n->').lower()

    if alien_color == 'green':
        print('You just earned 5 points.')
    elif alien_color == 'yellow':
        print('You just earned 10 points.')
    elif alien_color == 'red':
        print('You just earned 15 points.')

# 5-6 stages of life
def age_challenge():
    try:
        age = int(input('Type a age in\n->'))
    except ValueError:
        print('Cant be converted to an integer')
        age = 0
    except TypeError:
        print('Cant convert to an integer')
        age = 0

    if age <= 2:
        print('You are a baby.')
    elif age <= 4:
        print('You are a toddler.')
    elif age <= 13:
        print('You are a kid.')
    elif age <= 20:
        print('You are an teenager.')
    elif age <= 65:
        print('You are an adult.')
    elif age >= 65:
        print('You are an elder.')
    else:
        print('You are an ancient mythological creature XD a fossil.')

# 5-7 favorite fruit
def favorite_stuff():
    favorite_fruits = ['banana', 'orange', 'strawberry', 'blueberry', 'blackberry', 'kiwi', 'apple', 'tomato', 'pear']

    for fruit in favorite_fruits:
        if fruit == 'banana':
            print('You really like banana.', end=' ')
        if fruit == 'kiwi':
            print('You really like kiwi.', end=' ')
        if fruit == 'apple':
            print('You really like apple.', end=' ')

# 5-8  hello admin
def hello_admin():
    users = ['admin', 'Barbara']
    if users:
        for user in users:
            if user.lower() == 'admin'.lower():
                print('Hello admin, would you like to see a status report?')
            else:
                print('Hello %s, thank you for logging in again.' % user)
    else:
        print('List is empty, We need to find some users')

# 5-10 checking usernames
def usernames():
    current_users = ['admin', 'Barbara', 'Levente', 'Mickael']
    new_users = ['Barbara', 'David99', 'Monolith33', 'BackV']
    current_users_lower = [user.lower() for user in current_users]

    for user in new_users:
        if user.lower() in current_users_lower:
            print(f'You need to enter a new username please! {user}')
        else:
            print(f'That username: {user} Available!')

# 5-11 Ordinal numbers
def ordinal_version():
    ordinal_numbers = [i for i in range(1, 10)]
    for number in ordinal_numbers:
        if number == 1:
            print(f'•{number}st')
        elif number == 2:
            print(f'•{number}nd')
        elif number == 3:
            print(f'•{number}rd')
        else:
            print(f'•{number}th')

#