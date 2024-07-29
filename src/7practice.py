import sys

s_star = "*"
for i in range(1, 6):  # start, stop, step
    print(s_star)
    s_star += "*"


n = 5
for i in range(1, n + 1):
    print((n - i) * " ", "*" * i)
