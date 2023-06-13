# Create a dictionary for a student
student = {'name': 'Josh Jenkinson', 'age': 15, 'grade': 3, 'subjects': ['Mathematics', 'Physics', 'Chemistry']}
# Print student's name
print(student['name'])
# Add an item to student called school
student['school'] = 'Uffculme School'
# Print subjects that student is studying, one by one
for i in range(0,len(student['subjects'])):
    print(student['subjects'][i])