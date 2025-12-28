print('Annotation assignment')

# ------------------------
# Simple assignments
# ------------------------
x = 10           # simple assignment, x stores integer 10
x, y = 10, 20    # multiple assignment

# ------------------------
# Annotation assignment (Type Hints)
# ------------------------
# Syntax: identifier : type = expression
# Purpose: provide type information to the interpreter or type checkers
# Python itself does NOT enforce type checking at runtime
# Example:
x: int = 10       # x is hinted as int
z: int = 5.2      # Python allows it at runtime, but type checkers (PyCharm, mypy) will warn
y: str = "abc"    # y hinted as str
a: float = 2.5    # a hinted as float
b: bool = 5 > 2   # b hinted as bool, value True

# ------------------------
# Printing values and types
# ------------------------
# Issue in original code:
# You wrote type[x] → wrong syntax
# Correct way to get type of a variable: type(x)

print(x, type(x))  # Output: 10 <class 'int'>
print(z, type(z))  # Output: 5.2 <class 'float'>  (Python runtime ignores type hint)
print(y, type(y))  # Output: abc <class 'str'>
print(a, type(a))  # Output: 2.5 <class 'float'>
print(b, type(b))  # Output: True <class 'bool'>


# ------------------------
# Chain Assignment
# ------------------------

# Syntax: variable1 = variable2 = variable3 = value
# Purpose: assign the same value to multiple variables in a single statement

m = n = w = 15  # 15 is assigned to w first, then n gets the same reference, then m
                 # All three variables now refer to the same immutable integer object 15

# Printing values
print(m, n, w)  # Output: 15 15 15
