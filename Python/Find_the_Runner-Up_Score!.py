a=[]
n=int(input())
sc=input()
ab=sc.split()
for i in range(n):
    temp=ab[i]
    a.append(int(temp))
c=a.count(max(a))
a.sort()
print(a[n-c-1])
