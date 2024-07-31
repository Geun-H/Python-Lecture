l_all = list(map(int, input().split()))

if l_all[0] == l_all[1] and l_all[1] == l_all[2]:
    print(10000 + (l_all[0] * 1000))
elif l_all[0] == l_all[1] or l_all[1] == l_all[2]:
    print(1000 + (l_all[1] * 100))
elif l_all[0] == l_all[2]:
    print(1000 + (l_all[0] * 100))
else:
    print(max(l_all) * 100)
