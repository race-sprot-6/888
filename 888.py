a = [23,2,822,1,3,7]
for i in range(0,len(a)-1):
    for j in range(0,i):
        if a[j] < a[j+1]:
            a[j] = a[j]
        else:
            for j in range(i,0):
                if a[j] < a[j-1]:
                    c = a[j]
                    a[j] = a[j-1]
                    a[j-1] = c
                    #a[k] = a[k]
                    #for j in range(len(a)-1):
                    #j+1 == j
                else:
                    a[j-1] = a[j-1]

print(a)
