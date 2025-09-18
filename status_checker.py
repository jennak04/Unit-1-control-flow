# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()

print("Validity:")
print("========================================")

# TODO: Check if age is valid (between 16 and 100)
has_age = age >= 16 <= 100
if age >= 16 <= 100:
   print("Student has a valid age")
    
else: 
    print("Enter a valid age")

# TODO: Check if GPA is valid (between 0.0 and 4.0)
has_gpa = gpa >= 0.0 <= 4.0
if gpa >= 0.0 <= 4.0:
    print("GPA is valid")

else:
    print("GPA is not valid")

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)

eligibility = gpa >= 2.0 and age >= 18

# TODO: Check voting eligibility (age >= 18)

has_vote = age >= 18

# TODO: Check honor roll status (gpa >= 3.5)

honor_roll = gpa >= 3.5

# eligibility 

print("ELIGIBILITY STATUS:")
print("========================================")

if eligibility:
    print("ELIGIBLE for enrollment")
    
else: 
    print("NOT ELIGIBLE for enrollment")
    
if has_vote:
    print("ELIGIBLE to vote")
    
else:
    print("NOT ELIGIBLE to vote")
    
if honor_roll:
    print("ON HONOR ROLL!")
    
    



