# Assignment Statements
# ---------------------
# Syntax: identifier = expression
# The expression is evaluated first, then the result is assigned to the variable

# ---------------------
# 1. Simple assignment
x = 10 + 5           # 10+5 = 15 assigned to x
print(x)             # Output: 15

# ---------------------
# 2. Multiple assignment (unpacking)
a, b, c = 10, 20, 30  # three variables matched to three values
print(a, b, c)         # Output: 10 20 30

print('-----------------')

# 3. Tuple unpacking
a, b = (10, 20)
print(a, b)             # Output: 10 20

print('-----------------')

# 4. Parentheses optional with tuple unpacking
(a, b) = (50, 60)
print(a, b)             # Output: 50 60

print('-----------------')

# 5. List unpacking
[x, y] = [10, 20]
print(x, y)             # Output: 10 20

print('-----------------')

# 6. Another tuple unpacking example
(m, n) = (30, 40)
print(m, n)             # Output: 30 40

print('-----------------')

# ---------------------
# 7. Usage with a list
a = [10, 20, 30, 40, 50]  # 'a' is a packed structure (list)

# Unpacking: number of variables must match number of values
# [b, c] = a  #  This would raise ValueError: too many values to unpack

# Correct unpacking
[b, c, d, e, f] = a
# Print selected variables
# If you want to skip a variable, use '_' as placeholder
print(b, c, e, f)       # Output: 10 20 40 50
