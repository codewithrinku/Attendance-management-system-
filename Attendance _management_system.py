import csv

print("\t\t\tWelcome to the Student Result Generator\n\n")
print("""Note: This application helps you generate student results easily.
If you are not comfortable working with Excel, this tool is for you.
Just enter the student names and their subject marks, and it will automatically
calculate total marks, average, percentage, grade, division, and save everything in a CSV file.\n""")

data = []

# Input: Total number of students
while True:
    try:
        number = int(input("Enter the number of students to store in Excel: "))
        break
    except ValueError:
        print("❌ Please enter integer numbers only.")

# Input data for each student
for i in range(1, number + 1):
    print(f"\nEnter details for Student {i}")
    name = input("Enter Student Name: ").title()
    clas = input("Enter Class: ")

    # Function to get integer input with validation
    def get_int_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Please enter integer numbers only.")

    roll_number = get_int_input("Enter Roll Number: ")
    hindi = get_int_input("Enter Hindi Marks: ")
    english = get_int_input("Enter English Marks: ")
    math = get_int_input("Enter Math Marks: ")
    physics = get_int_input("Enter Physics Marks: ")
    chemistry = get_int_input("Enter Chemistry Marks: ")

    total = hindi + english + math + physics + chemistry
    average = total / 5
    percentage = round((total / 500) * 100, 2)

    # Pass/Fail check
    result = "Pass" if all(subject >= 33 for subject in [hindi, english, math, physics, chemistry]) else "Fail"

    # Grade calculation
    if 33 <= percentage <= 45:
        grade = "C"
    elif 45 < percentage <= 60:
        grade = "B"
    elif 60 < percentage <= 90:
        grade = "A"
    elif 90 < percentage <= 100:
        grade = "A+"
    else:
        grade = "No Grade"

    # Division calculation
    if 33 <= percentage <= 45:
        division = "Third Division"
    elif 45 < percentage <= 60:
        division = "Second Division"
    elif 60 < percentage <= 100:
        division = "First Division"
    else:
        division = "No Division"

    data.append((
        name, clas, roll_number, hindi, english, math,
        physics, chemistry, total, average, percentage,
        result, grade, division
    ))

# Save to CSV file
with open("student_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Name", "Class", "Roll Number", "Hindi", "English", "Math", "Physics", "Chemistry",
        "Total Marks", "Average", "Percentage", "Result", "Grade", "Division"
    ])
    writer.writerows(data)

print("\n✅ Student data has been saved successfully in 'student_data.csv'")
print("🙏 Thank you for using this project!")
