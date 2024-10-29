# Activity 1: Simple Loop
print('How many mountains should I display?')
mountains = int(input('amount> '))
i = 0
mountain_ascii = """      __
     /  \\_
    /^    \\
   / ^     \\_
 _/ ^ ^     ^\\
/ ^       ^   \\"""
print('Displaying...')
for i in range(mountains):
    print(mountain_ascii)
    i += 1

print('Done!')