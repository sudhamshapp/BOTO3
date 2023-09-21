marks = [90, 89, 99, 95, 98, 93]
def find_average_marks_of_a_student():
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    find_average_marks = sum_of_marks/total_subjects
    return find_average_marks
result = find_average_marks_of_a_student()
print(result)

# calculate the grade and return it
def calculate_grade(find_average_marks):
    if find_average_marks >= 90:
        return "A"
    elif find_average_marks >= 80:
        return "B"
    elif find_average_marks >= 70:
        return "C"
    elif find_average_marks >= 60:
        return "D"
grade = calculate_grade(result)
print(grade)