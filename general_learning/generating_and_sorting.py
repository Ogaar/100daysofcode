# Import needed packages.
import random
import sorting_a_list

def main():
    # Generate an empty text file with user inputted name.
    name_of_file = input("What do you want to call your text file? (no spaces) \n")
    location_of_file = input("Where do you want your text file to be located? (with slash at end) \n")
    if name_of_file.endswith(".txt"):
        empty_file = open(location_of_file + name_of_file, mode = "w+")
    else:
        empty_file = open(location_of_file + name_of_file + ".txt", mode = "w+")

    # User inputted boundaries.
    number_of_nums = int_checker("How many numbers do you want written in your text file? \n")
    min_number = int_checker("What is your lower bound for a number to be generated? \n")
    max_number = int_checker("What is your lower bound for a number to be generated? \n")

    dummy_variable = 0

    # If the user inputted a max number smaller than the minimum number, it swaps them.
    if max_number < min_number:
        dummy_variable = min_number
        min_number = max_number
        max_number = dummy_variable

    # Generate set amount of random numbers between set boundaries.
    for i in range(0, number_of_nums):
        empty_file.write(str(random.randint(min_number, max_number)) + ",")

    # Use function from other file to sort list
    empty_file.close()
    sorting_a_list.list_sorter(location_of_file, name_of_file)

# Define a function that checks if a value is an integer and doesn't let you continue unless it is.
def int_checker(user_question):
    while True:
        try:
            return_value = int(input(user_question))
            break
        except Exception:
            print("That isn't an integer. Try again! \n")
    return return_value


main()
