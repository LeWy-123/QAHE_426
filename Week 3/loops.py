# task and activity 1
# program that print out n times 'remove apple'
print("How many apples should I remove?")
apples = int(input("Enter you how many apples you wanna remove from the box:\nyour answer> "))
while apples > 0:                            # opens a loop that counts backwards instead count up to desired numbers
    print(f'apple removed! {apples} left')   # prints Apple removed every line and tells how many apples left
    apples -= 1                              # decrement the variable when reach 0 it breaks the loop

# Task and activity 2
