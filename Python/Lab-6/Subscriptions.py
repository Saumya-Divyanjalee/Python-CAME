
#Subscription = can pick member,can get values
#String(immutable)
a= "This is a string.It is also a sequence"
#List
b = [10,20,30,40]
#Tuple
c = (1,2,3,4)
#set
d = {5,2,5,1,3}# set not work subscription- no order that reason can't find pick member
#Map
e = {'id':'C001','name':'saumya'}

print(a[2],a[-2])
print(b[2],b[-2])
print(c[2],c[-2])
print(d[2],d[-2])

print(e["id"])#map ,use key


# A normal class without container behavior
class Custom:
    pass

f = Custom()
# f[2]  #  This will cause: TypeError (not subscriptable)


# A class that behaves like a container
class MyClz:
    # __getitem__ is a special (magic) method
    # It allows the object to be accessed using square brackets []
    def __getitem__(self, key):
        # 'key' is whatever is inside the brackets
        # Example: g[2]  → key = 2
        # Example: g[2, 3] → key = (2, 3)
        return 10


# Create an object of MyClz
g = MyClz()

# Subscription expression
# This internally calls: g.__getitem__(2)
print(g[2])        # Output: 10

# You can also pass a list, tuple, etc.
print(g[[2]])      # Output: 10

