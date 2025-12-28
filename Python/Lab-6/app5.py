class MyUtil:
    # Class variables
    PI = 3.14
    TEXT = 'CAME'

    # Class body should only contain definitions
    # No direct reference to class name here


# Access class variables AFTER class definition
print(MyUtil.PI)     # 3.14
print(MyUtil.TEXT)   # CAME
# print(MyUtil.TEST) #  AttributeError (TEST not defined)
