# 7-8 Deli:
print('DELI run out of pastrami!')
print('\U00002014' * 26)
sandwich_orders = ['Pastrami', 'BLT', 'Grilled Cheese', 'Pastrami', 'Ham and Cheese', 'Pastrami',
                   'Roast Beef', 'Tuna Salad', 'Veggie Wrap', 'Pastrami', 'Pastrami']

# 7-9 No Pastrami
def remove_all_items(item):
    if item not in sandwich_orders:
        print(f'Invalid item there is no {item} in the list of sandwich_orders')
        return None
    while item in sandwich_orders:
        sandwich_orders.remove(item)

# removing pastrami because we run out
remove_all_items('Pastrami')

def sandwich_list():
    finished_sandwiches = []

    for sandwich in sandwich_orders:
        print(f'I made your {sandwich} sandwich!')
        finished_sandwiches.append(sandwich)

    sandwich_orders.clear()
    print(f'\nSandwiches has been made:')
    for made_sandwich in finished_sandwiches:
        print(f'\t> {made_sandwich}')

#sandwich_list()

# 7-10 Dream Vacation
dream_vacation_pool = {}
while True:
    print('If you could visit one place in t he world, where would you go?')
    place = input('Place: ')
    if place.lower() in ['', ' ', 'quit', 'end']: break
    name = input('And your Name: ')
    print('\U00002014'*20)
    dream_vacation_pool[name] = place


for name, vacation in dream_vacation_pool.items():
    print(f'{name} would like to visit {vacation}. :)')