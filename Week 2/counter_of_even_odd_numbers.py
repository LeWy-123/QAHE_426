
def which_is_the_greater(loop_lenght=5, i = 0):
    even_counter = 0
    odd_counter = 0
    while i < loop_lenght:
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



which_is_the_greater()