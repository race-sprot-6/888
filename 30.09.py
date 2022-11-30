l = [3,9,1,20,10,5]
for i in range(len(l)-1):
    for j in range(0,i):
        for x in range(len(j),0)
            if l[j]<l[j-1]:
                t = l[j]
                l[j] = l[j-1]
                l[j-1] = t
            #c = l[i]
            #l[i] = l[i-1]
            #l[i-1] =c


            else:
                l[j] = l[j]
print(l)