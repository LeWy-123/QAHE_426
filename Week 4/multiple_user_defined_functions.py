# Activity 1: Multiple User Defi ned Functions

def display_ladder(steps=0):        # Defines the method which creates ASCII ladder based on argument input
    for i in range(steps):          # iterates up to X number based on argument
        print('| |')
        print('***')
    print('| |')

def create_ladder():
    steps = int(input('How many steps remain?\n->'))
    display_ladder(steps)

create_ladder()
# Activity 2: Return Values
