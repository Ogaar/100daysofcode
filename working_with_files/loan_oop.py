class Loan:
    def __init__(self, loan_line):
        self.loan_id = loan_line[0]
        self.first_name = loan_line[1]
        self.middle_name_initial = loan_line[2]
        self.last_name = loan_line[3]
        self.branch_code = loan_line[4]
        self.gender = loan_line[5]
        self.date_of_birth = loan_line[6]
        self.loan_amount = loan_line[7]
        self.phone_number = loan_line[8]
        self.password = loan_line[9]

