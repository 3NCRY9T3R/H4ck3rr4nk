a=[]
b=[]
n=int(input())
g=input()
ele=input()
newg=g.split(' ')
newele=ele.split(' ')
for i in range(n):
    temp1=int(newg[i])
    temp2=int(newele[i])
    a.append(temp1*temp2)
    b.append(temp2)
mean=sum(a)/sum(b)
print('%.1f'%mean)
