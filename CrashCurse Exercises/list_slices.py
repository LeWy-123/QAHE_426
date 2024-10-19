# list exercises with slices

my_list = [1, "Foo", "bar", "BMW", 7, 3.14, "Love", 90]

print(*(f"The first three items in the list are: {my_list[:3]}"), sep="")
print(*(f"Three items from the middle of the list are: {my_list[(int(len(my_list)/-2)):(int(len(my_list)/2)+3)]}"), sep="")
print(f"The last three items in the list are: {my_list[-3:]}", end="\n")

friends_pizza = ['pizza', 'ice cream', 'falafel', 'carrot cake', 'cannoli', 'nutts']
my_pizza = friends_pizza[:]
print(*(f"The foods on the list: {friends_food}" for friends_food in friends_pizza), sep='\n')