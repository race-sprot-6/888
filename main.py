a = [23,59,204,822,1,22,93,58]
for k in range(0,len(a)-1):
    for i in range(0,len(a)-1):
        if a[i]<a[i+1]:
            a[i]=a[i]
        else:
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
print(a)