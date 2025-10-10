# pyramid pattern
# step by step guide
# row 0: 4 spaces, 1 star
# row 1: 3 spaces, 3 star
# row 2: 2 spaces, 5 star
# row 3: 1 spaces, 7 star
# row 4: 0 spaces, 9 star

rows = 5

#Step 1: create an outer loop for the row 
for i in range(rows):
    
#Step 2: print the spaces(rows - i - 1)
    for j in range(rows - i - 1):
        print(' ', end='') #end give spaces on the same line

#Step 3: print the stars (2 * i + 1)
    for k in range(2 * i + 1):
        print('*', end='')
        
#Step 4: print a new line
    print()