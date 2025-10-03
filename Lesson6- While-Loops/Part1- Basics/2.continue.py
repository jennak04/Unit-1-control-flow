# the continue statement

'''
**continue** - skip to the next iteration!

**difference from break:**
- break exits the loop completely
- continue skips current iteration, keep looping
'''

# example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count) #1, 2, 4, 5