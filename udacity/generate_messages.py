names = input("Enter name of students separated by commas:")
names = names.split(",")
names = [name.title() for name in names]
assignments = input("Enter assignment counts separated by commas:")
assignments = assignments.split(",")
grades = input("Enter grade of students separated by commas:")
grades = grades.split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    maximum_grade = int(grade) + (int(assignment) * 2)
    print(message.format(name, assignment, grade, str(maximum_grade)))