l_list = []
for i in range(1, 10):
    n = int(input())
    if int(n) < 100:
        l_list.append(n)
i_m = max(l_list)
print(i_m)
print(l_list.index(i_m) + 1)
