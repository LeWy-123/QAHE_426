# Activity 1: Nested Decision
# Ask user for book details
print("What type of cover does this book have?")
cover_type = input ()


# Display appropriate message
if cover_type == "soft":
    print("Is the book perfect-bound?")
    perfect_bound = input()
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

# Activity 2: Multiple Nested Decisions
# Start of the program
def look_for_phone():
    print("Where should I look?")
    location = input()

    if location == "in the bedroom":
        print("Where in the bedroom should I look?")
        specific_location = input()
        if specific_location == "under the bed":
            print("Found some shoes but no phone.")
        else:
            print("Found some mess but no phone.")

    elif location == "in the bathroom":
        print("Where in the bathroom should I look?")
        specific_location = input()
        if specific_location == "in the bathtub":
            print("Found a rubber duck but no phone.")
        else:
            print("Found bathroom stuff but no phone.")

    elif location == "in the living room":
        print("Where in the living room should I look?")
        specific_location = input()
        if specific_location == "on the table":
            print("Yes! I found my phone!")
        else:
            print("Found some stuff but no phone.")

    else:
        print("I do not know where that is but I will keep looking.")

# Run the program
look_for_phone()
