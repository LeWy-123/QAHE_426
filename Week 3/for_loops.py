# Activity 1: Simple Loop
print('How many mountains should I display?')
mountains = int(input('amount> '))
i = 0
mountain_ascii = """      __ 
     /  \\_
    /^    \\
   / ^     \\_
 _/ ^ ^     ^\\
/ ^       ^   \\"""                         # large ASCII art stored in a variable for cleaner code

print('Displaying...')
for i in range(mountains):
    print(mountain_ascii)
    i += 1

print('Done!')

# Activity 2: Count Down

print('How far we from the target?')
target = int(input('amount> '))             # promoting the user
for i in range(target, 0, -1):              # for loop to count downwards
    print(f'{i} steps remaining')           # printing to the terminal

print('Target archived!')

# Activity 3: Range
print('what level of brightness is required?')
brightness = int(input('amount> '))         # promoting the user for the brighness level


print('\nAdjusting brightness...\n')

for i in range(0, brightness, 2):
    print(f'Brightness level: {"*"*i}')

# Activity 4: Characters
print("What word do you see?")
user_word =input()

print('Displaying index positions...')
for position in range(0, len(user_word)):
    print(f'index: {position}:', user_word[position])

print('Done!')