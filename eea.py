import math
a = 143
b = 7
r = [a,b]
x = y = [0,1]
i = 0
q = []
while r[i] != 0:
    i = i + 1
    q.append(math.ceil(r[i-2]/r[i-1]))
    r.append(r[i-2]-q[i]*r[i-1])
    x.append(x[i-2]-q[i]*x[i-1])
    y.append(y[i-2]-q[i]*y[i-1])

print("d = " + str(r[i-1]))
print("x = " + str(x[i-1]))
print("y = " + str(y[i-1]))