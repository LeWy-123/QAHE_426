# Activity 1
def book_type_function():
    book_type = input("What type of book is this? ")
    if book_type == "adventure":
        print("I like adventure books")
    else:
        print(f"I don't like {book_type} books")

    print("Finished reading books")

# Activity 2
def activity_function():
    activity = input("Please enter activity to be performed: ")
    if activity == "calculate":
        print("Performing calculations")
    else:
        print(f"Performing {activity}")

    print("Activity completed")

# Activity 3
def robot_directions():
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

# Activity 4
