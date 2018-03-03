a=[1,9,7]
b=[3,8,0]
if (a[0]>a[1] and a[0]<a[2]) or (a[0]<a[1] and a[0]>a[2]):
    temp1=int(a[0])
elif ((a[0]<a[1])and(a[1]<a[2]))or((a[0]>a[1])and(a[1]>a[2])):
    temp1=a[1]
else:
    temp1=a[2]
if (b[0]>b[1] and b[0]<b[2]) or (b[0]<b[1] and b[0]>b[2]):
    temp2=int(b[0])
elif ((b[0]<b[1])and(b[1]<b[2]))or((b[0]>b[1])and(b[1]>b[2])):
    temp2=b[1]
else:
    temp2=b[2]
list=[temp1,temp2]
print(list)