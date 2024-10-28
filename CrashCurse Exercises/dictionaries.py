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
    'Barbara': [7, 5, 3, 11],
    'Daphne': [3, 8, 9, 66, 69],
    'Béla': [100, 15, 18],
    'Atilla': [9, 3]
}

for key, value in peoples_fav_numbers.items():
    print(f'{key}\'s favorite numbers is', end='')
    for numbers in value:
        print(f', {numbers}', end='')
    print()

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
def pets_and_owners():
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

# 6-9 favorite places
def fav_places():
    favorite_places = {
        'Oliver' : ['The British Museum', 'London Eye', 'Kew Gardens'],
        'Leo' : ['Buckingham Palace'],
        'Harry' : ['Tower Of London', 'Tower Bridge'],
        'Oscar' : ['River Thames', 'Madame Tussaud\'s']
    }

    for name, locations in favorite_places.items():
        if len(locations) <= 1:
            print(f'{name}\'s favorite location is', locations[0])
        else:
            print(f'{name}\'s favorite locations is')
            for location in locations:
                print(f'\t⁜ {location}')


# 6-11 Cities
def print_CAPITALS_and_facts():
    capitals = {
        'Austria' : {
            'capital' : 'Viena',
            'population' : 9_118_472,
            'facts' : 'Austria, largely mountainous landlocked country of south-central Europe. Together with Switzerland, '
                     'it forms what has been characterized as the neutral core of Europe, notwithstanding Austria’s full '
                     'membership since 1995 in the supranational European Union (EU).',
            'language' : 'german'
        },
        'Hungary' : {
            'capital' : 'Budapest',
            'population' : 9_994_993,
            'facts' : 'Hungary is also the birthplace of many famous people. Erno Rubik, a sculptor and professor, '
                      'invented the Rubik\'s Cube in 1974. Hungary boasts 13 Nobel Prize winners, and magician Harry '
                      'Houdini was also born in the country\'s capital, Budapest. The Eastern European country\'s cuisine '
                      'primarily consists of meat dishes.',
            'language' : 'hungarian'
        },
        'Portugal' : {
            'capital' : 'Portugal',
            'population' : 10_420_938,
            'facts' : "Portugal and Britain are best friends. In fact, they have the oldest official continuous treaty "
                      "between two countries in the entire world, dating back to 1386. The national flower of Portugal is "
                      "lavender. Until the famous expeditions by Portuguese sailors in the 15th century, Cape St Vincent "
                      "at the western end of the Algarve was believed to be the end of the world. At 12 miles long, "
                      "the Vasco de Gama Bridge in Lisbon is the longest bridge in Europe. The Portuguese language has "
                      "600 words that come from Arabic, from when the country was part of the huge Moorish/Arabic empire.",
            'language' : 'portuguese'
        },
        'United_Kingdom' : {
            'capital' : 'London',
            'population' : 69_272_487,
            'facts' : 'Brits drink a lot of tea... about 100 million cups every day! The stereotype that the British '
                      'drink a lot of tea is immediately confirmed with this fun fact. They drink around 100-160 million '
                      'cups of tea daily, which is about 36 billion every year. The difference from most of the countries '
                      'in the world is that almost all the tea drinkers in the UK (98%) add milk to their cup of tea.',
            'language' : 'english'
        }
    }

    for country, details in capitals.items():
        print(f'Facts and details from {country}:')
        for fact, values in details.items():
            print(f'\t⁜{fact.title()}, {str(values).title()}')
        print()

# 6-12 Extension:
if __name__ == '__main__':
    print('Yes')