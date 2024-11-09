# 7-1 Rental Car
rent_car = input("What car would you like to rent?: ")
print(f'Let me see if I can find you a {rent_car}.')

# 7-2 Restaurant Seating
dinner_group = int(input('How manny people in your dinner group? '))
if dinner_group > 8: print('You have to wait for the table!')
else: print('Your table is ready')

# 7-3 Multiples of Ten
numbers = int(input('multiplies of 10? '))
if numbers % 10 == 0:
    print(f'Your number {numbers} is multiplies of 10.')
else:
    print(f'Your number {numbers} is NOT multiplies of 10.')

