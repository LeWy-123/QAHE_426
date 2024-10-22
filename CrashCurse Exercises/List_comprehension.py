
# for loop to count up to 20
for i in range(0, 21):
    print(f"Number: {i}")

print("--------- Exercise 1 ended ---------")

one_million_numbers = [value for value in range(1, 1_000_001)]
#for number in one_million_numbers:
#    print(f"Number: {number}")

print("--------- Exercise 2 ended ---------")

print("Sum: ", sum(one_million_numbers))
print("Min: ", min(one_million_numbers))
print("Max: ", max(one_million_numbers))

print("--------- Exercise 3 ended ---------")

odd_list = [ value for value in range(0, 21, 3)]
print(*(f'this is an odd number: {x}' for x in odd_list), sep='\n')

print("--------- Exercise 4 ended ---------")

multi_tree = [value*3 for value in range(1, 11)]
print(multi_tree)
print(*(f"Multiplies of tree: {x}" for x in multi_tree), sep='\n')

print("--------- Exercise 5 ended ---------")

cubes = [value**3 for value in range(0, 11)]
j = 0
for i in cubes:
    print(f"Cube of {j} is {i}")
    j += 1

print("--------- Exercise 6 ended ---------")
twod_array = [[0 for i in range(10)] for j in range(2)]

print(twod_array, sep='\n\n', end='\n')