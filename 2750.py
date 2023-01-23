N=int(input())
lis=[]
for i in range(N):
    lis.append(int(input()))
lisort=sorted(lis)
for i in range(len(lis)):
    print(lisort[i])