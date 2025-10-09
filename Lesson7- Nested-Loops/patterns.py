# pyramid pattern
# step by step guide
# row 0: 4 spaces, 1 star
# row 1: 3 spaces, 3 star
# row 2: 2 spaces, 5 star
# row 3: 1 spaces, 7 star
# row 4: 0 spaces, 9 star

rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')

    for k in range(2 * i + 1):
        print('*', end='')

    print()