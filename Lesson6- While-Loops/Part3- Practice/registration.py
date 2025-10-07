print("\n= User Registration = \n")

# username
while True:

    username = input("Enter a username: ")

    if len(username) < 3:
        print("Too short! Minimum 3 characters")
        continue

    elif len(username) > 15:
        print("Too long! Maximum 15 characters")
        continue

    has_space = False
    for char in username:
        if char == " ":
            has_space = True
            break

    if has_space:
        print("No spaces allowed")
        continue

    print("Username accepted")
    break

# password

while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Too short! Min length 8 characters")
        continue

    has_digit = False
    has_upper = False

    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
        if "0" <= char <= "9":
            has_digit = True

    if not has_digit: #if has_digit is false
        print("Requires at least 1 digit")
        continue

    if not has_upper:
        print("Requires at least 1 uppercase letter")
        continue


    print("Password accepted")
    break

# age
while True:
    age_input = input("Enter your age: ")
    
    if not age_input.isdigit():
        print("Age must be a number")
        continue
    
    age = int(age_input)
    
    if age < 13:
        print("You must be at least 13 years old")
        continue
    
    if age > 120:
        print("Please enter a valid age (120 or less)")
        continue
        
    print("AGe accepted")
    break

# confirmation

while True:
  confirmation = input("Confirm registration? (yes/no): ").lower()

  if confirmation == "yes" or confirmation == "y":
        print("Registration successful")
        print(f"Welcome {username}")
        break 

  elif confirmation == "no" or confirmation == "n":
        print("Registration cancelled")
        break  

  else:
        print("Please enter yes or no")