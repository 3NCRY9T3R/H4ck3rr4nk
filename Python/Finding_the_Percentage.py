n=int(input())
a=[]
b=[]
s=0
c=[]
for i in range(n):
    data=input()
    a=data.split(' ')
    b.append(a)
name=input()
for sublist in b:
    for val in sublist:
        c.append(val)
for i in range(len(c)):
    if(name==c[i]):
        s=(float(c[i+1])+float(c[i+2])+float(c[i+3]))
        p=(s/3)
print("{0:.2f}".format(p))
