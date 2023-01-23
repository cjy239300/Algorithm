M=int(input())
N=int(input())
lis=[0]
for i in range(M,N+1):
    for j in range(2,i+1):
        if i==j:
            lis.append(i)
        if i%j==0:
            break
if sum(lis)==0:
    print(-1)
else:
    print(sum(lis))
    print(lis[1])
