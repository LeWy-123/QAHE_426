buffet = ('Beef burger', 'Pizza', 'Fish and chips', 'Chicken wings', 'brownie')
for food in buffet:
    print(food)

print("\n---Menu changed---")
buffet = *buffet[:-2], 'Snack', 'waffle with icecream'

for food in buffet:
    print(food)
