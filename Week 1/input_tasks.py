# Activity 1
# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# activity 2
print('Please enter a character for the eye -> ', end='')
eye = input()
print('The robots expression is now as follows:\n')
print(f'##########\n'
      f'#  {eye}  {eye}  #\n'
      f'#  ----  #\n'
      f'##########\n')

# Activity 3
print("What is your name?")
name = input()

print(f'How old are you (in years)?')
age = input()
print(f'How tall are you (in centimeters)?')
height = (int(input()) ** 2) / 10000
print(f'How much do you weigh? (in kilograms)')
weight = int(input())

print(f'Dear {name} you are {age} years old and your BMI is {weight/height}.')

# Activity 4: String operator
print('Please enter the number of lives.')
lives = int(input())
print('Please enter the energy level.')
energy_level = int(input())
print('Please enter the shield level.')
shield_level = int(input())
print('\nHealth has been set.\n')
print(f'Lives: {"♥"*lives}')
print(f'Energy level: {"✭"*energy_level}')
print(f'Shield level: {"Θ"*shield_level}')