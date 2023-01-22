new_list=[1]*10001
for b in range(1,10001):
    new_num = b
    c = str(new_num)
    for i in range(len(c)):
        new_num += int(c[i])

    if new_num < 10001:
        new_list[new_num] = 0


for i in range(1,10001):
    if new_list[i] == 1:
        print(i)