# ------------------------
# Augmented Assignment / Compound Assignment
# ------------------------

# 1. Simple assignment
x = 5            # x = 5

# 2. Augmented assignment combines a binary operation with assignment
x += 2           # equivalent to x = x + 2
print(x)         # Output: 7

# Syntax:
# identifier (operator)= expression
# Examples:
x -= 3           # equivalent to x = x - 3
print(x)         # Output: 4

x *= 2           # equivalent to x = x * 2
print(x)         # Output: 8

x /= 4           # equivalent to x = x / 4
print(x)         # Output: 2.0

x %= 2           # equivalent to x = x % 2
print(x)         # Output: 0.0

x **= 3          # equivalent to x = x ** 3
print(x)         # Output: 0.0

# ------------------------
# Important Notes
# ------------------------

# 1. Only binary operators can be used with augmented assignment
# Valid binary operators include: +, -, *, /, //, %, **, &, |, ^, <<, >>, @
y = 2
y **= 3         # equivalent to y = y ** 3
print(y)        # Output: 8

# 2. Augmented assignment is just shorthand
# Example: x = x + 3  → x += 3

# 3. Works with mutable objects as well
lst = [1, 2, 3]
lst += [4, 5]   # equivalent to lst = lst + [4, 5]
print(lst)      # Output: [1, 2, 3, 4, 5]

# 4. Works with strings
s = "Hello"
s += " World"
print(s)        # Output: "Hello World"

# ------------------------
# Rewriting expressions without augmented assignment
# ------------------------

x = 2
x = x + 2       # equivalent to x += 2
print(x)        # Output: 4

x = 2 
x += 2 
print(x)        # Output: 4

y = 2
y = y ** 2      # equivalent to y **= 2
print(y)        # Output: 4

y = 2
y = y - 2       # equivalent to y -= 2
print(y)        # Output: 0

y = 2
y -= 2
print(y)        # Output: 0

# ------------------------
# Invalid operations explanation
# ------------------------

# Python does NOT support these:
# y = y ~ 2  #  SyntaxError: invalid syntax
# y ~= 2     #  SyntaxError: invalid syntax

# Explanation:
# - '~' is a unary bitwise NOT operator, cannot combine with '=' like '~='
# - Python has no operator called '~='
# Correct usage of '~':
y = 2
y = ~y       # bitwise NOT, flips all bits
print(y)     # Output: -3 (in 2's complement)

# ------------------------
# Boolean expression assignment
# ------------------------
y = 2
y = y > 2       # evaluates boolean expression, assigns True/False
print(y)        # Output: False

# ------------------------
# Expression statement example
# ------------------------
y = 2
y >= 2          # This is a comparison expression, evaluated but not assigned
print(y)        # Output: 2
# Explanation:
# - 'y >= 2' evaluates to True but is NOT assigned to y
# - Python treats it as an "expression statement" and discards the result

# ------------------------
# Logical operation assignment
# ------------------------
y = 2
y = y and 2     # Logical AND, assigns the result to y
print(y)        # Output: 2
# Explanation:
# - 'y and 2' returns the second operand if the first is truthy
# - Result is assigned back to y
