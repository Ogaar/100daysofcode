# Import necessary commands from package
from statistics import mean
import os

# Define function to extract list from Notepad and be used when generating a list
def list_sorter(location_of_file, name_of_file):
    # Convert notepad list into string list
    if name_of_file.endswith(".txt"):
        empty_file = open(location_of_file + name_of_file, mode = "r")
    else:
        empty_file = open(location_of_file + name_of_file + ".txt", mode = "r")
    string_of_num_list = empty_file.read()
    real_num_list = string_of_num_list.split(",")

    # Use a for loop to turn string list into integer list
    for i in range(0,len(real_num_list)):
        try:
            real_num_list[i] = int(real_num_list[i])
        except Exception as e:
            print("We skipped '" + real_num_list[i] + "' because it is not an integer.")
            real_num_list.remove(real_num_list[i])
            continue

    # Work out the mean, max and min of the list
    mean_of_real_num_list = mean(real_num_list)
    maximum_of_real_num_list = max(real_num_list)
    minimum_of_real_num_list = min(real_num_list)

    # Display nicely
    print("The mean of this list is " + str(mean_of_real_num_list)+ ".")
    print("The minimum of this list is " + str(minimum_of_real_num_list) + ".")
    print("The maximum of this list is " + str(maximum_of_real_num_list) + ".")
