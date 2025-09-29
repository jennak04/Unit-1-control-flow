text = "Hello World"
vowel_count = 0

# for char in text:
   # if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char =="U":
       # print(f"{char} contains a vowel")
        
  #  else:
       # print(f"{char} does not contain a vowel")
       
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{text}': {vowel_count}")

print("")

text = "ABC123xyz"
for i in range(len(text)):
    if '0' <= text[i] <= '9':
        print(f"Digit at position {i}: {text[i]}")
        
print("")

word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")