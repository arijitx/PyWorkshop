# taking input
m1 = float(input())
m2 = float(input())
r = float(input())

# initialize constant
G = 6.674

# grams to kgs
m1 = m1/1000.
m2 = m2/1000.

# feet to meters
r = r*0.3048

# calculate force
f = G*(m1*m2)/r

# print results
print("%.10f" % f)
