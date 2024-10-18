def book_type_function():
    book_type = input("What type of book is this? ")
    if book_type == "adventure":
        print("I like adventure books")
    else:
        print(f"I don't like {book_type} books")

    print("Finished reading books")

def activity_function():
    activity = input("Please enter avtivity to be performed: ")
    if activity == "calculate":
        print("Performing calculations")
    else:
        print(f"Performing {activity}")

    print("Activity completed")

activity_function()