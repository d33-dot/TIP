import math

strange=[[],1]
print(type(strange))

for x in range(2):
    for y in range(2):
        if (x or y) and ((not x) or y) and not(x and y):
            print(x,y)

a = [3,5,6,7]
print(a[::-1])

a = int(input('хартли '))
print(math.log(a,2))

b = float(input('шеннон 1 '))
c = float(input('шеннон 2 '))
def f(x):
    return -x*math.log(x,2)
b= f(b)
c = f(c)
print(b,c,b+c)

x = float(input(''))
print( (math.tan( (math.cos(x)*math.sin(2*x))/x*math.exp(x) ))**math.log(x,7) )

y = int(input('байт '))
if str(y).count('1')%2==0:
    print(str(y)+'0')
else: print(str(y)+'1')