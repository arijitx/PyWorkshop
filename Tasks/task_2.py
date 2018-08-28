# import math package
import math

# take inputs
a = int(input())
b = float(input())
c = float(input())
d = float(input())

# init constants
pi = math.pi

# calculate x
x = pi*((math.ceil(b)*math.exp(c))/float(math.factorial(a))) + math.pow(c,d)

# print results
print(x)