import random, math
s=0
c=0

for i in range(101):
    y=3*random.random()+2
    s=s+y
    k=s/100

    result = [k]
K = [k]
for k in K:
    d = (y-k)**2
    c=c+d
m = math.sqrt(c/100)
print(k, "+-", m)