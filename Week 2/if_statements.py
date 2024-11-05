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

# Activity 4 Modulo Operator
def odd_or_even():
    number = int(input("Enter a number please: "))

    if number % 2 == 0:
        print(f"{number} was Even")
    else:
        print(f"{number} was Odd")

# Activity 5: Comparison Operators
def which_is_the_greater():
    print("Please enter the first number please: ")
    first_number = int(input("first number: >"))
    print("Please enter the second number please: ")
    second_number = int(input("second number: >"))

    if first_number > second_number:
        print(f"{first_number} was greatest!")
    elif first_number < second_number:
        print(f"{second_number} was greatest!")
    else:
        print(f"The two numbers were equal. {first_number} = {second_number}")

# Activity 6: Counter
def which_is_the_greater(loop_length=5, i = 0):
    even_counter = 0
    odd_counter = 0
    while i < loop_length:
        input_number = int(input(f"No: {i} - Enter a number: "))
        if input_number % 2 == 0:
            even_counter += 1
            print("One even number added!")
        else:
            odd_counter += 1
            print("One odd number added!")
        i += 1
    print("------------------------------------------------")
    print("The number of even numbers is: ", even_counter)
    print("The number of odd numbers is: ", odd_counter)
    print("------------------------------------------------")
