# Printing a range object
print(range(5))
# Output: range(0, 5)
# Explanation:
# - range(5) creates a range object from 0 to 4
# - It does NOT print numbers directly, only the range description


# Iterating over range(5)
for x in range(5):
    print(x, end="")
# Output: 01234
# Explanation:
# - range(5) generates numbers: 0, 1, 2, 3, 4
# - end="" keeps all output on the same line

print()  # move to next line


# Printing a range with start and end
print(range(5, 10))
# Output: range(5, 10)
# Explanation:
# - range(5, 10) generates numbers from 5 to 9


# Iterating over range(5, 10)
for x in range(5, 10):
    print(str(x) + ".", end="")
# Output: 5.6.7.8.9.
# Explanation:
# - Converts number to string to concatenate "."
# - end="" prints on the same line

print()  # new line


# Printing a range with start, end, and step
print(range(1, 10, 2))
# Output: range(1, 10, 2)
# Explanation:
# - Starts at 1
# - Stops before 10
# - Step is 2 (skips one number each time)


# Iterating over range(1, 10, 2)
for x in range(1, 10, 2):
    print(str(x) + ".", end="")
# Output: 1.3.5.7.9.
# Explanation:
# - Numbers increase by 2 each time

print()  # new line
