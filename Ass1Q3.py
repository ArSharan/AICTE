def calculate_result(name, marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    
    if average >= 75:
        result = "Distinction"
    elif average >= 60:
        result = "First class"
    elif average >= 50:
        result = "Second class"
    elif average >= 35:
        result = "Third class"
    else:
        result = "Fail"
    
    return total_marks, average, result

student_number = input("Enter student number: ")
student_name = input("Enter student name: ")
marks = []
for i in range(3):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))


total_marks, average, result = calculate_result(student_name, marks)

print("\nStudent Result")
print("Student Number:", student_number)
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average)
print("Result:", result)
