# prompt the user for direction
direction = input("Towards which direction should I go (up, down, left, right): ")

# If statements for branching
if direction == "up":
    print("I am moving in upward direction")
elif direction == "down":
    print("I am moving in downward direction")
elif direction == "left":
    print("I am moving in left direction")
elif direction == "right":
    print("I am moving in right direction")
else:
    print("Invalid direction")
