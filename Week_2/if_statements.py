# Activity 1
def book_type_function():           # declaring a new function
    book_type = input("What type of book is this? ")
    if book_type == "adventure":    # asking user for an input and evaluates and prints I like adventure books if
        print("I like adventure books")  # user chooses adventure. slightly different code than task asked to do
    else:
        print(f"I don't like {book_type} books")

    print("Finished reading books")

# Activity 2
def activity_function():            # creating a new function which prints performing activity or calculate
    activity = input("Please enter activity to be performed: ")
    if activity == "calculate":
        print("Performing calculations")
    else:
        print(f"Performing {activity}")

    print("Activity completed")     # This print function executed at the end of the function

# Activity 3
def robot_directions():
    # prompt the user for a direction
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
    # checks whether a number even or odd based on the user's input
    if number % 2 == 0:
        print(f"{number} was Even")
    else:
        print(f"{number} was Odd")

# Activity 5: Comparison Operators
def which_is_the_greater():         # function tells the user which number was greater
    print("Please enter the first number please: ")
    first_number = int(input("first number: >"))
    print("Please enter the second number please: ")
    second_number = int(input("second number: >"))
    # if statements for comparing values
    if first_number > second_number:
        print(f"{first_number} was greatest!")
    elif first_number < second_number:
        print(f"{second_number} was greatest!")
    else:
        print(f"The two numbers were equal. {first_number} = {second_number}")

# Activity 6: Counter
def which_is_the_greater(loop_length=5, i = 0):     # custom-made function which counts odd or even numbers
    even_counter = 0                                # defining the variables storing the values
    odd_counter = 0
    while i < loop_length:                          # starting the loop based on the argument given/passed-to.
        input_number = int(input(f"No: {i} - Enter a number: "))    # repeatedly prompt the user for a number based on
        if input_number % 2 == 0:                                   # loop_length parameter
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
