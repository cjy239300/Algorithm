N=int(input())
num=0
for i in range(1,N+1):
    if i<100:
        num+=1
    else:
        c=list(map(int,str(i)))
        if (c[0]-c[1])==(c[1]-c[2]):
            num+=1
print(num)