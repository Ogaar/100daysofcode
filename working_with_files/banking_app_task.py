import os
import pandas
import random
import ast
from datetime import datetime

# Define login function
def login():
    password = "test"
    login_option = input("Enter one of 2 options:\n 1. Login\n 2. Quit\n")
    if login_option == "1":
        password_entry = input("Enter the password:\n")
        if password_entry == password:
            print("You have successfully logged in.\n")
        else:
            print("The password you have entered is incorrect. Going back to login menu...")
            main()
    elif login_option == "2":
        print("Exiting...")
        exit()
    else:
        print("That isn't one of the options. Try again:")
        main()


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
    elif loggedin_option == "3":
        query_loan_id(loans)
    elif loggedin_option == "4":
        branch_information(loans)
    elif loggedin_option == "5":
        show_birthdays(loans)
    elif loggedin_option == "0":
        print("Exiting back to login menu...")
        main()
    else:
        print("That isn't one of the options. Try again:")
        loggedin_main_menu(loans)

def show_all_loans(loans):
    loan_columns = ["Loan ID", "First Name", "Middle Name Initial", "Last Name", "Branch Code",
                    "Gender (F/M)", "Date of Birth (mm/dd/yyyy)", "Loan Amount", "Customer Phone Number", "Pass Code"]
    print(pandas.DataFrame(data = loans, columns = loan_columns).to_string(index = False).replace(r"\n",""))
    print("Back to login menu,,,")
    main()

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
        print("Going back to login menu...")
        main()

def query_loan_id(loans):
    loan_id_option = input("Enter the loan ID you wish to query:\n")
    possible_options = []
    for loan in loans:
        possible_options.append(loan[0])
    if loan_id_option not in possible_options:
        print("That is not a valid loan ID.")
        query_loan_id(loans)
    else:
        for loan in loans:
            if loan_id_option == loan[0]:
                id_password = loan[9].encode().decode('unicode-escape')
                id_password = id_password[:-1]
                first_name = loan[1]
                middle_name_initial = loan[2]
                last_name = loan[3]
                branch_code = loan[4]
                gender = loan[5]
                date_of_birth = loan[6]
                loan_amount = loan[7]
                phone_number = loan[8]
        random_generations = rng_checker(id_password)
        sorted_random_generations = sorted(random_generations)

        password_character_1 = input("Please enter character {} of your password:\n"
                                     .format(sorted_random_generations[0] + 1))
        if password_character_1 != id_password[sorted_random_generations[0]]:
            print("Incorrect character. Back to login menu in case of intruder...")
            main()

        password_character_2 = input("Please enter character {} of your password:\n"
                                     .format(sorted_random_generations[1] + 1))
        if password_character_2 != id_password[sorted_random_generations[1]]:
            print("Incorrect character. Back to login menu in case of intruder...")
            main()

        password_character_3 = input("Please enter character {} of your password:\n"
                                     .format(sorted_random_generations[2] + 1))
        if password_character_3 != id_password[sorted_random_generations[2]]:
            print("Incorrect character. Back to login menu in case of intruder...")
            main()
        print("Pass code accepted.")
        print("Here is the information of {}:".format(loan_id_option))
        print("-----------------------------------")
        print("Customer Name: {} {}. {}".format(first_name, middle_name_initial, last_name))
        print("Branch Code: {}".format(branch_code))
        print("Gender: {}".format(gender))
        print("Date of Birth: {}".format(date_of_birth))
        print("Loan Amount: £{}".format(loan_amount))
        print("Phone Number: {}".format(phone_number))
        print("Back to login menu,,,")
        main()


def rng_checker(id_password):
    random_generations = set()
    while len(random_generations) != 3:
        random_num = random.randint(0,len(id_password))
        random_generations.add(random_num + 1)
    return random_generations

