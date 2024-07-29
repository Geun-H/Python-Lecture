import sys

l_num = [6, 28, 21, 13]

for i in l_num:

    if i % 3 == 0 and i % 7 == 0:
        print(f"{i}은 3과 7의 배수입니다.")

    elif i % 3 == 0:
        print(f"{i}은 3의 배수입니다.")
    elif i % 7 == 0:
        print(f"{i}은 7의 배수입니다.")

    else:
        print(f"{i}은 3의 배수, 7의 배수가 아닙니다.")
