from collections import Counter

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

count_a=Counter(a)
count_b=Counter(b)
c=[]

for i in b:
    if count_b[i]>count_a[i]:
        c.append(i)
        count_a[i] += 1

print(' '.join(map(str,c)))