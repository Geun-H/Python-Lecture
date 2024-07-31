a, b = input().split()
i_a = int(a)
i_b = int(b)
i_c = int(input())
i_b = i_b + i_c

if i_b >= 60:
    i_a += i_b // 60
    i_b = i_b % 60
    if i_a >= 24:
        i_a = i_a % 24
print(i_a, i_b)
