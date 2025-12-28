# Input marks from user
marks = int(input('Enter marks: '))  # input() returns string, int() converts to integer

# Conditional statements to determine grade
if marks >= 75:
    print('Grade: A')
elif marks >= 60:     # marks between 60 and 74
    print('Grade: B')
elif marks >= 50:     # marks between 50 and 59
    print('Grade: C')
elif marks >= 40:     # marks between 40 and 49
    print('Grade: D')
else:                 # marks below 40
    print('Grade: F')


rows = 10
cols = 10

for i in range(rows):print('*' * cols)

 
 
