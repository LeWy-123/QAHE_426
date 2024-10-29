# Activity 1: Simple loop
# program that print out n times 'remove apple'
print("How many apples should I remove?")
apples = int(input("Enter you how many apples you wanna remove from the box:\nyour answer> "))
while apples > 0:                            # opens a loop that counts backwards instead count up to desired numbers
    print(f'apple removed! {apples} left')   # prints Apple removed every line and tells how many apples left
    apples -= 1                              # decrement the variable when reach 0 it breaks the loop

# Activity 2: Count
print('How many obstacles must I avoid?')
avoidant = int(input("your answer> "))
obstacles = 0
while avoidant > obstacles:
    print('Avoiding...', end = '')
    obstacles += 1
    print(f'...Done! {obstacles} obstacles avoided!')

print('\nAll obstacles have been avoided.')

