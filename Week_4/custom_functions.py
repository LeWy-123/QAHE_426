# Activity 1: Simple User Defi ned Function
def listen():
    sound = ''          # define a variable
    while True:         # use a while loop to prompt the user endlessly until no input
        sound = input('What sound did you hear?\n-> ')
        print(f'That was a loud {sound}')
        if sound == '' or sound == ' ':
            break       # break out the loop and program terminates


# Activity 2: Nesting
def identify():
    object_seen = input('What lies before us? ')
    if object_seen == 'a large boulder' or 'boulder':
        print('It\'s time to run!')
    else:
        print(f'We will be fi ne. coz it\'s {object_seen}.')

# Activity 3: Parameters
def escape_by(plan=None):
    if plan == 'jumping over':
        print('We cannot escape that way! The boulder is too big!')
    elif plan == 'running around':
        print('We cannot escape that way! The boulder is moving too fast!')
    elif plan == 'cross bridge ahead':
        print('That might just work! Let\'s go!')
    elif plan is None:
        return 0
    else:
        print('We cannot escape that way! The boulder is in the way!')

# calling the method
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
print()
# Activity 4: Loop
def cross_bridge(step):             # Defining the method
    i = 0                           # creating the iterator variable
    while i < step:                 # engaging the loop which runs till reaches {step} count
        i += 1
        print('Crossed step.')      # displays the requested string
        if i % 5 == 0:              # this code checks whether the iterator 'i' is multiplies of 5. every 5th iteration
            if i <= 5:              # displays the required message
                print('We must keep going!')
            elif i > 5:
                print('The bridge is collapsing!')

cross_bridge(11)

# Activity 5: Multiple Parameters
def climb_ladder(number_of_steps_remaining, number_of_steps_crossed):
    if(number_of_steps_remaining > number_of_steps_crossed):             # Compares 2 numbers
        print("Still some way to go!")
    else:
        print("We are almost there!")

# calling the method
climb_ladder(5, 2)
climb_ladder(2, 5)

