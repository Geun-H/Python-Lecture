import sys

i = 5
res = 1
while i > 0:
    res *= i
    i -= 1
print(res)


n = 5
result = 1
while True:
    if n == 0:
        break

    result *= n
    n -= 1

print(result)
