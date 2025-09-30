uppercase_letters = 0
lowercase_letters = 0
digits = 0
special_characters = 0
letter_count = 0
sequence = False
repeat_chars = False


user_password = input("Enter a password: ")

for char in user_password:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
    
    if 'A' <= char <= 'Z':
        uppercase_letters += 1
    
    elif 'a' <= char <= 'z':
        lowercase_letters += 1
        
    elif '0' <= char <= '9':
        digits += 1
        
    else: 
        special_characters += 1
       

print("PASSWORD ANALYSIS:")
print("=" * 40)
print(f"Password: '{user_password}'")

print("")

print("CHARACTER COUNTS: ")
print(f"Length: {letter_count}")
print(f"Uppercase letters: {uppercase_letters}")
print(f"Lowercase letters: {lowercase_letters}")
print(f"Digits: {digits}")
print(f"Special characters: {special_characters}")

print("")

print("REQUIREMENT CHECK")

print(f"Length (8+ characters): {'PASSED' if len(user_password) > 8 else 'FAILED'}")
print(f"Uppercase letters: {'PASSED' if uppercase_letters > 0 else 'FAILED'}")
print(f"Lowercase letters: {'PASSED' if lowercase_letters > 0 else 'FAILED'}")
print(f"Digits: {'PASSED' if digits > 0 else 'FAILED'}")
print(f"Special Characters: {'PASSED' if special_characters > 0 else 'FAILED'}")

print("")
print("SECURITY ISSUES")
for i in range(len(user_password) - 2):
    if (ord(user_password[i+1]) == ord(user_password[i]) + 1 and
        ord(user_password[i+2]) == ord(user_password[i]) + 2):
        sequence = True
        print(f"Contains sequence: {user_password[i:i+3]}")
        break

if not sequence:
    print("Does not contain sequence")

for i in range(len(user_password) - 2):
    if user_password[i] == user_password[i+1] == user_password[i+2]:
        repeat_chars = True
        print(f"Repeated Characters: {user_password[i]}")
        break

if not repeat_chars:
    print("No Repeated Characters")

if (len(user_password) > 8 and
    uppercase_letters > 0 and
    lowercase_letters > 0 and
    digits > 0 and
    special_characters > 0 and
    not sequence and
    not repeat_chars):
    rating = "STRONG"
elif (len(user_password) < 8 and (sequence or repeat_chars)):
    rating = "WEAK"
else:
    rating = "MEDIUM"

print(f"FINAL RATING: {rating}")

