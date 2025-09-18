# ========================================
# ACCELERATED PYTHON UNIT 2 - LESSON 1
# Conditionals: JavaScript to Python
# ========================================

# ========================================
# SECTION 1: QUICK TRANSLATION CHALLENGE
# ========================================
print("==Grade Classification==")
score = 87
if score >= 90:
    print("A grade!")
elif score >= 80:
    print("B grade!")
else: 
    print("Below B") 
    
# ========================================
# SECTION 2: AGE CATEGORY CLASSIFIER
# ========================================
age_input = input("Enter your age:")

if age_input:
    age = int(age_input)

    if age >= 0 <= 12:
        print("You are a child")
    elif age >= 13 <= 19:
        print("You are a teenager")
    elif age >= 20 <= 64:
        print("You are an adult")
    elif age >= 65:
        print("You are a senior")
    else:
        print("Enter a valid age")

else: 
    print("Enter a valid age")
# ========================================
# SECTION 3: STUDENT STATUS CHECKER
# ========================================

age = 17
gpa = 3.8
has_liscene = True

can_drive = age >= 16 and has_liscene
honor_roll = gpa >= 3.5
eligible = can_drive and honor_roll and age >= 17

print(f"Can drive: {can_drive}")
print(f"Honor roll: {honor_roll}")
print(f"Eligible: {eligible}")




# ========================================
# SECTION 4: GRADE VALIDATOR CHALLENGE
# ========================================


# ========================================
# SECTION 5: WEATHER DECISION SYSTEM
# ========================================
