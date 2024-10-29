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
print('Calculating the sum of the first 100 numbers using the sum method...')
hundred_numbers = [n for n in range(1, 101)] # it creates a list with numbers up to 100 from 1. I used list comprehension
print(sum(hundred_numbers))                  # use a sum built-in function to print the sum
print()
i = 1

# using the while loop method
print('Calculating the sum of the first 100 numbers...')
answer = 1                                   # variable that will store the numbers and we do the calculations
while i < 100:                               # this is a while loop runs till reaches 100 after stop running
    answer += i + 1                          # here the answer variable will be added i and 1. this way the numbers are
    print(answer)                            # always ahead by 1 what we add to the answer variable
    i += 1

print(f'...Done! The answer is {answer}')    # the final output should be 5050 but can be changed to add up any numbers

# Activity 6: Sum User Numbers
print('How many numbers should I sum up?')
counting_up = int(input("your answer> "))
i = 1
calc = 0
while i < counting_up:
    print(f'Please enter a number {i} of {counting_up}:')
    summable_number = int(input("your answer> "))
    calc += summable_number
    i += 1

print(f'...Done! The answer is {calc}')