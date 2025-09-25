# Three forms of range() function
#1 range(stop)

for i in range(5):
    print(i) #prints 0, 1, 2, 3, 4
    
print("")
#2 range(start, stop)

for i in range(3, 8):
    print(i) #prints 3, 4, 5, 6, 7
    
print("")
#3 range(start, stop, step)

for i in range(2, 11, 2):
    print(i) #prints 2, 4, 6, 8, 10
    
    
print("")
    #counting backwards
for i in range(10, 1, -2): #10, 8, 6, 4, 2
     print(i)
     
print("")

#Countdown Timer

import time

for seconds in range(10, -1, -1):
    print(f"{seconds}-seconds")
    time.sleep(0.2) # wait 1 second between numbers
print("BLAST OFF! ")

print("")
#multiplication table
# take user input for number and print the table 
# if the user submitted 5
# 5 x 1 = 5

number = int(input("Enter a number: (1-12) "))

if 1 <= number <= 12:
    for i in range(1, 13):
        result = number * i
        print(f"{number}x{i:2d}={result}")
        
else:
    print("Please eneter a number between 1 and 12")
