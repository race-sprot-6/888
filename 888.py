a = [23,2,822,1,3,8,22,58,5,20,4]
for i in range(0,len(a)-1):
    for j in range(0,i):
        if a[j] < a[j+1]:
            a[j] = a[j]
        else:
            while a[j+1] < a[j]: #and a[k] != a[0]:
                c = a[j+1]
                a[j+1] = a[j]
                a[j] = c
                #a[k] = a[k]
            else:
                a[j+1] = a[j+1]

print(a)
