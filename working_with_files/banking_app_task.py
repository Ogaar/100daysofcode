import os
import pandas

# Define login function
def login():
    password = "test"
    login_option = input("Enter one of 2 options:\n 1. Login\n 2. Quit\n")
    if login_option == "1":
        password_entry = input("Enter the password:\n")
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
    loans = []
    for line in data.readlines():
        loans.append(line.split(','))
    return loans


def loggedin_main_menu(loans):
    loggedin_option = input("Enter one of 6 options:\n 1. List all loan objects\n 2. Display loans by branch code\n"
                            " 3. Query loan by ID\n 4. Display summary by branch\n 5. Show this month's birthdays\n"
                            " 0. Exit\n")
    if loggedin_option == "1":
        show_all_loans(loans)
    elif loggedin_option == "2":
        show_branch_code_loans(loans)
    # elif loggedin_option == "3":
    #
    # elif loggedin_option == "4":
    #
    # elif loggedin_option == "5":
    #
    # elif loggedin_option == "0":
    #     print("Exiting back to login menu...")
    #     login()
    # else:
    #     print("That isn't one of the options. Try again:")
    #     loggedin_main_menu()


def show_all_loans(loans):
    loan_columns = ["Loan ID", "First Name", "Middle Name Initial", "Last Name", "Branch Code",
                    "Gender (F/M)", "Date of Birth (mm/dd/yyyy)", "Loan Amount", "Customer Phone Number", "Pass Code"]
    print(pandas.DataFrame(data = loans, columns = loan_columns).to_string(index = False).replace(r"\n",""))

def show_branch_code_loans(loans):
    branch_code_option = input("Enter the branch code you wish to display loans (1/2/3/4/5):\n")
    possible_options = ["1", "2", "3", "4", "5"]
    if branch_code_option not in possible_options:
        print("That is not a valid branch code.")
        show_branch_code_loans(loans)
    else:
        print("These are the loans of branch " + branch_code_option)
        for loan in loans:
            if loan[4] == branch_code_option:
                print("Loan {} for customer {} {}. {}.".format(loan[0], loan[1], loan[2], loan[3]))

def query_loan_id(loans):
    loan_id_option = input("Enter the loan ID you wish to query:\n")
    possible_options = []
    for loan in loans:
        possible_options.append(loan[0])
    if loan_id_option not in possible_options:
        print("That is not a valid loan ID.")
        query_loan_id(loans)
    else:



def main():
    login()
    print("Reading CSV file:")
    loans = reading_data()
    loggedin_main_menu(loans)


main()
