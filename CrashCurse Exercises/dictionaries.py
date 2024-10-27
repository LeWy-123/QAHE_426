# 6-1 Person and 6-7 Peoples

def dictionary_game():
    a_person = {
        'first_name': 'John',
        'last_name': 'Max',
        'age': 50,
        'city': 'London'
    }

    b_person = {
        'first_name': 'Mark',
        'last_name': 'Tailor',
        'age': 24,
        'city': 'Berlin'
    }

    people = [a_person, b_person]

    for person in people:
        print(f'Person: {person["first_name"]}')
        for key, value in person.items():
            print(f'\t› {key.title()}: {str(value).title()}')
        print('')


# 6-2 Favorite Number
peoples_fav_numbers = {
    'Barbara': 7,
    'Daphne': 3,
    'Béla': 100,
    'Atilla': 9
}

#for key, value in peoples_fav_numbers.items():
#    print(f'{key}\'s favorite number is {value}')

# 6-3 Glossary
glossary = {
    'list comprehension': 'List comprehension offers a shorter syntax when you want to create a new list based on \n'
                          'the values of an existing list.',
    'integer': 'In Python, integers are classified into zero, positive, or negative whole numbers with no fractional\n'
               'part and infinite precision, such as 0, 100, -10, and so on. If there is a decimal, it is considered\n'
               'as a float variable.',
    'float': 'Float is a function or reusable code in the Python programming language that converts values into\n'
             'floating point numbers. Floating point numbers are decimal values or fractional numbers like 133.5,\n'
             '2897.11, and 3571.213, whereas real numbers like 56, 2, and 33 are called integers',
    'dictionary': 'Dictionary is a collection of key-value pairs that can be stored in a dictionary.'
}


def glossaries():
    for key, value in glossary.items():
        print(f'{key} -> {value}')
        print()

    test_for = [['John', 'Max'], ['John', 'noob'], ['cat', 'hello']]
    for key, value in test_for:
        print(f'{key} -> {value}')

    print(type(glossary.keys()), glossary.keys())


# 6-5 Rivers
biggest_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'yangtze': 'china',
    'mississippi-missouri': 'united states',
    'Yenisei': 'mongolia'
}


def print_biggest_rivers():
    print('The biggest rivers are:')
    for key, value in biggest_rivers.items():
        print(f'\tThe {key.title()} is located in {value.title()}')


print('---------------------------------')

def favorite_languages_of_peoples():
    print('Favorite languages are:')
    favorite_languages = {
        'jen' : 'python',
        'sarah': 'java',
        'edward': 'ruby',
        'phil': 'python',
        'joe' : 'C++',
        'mark' : 'javascript'
    }

    new_users = ['jen', 'barbara', 'edward', 'michael']

    for person in favorite_languages.keys():
        if person in new_users:
            print(f'Dear {person.title()} you haven\'t take the poll yet, you should vote for your favorite language! :)')
        else:
            print(f'Thank you {person.title()}! for taking the poll and voted for your favorite language! :)')


# 6-8 Pets:
pets_details = {
    'Cat': {
        'name' : 'Poppy',
        'owner' : 'Madison',
        'breed' : 'Ragdoll',
        'location' : 'San Francisco'
    },
    'Dog' : {
        'name' : 'Luna',
        'owner' : 'Arthur',
        'breed' : 'Golden Retriever',
        'location' : 'Los Angeles'
    }
}

for pet, details in pets_details.items():
    print(f'{pet}')
    for key, value in details.items():
        print(f'\t{key} -> {value}')