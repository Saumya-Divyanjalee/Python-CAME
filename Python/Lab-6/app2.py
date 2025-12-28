#f(x) = x ** 2 + 2x + 1
y = lambda x: x ** 2 + 2 * x + 1
print(y)
print(y(5))#call expression y(5)

#f(x,y) = x**2 - y**2
y = lambda x,y: x ** 2 - y ** 2
print(y(5,3))
print(y(10,4))
print(y(2,5))

# (lambda a,b,c : a+b+c)(10,20,30)
y = (lambda a,b,c : a+b+c)(10,20,30)
print(y)

y = lambda a=2,b=3: a**2 + b**2#using default values
print(y())
print(y(3))
print(y(b=10))#b assign valuew 10
print(y(3,4))

x = 3
print(x:=(lambda x,y:x-y)(y=x,x=(3,4))+5+x)
# x = 3
# print(x := (lambda x, y, : x - y)(y = x, x = (3, 4)) + 5)

a = 2
print( (lambda a, b=4: a*2 - b)(b=a, a=a)+(lambda x: x(2)(lambda y: y**2)))