def branch_information(loans):
    loan_amount_dict = {'branch 1': 0, 'branch 2': 0, 'branch 3': 0, 'branch 4': 0}
    average_dict = {'branch 1': 0, 'branch 2': 0, 'branch 3': 0, 'branch 4': 0}

    branch_1_counter = 0
    branch_1_male = 0

    branch_2_counter = 0
    branch_2_male = 0

    branch_3_counter = 0
    branch_3_male = 0

    branch_4_counter = 0
    branch_4_male = 0

    for loan in loans:
        if loan[4] == "1":
            branch_1_counter += 1
            loan_amount_dict['branch 1'] += int(loan[7])
            if loan[5] == "M":
                branch_1_male += 1

        if loan[4] == "2":
            branch_2_counter += 1
            loan_amount_dict['branch 2'] += int(loan[7])
            if loan[5] == "M":
                branch_2_male += 1

        if loan[4] == "3":
            branch_3_counter += 1
            loan_amount_dict['branch 3'] += int(loan[7])
            if loan[5] == "M":
                branch_3_male += 1

        if loan[4] == "4":
            branch_4_counter += 1
            loan_amount_dict['branch 4'] += int(loan[7])
            if loan[5] == "M":
                branch_4_male += 1

    branch_1_female = branch_1_counter - branch_1_male
    average_dict['branch 1'] = loan_amount_dict['branch 1'] / branch_1_counter
    branch_1_male_percentage = (branch_1_male/branch_1_counter) * 100
    branch_1_female_percentage = (branch_1_female/branch_1_counter) * 100

    branch_2_female = branch_2_counter - branch_2_male
    average_dict['branch 2'] = loan_amount_dict['branch 2'] / branch_2_counter
    branch_2_male_percentage = (branch_2_male / branch_2_counter) * 100
    branch_2_female_percentage = (branch_2_female / branch_2_counter) * 100

    branch_3_female = branch_3_counter - branch_3_male
    average_dict['branch 3'] = loan_amount_dict['branch 3'] / branch_3_counter
    branch_3_male_percentage = (branch_3_male / branch_3_counter) * 100
    branch_3_female_percentage = (branch_3_female / branch_3_counter) * 100

    branch_4_female = branch_4_counter - branch_4_male
    average_dict['branch 4'] = loan_amount_dict['branch 4'] / branch_4_counter
    branch_4_male_percentage = (branch_4_male / branch_4_counter) * 100
    branch_4_female_percentage = (branch_4_female / branch_4_counter) * 100

    print("For Branch 1:")
    print("The total loan amount is £{}.".format(loan_amount_dict['branch 1']))
    print("The average loan amount is £{:0.2f}.".format(average_dict['branch 1']))
    print("The percentage of male clients that applied for a loan is: {:0.2f}%.".format(branch_1_male_percentage))
    print("The percentage of female clients that applied for a loan is {:0.2f}%.\n".format(branch_1_female_percentage))

    print("For Branch 2:")
    print("The total loan amount is £{}.".format(loan_amount_dict['branch 2']))
    print("The average loan amount is £{:0.2f}.".format(average_dict['branch 2']))
    print("The percentage of male clients that applied for a loan is: {:0.2f}%.".format(branch_2_male_percentage))
    print("The percentage of female clients that applied for a loan is {:0.2f}%.\n".format(branch_2_female_percentage))

    print("For Branch 3:")
    print("The total loan amount is £{}.".format(loan_amount_dict['branch 3']))
    print("The average loan amount is £{:0.2f}.".format(average_dict['branch 3']))
    print("The percentage of male clients that applied for a loan is: {:0.2f}%.".format(branch_3_male_percentage))
    print("The percentage of female clients that applied for a loan is {:0.2f}%.\n".format(branch_3_female_percentage))

    print("For Branch 4:")
    print("The total loan amount is £{}.".format(loan_amount_dict['branch 4']))
    print("The average loan amount is £{:0.2f}.".format(average_dict['branch 4']))
    print("The percentage of male clients that applied for a loan is: {:0.2f}%.".format(branch_4_male_percentage))
    print("The percentage of female clients that applied for a loan is {:0.2f}%.\n".format(branch_4_female_percentage))
    print("Back to login menu...")
    main()
def show_birthdays(loans):
    current_month = datetime.now().month
    for loan in loans:
        client_dob = datetime.strptime(loan[6], '%m/%d/%Y')
        if current_month == client_dob.month:
            customer_birthday_first_names = loan[1]
            customer_birthday_middle_names = loan[2]
            customer_birthday_last_names = loan[3]
            customer_birthday_dob = loan[6]
            print("{} {}. {} with date of birth: {}".format(customer_birthday_first_names,
                  customer_birthday_middle_names, customer_birthday_last_names, customer_birthday_dob))
    print("Back to login menu...")
    main()
def main():
    login()
    print("Reading CSV file:\n")
    loans = reading_data()
    loggedin_main_menu(loans)

main()
