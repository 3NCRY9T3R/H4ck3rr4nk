a=[]
b=[]
mod=[]
final=[]
n=int(input())
g=input()
newg=g.split(' ')
for i in range(len(newg)):
    temp=int(newg[i])
    a.append(temp)
mean=sum(a)/n
print(mean)
a.sort()
if(n%2==0):
    median=(a[n//2]+a[(n//2)-1])/2
else:
    median=a[(n//2)+1]
print(median)
for i in range(n):
    c=a.count(a[i])
    b.append(c)
d=max(b)
for i in range(n):
    if(d==b[i]):
        mod.append(i)
for i in range(len(mod)):
    final.append(a[mod[i]])
print(min(final))
