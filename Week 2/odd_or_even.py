def odd_or_even():
    number = int(input("Enter a number please: "))

    if number % 2 == 0:
        print(f"{number} was Even")
    else:
        print(f"{number} was Odd")

def which_is_the_greater():
    print("Please enter the first number please: ")
    first_number = int(input("first number: >"))
    print("Please enter the second number please: ")
    second_number = int(input("second number: >"))


    if first_number > second_number:
        print(f"{first_number} was greaterst!")
    elif first_number < second_number:
        print(f"{second_number} was greaterst!")
    else:
        print(f"The two numbers were equal. {first_number} = {second_number}")

