# ------------------------
# Print single stars
# ------------------------
print("*", end="")  # prints star without newline
print("*", end="")  # prints another star on same line
print()             # newline after stars

# ------------------------
# Solid rectangle
# ------------------------
rows = 5
cols = 10
for i in range(rows):
    print("*" * cols)   # prints 10 stars per row

# ------------------------
# Right-Angled Triangle (growing)
# ------------------------
rows = 5
for i in range(1, rows+1):
    print("*" * i)      # prints 1,2,3.. stars per row

# ------------------------
# Inverted Right-Angled Triangle (shrinking)
# ------------------------
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)      # prints 5,4,3.. stars per row

# ------------------------
# Solid square using list [1,2,3,4,5]
# ------------------------
for x in [1,2,3,4,5]:
    for i in [1,2,3,4,5]:
        print("*", end="")
    print()  # newline after each row

# ------------------------
# Right-Angled Triangle using slicing
# ------------------------
for x in [1,2,3,4,5]:
    for i in [1,2,3,4,5][:x]:   # slice controls number of stars
        print("*", end="")
    print()  # newline after each row

# ------------------------
# Inverted Right-Angled Triangle using slicing
# ------------------------
for x in [5,4,3,2,1]:
    for i in [1,2,3,4,5][:x]:   # slice controls number of stars
        print("*", end="")
    print()  # newline after each row

print('---------------------------------')

# Using lists instead of range
rows_list_shrink = [5, 4, 3, 2, 1]   # Shrinking part
rows_list_grow = [2, 3, 4, 5]        # Growing part

# Shrinking part
for i in rows_list_shrink:
    print("*" * i)

# Growing part
for i in rows_list_grow:
    print("*" * i)


for p in range(10):
    for q in range(5-p if p<5 else p+1-5):
        print("*", end=" ")
    print()