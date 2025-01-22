school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
attendance_set = set(attendance_list)
missing_classes_students = school.difference(attendance_set)

print('Students who are missing classes are: ', missing_classes_students)

# Shortest way
print('Students who are missing classes are: ', school.difference(attendance_list))