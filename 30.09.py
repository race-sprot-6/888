l = [3,9,1,20,10,5]
for i in range(len(l)-1):
    for j in range(0,i):
        while l[i]<l[i-1]:
            t = l[i]
            l[i] = l[i-1]
            l[i-1] = t
            #c = l[i]
            #l[i] = l[i-1]
            #l[i-1] =c

        else:
            l[i] = l[i]
print(l)