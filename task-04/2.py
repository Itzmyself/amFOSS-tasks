from collections import Counter

a=int(input())
b=list(map(int,input().split()))
count_b=Counter(b)

for i in b:
    if count_b[i]==1:
        print(i)