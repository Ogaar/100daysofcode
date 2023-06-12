# Importing package to move file
import os

# Make sure to put this code into nice functions

def move_file_to_folder(file, output_location):
    # Moving the file
    os.rename(file, output_location)

def main():
    # First get location of the files and save them to variables
    file = input("Enter the filepath of the file you want to move:\n")
    output_location = input("Enter the path where you want to move the file and (new) name of the file with the file "
                            "type:\n")
    # Pass the above variables to and call move_file_to_folder
    move_file_to_folder(file, output_location)

main()