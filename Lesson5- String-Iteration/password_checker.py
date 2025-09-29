uppercase_letters = 0
lowercase_letters = 0
digits = 0
special_characters = 0
letter_count = 0


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

rating = ('STRONG' if 'PASSED' else 'WEAK')
print(f"FINAL RATING: {rating}")

