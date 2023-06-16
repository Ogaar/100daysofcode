import os
# Define login function
def login():
    password = "test"
    login_option = input("Enter one of 2 options:\n 1. Login\n 2. Quit\n")
    if login_option == "1":
        password_entry = input("Enter the password: ")
        if password_entry == password:
            print("You have successfully logged in.")
        else:
            print("The password you have entered is incorrect. Going back to Main Menu...")
            login()
    elif login_option == "2":
        print("Exiting...")
        exit()
    else:
        print("That isn't one of the options. Try again:")
        login()

def reading_data():
    data = open("C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\working_with_files\\data_project"
                "\\customermortgage.csv", "r")
    loans = data.readlines()
    for line in loans:
        print(line)

def loggedin_main_menu():
    loggedin_option = input("Enter one of 6 options:\n 1. List all loan objects\n 2. Display loans by branch code\n"
                            " 3. Query loan by ID\n 4. Display summary by branch\n 5. Show this month's birthdays\n"
                            " 0. Exit")


def main():
    login()
    print("Reading CSV file:")
    reading_data()
    loggedin_main_menu()











main()