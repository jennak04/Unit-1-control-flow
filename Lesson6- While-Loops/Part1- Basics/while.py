# while loop that counts down from 5

'''
initilizae variable
while condition(test variable)

'''

num = 5

while num >= 1:
    print(num)
    num -= 1

print("Blast off!")


print("")
# sum numbers 1 to 10
num = 1
sum = 0

#while num <= 10:
   # sum += num #(total = total + num)
   # num += 1

#print(f"SUM of numbers 1-10: {sum}")

while num <= 10:
    sum += num
    if num < 10:
        print(num, end="+")
    else:
        print(num, end="=")
    num += 1
print(sum)
print()
    
# Sum of digits
# take a user input as int, and sum the digits of it

user_num = input("Enter a number: ") #1234
sum = 0
#for char in user_num:
   # print(f"{char} {type(char)}")
   # sum += int(char)

#print(f"\nTotal {sum}")

i=0
while i < len(user_num):
    sum += int(user_num[i])
    i += 1
print(sum)
    
    

    