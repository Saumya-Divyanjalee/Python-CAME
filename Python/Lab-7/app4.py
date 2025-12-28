print('Augmented Assignment')

# ------------------------
# Simple augmented assignment with integers
# ------------------------
x = 5
x += 8           # equivalent to x = x + 8
print(x)         # Output: 13

y = 2
y **= 3          # equivalent to y = y ** 3
print(y)         # Output: 8

# ------------------------
# List assignment and memory reference
# ------------------------
x = [10, 20, 30]  # x points to a list object in memory
y = x              # y now points to the same list object as x
                    # Both x and y refer to the same memory location

# Using x = x + [40, 50]
x = x + [40, 50]  
# Explanation:
# - x + [40, 50] creates a **new list object** in memory
# - x is updated to point to this new list
# - y still points to the original list ([10, 20, 30])
print(x)  # Output: [10, 20, 30, 40, 50] → new list
print(y)  # Output: [10, 20, 30]           → original list

# ------------------------
# Using augmented assignment with lists
# ------------------------
x = [10, 20, 30]
y = x              # y points to the same list as x

x += [40, 50]      # equivalent to x.extend([40, 50])
# Important difference from x = x + [...] :
# - Augmented assignment modifies the list **in-place**
# - x still points to the same memory object
# - y also sees the updated list because both refer to the same object

print(x)           # Output: [10, 20, 30, 40, 50]
print(y)           # Output: [10, 20, 30, 40, 50]

print(x is y)      # Output: True
# Explanation:
# - 'is' checks if two variables point to the **same object**
# - After x += [...], x still points to the original list object
# - So x and y are identical (same memory location)
