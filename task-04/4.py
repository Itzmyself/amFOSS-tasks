a=input()
freq=[0]*10

for i in a:
    if i.isdigit():
        freq[int(i)]+=1

print(' '.join(map(str,freq)))