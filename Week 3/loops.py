# Activity 1: Simple loop
# program that print out n times 'remove apple'
print("How many apples should I remove?")
apples = int(input("Enter you how many apples you wanna remove from the box:\nyour answer> "))
while apples > 0:                            # opens a loop that counts backwards instead count up to desired numbers
    print(f'apple removed! {apples} left')   # prints Apple removed every line and tells how many apples left
    apples -= 1                              # decrement the variable when reach 0 it breaks the loop

print()

# Activity 2: Count
print('How many obstacles must I avoid?')    # print the question
avoidant = int(input("your answer> "))
obstacles = 0
while avoidant > obstacles:                  # opens a while loop to count and rach the desired obstacle numbers
    print('Avoiding...', end = '')
    obstacles += 1
    print(f'...Done! {obstacles} obstacles avoided!')

print('\nAll obstacles have been avoided.')
print()

# Activity 3: ASCII
bar = '█'                                    # crete a variable contains the ascii character
print('How many bars should be charged?')    # prompt the user fpr desired charging level
charge_level = 1
desired_level = int(input("your answer> "))  # the actual prompt where assign to a variable
while charge_level <= desired_level:
    if charge_level == 0:                    # this i put here if the charge level is 0 it will displays it
        print(f'Battery empty')
    else:
        print(f'Charging {bar * charge_level}')
    charge_level += 1                        # increment charge bars by 1

print('\nThe battery is fully charged.')
print()

# Activity 4: Repeating Word
parse = input('Please enter a phrase: ')     # in prompts the user for a string
parse = parse.replace(" ", "")   # removes any empty spaces just to count the text and not all objects
i = 0
while i < len(parse):                        # while loop runs till reaches the length of the parse
    print('Hi ', end='')
    i += 1
print()

# Activity 5: Sum 100
