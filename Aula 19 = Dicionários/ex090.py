student_info = dict()
student_info['name'] = str(input("Student's name: "))
student_info['average'] = float(input(f"{student_info['name']}'s average: "))
if student_info['average'] < 7:
    student_info['status'] = 'DISAPPROVED'
else:
    student_info['status'] = 'APPROVED'
print(f"The student's name is {student_info['name']},", end=' ')
print(f"his average is {student_info['average']}", end=' ')
print(f"and the situation is {student_info['status']}")
