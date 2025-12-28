print('for Loop')

# ------------------------
# Single-line for loop
# ------------------------
for x in [10, 20, 30, 40, 50]: 
    print(x); print('------------------------')
# Explanation:
# - The semicolon separates two statements on the same line
# - Colon (:) only used once after 'for ... in ...'

# ------------------------
# Multi-line for loop
# ------------------------
for x in [10, 20, 30, 40, 50]:
    print(x)                # prints current element
    print('------------------------')  # prints separator

# ------------------------
# For-Else with a non-empty iterable
# ------------------------
for char in "Hello":
    print(char)             # prints each character
else:
    print('Nothing to iterate')  
# Explanation:
# - 'else' block executes only if the loop **completes normally** (not broken by break)
# - Here, loop iterates all characters, so else executes after finishing

# ------------------------
# For-Else with an empty iterable
# ------------------------
for y in {}:
    print(y)                # no iteration occurs because dictionary is empty
else:
    print('Nothing to print here')
# Explanation:
# - Iterable is empty → for-loop body does NOT execute
# - Else block **still executes** because loop did NOT encounter a break
