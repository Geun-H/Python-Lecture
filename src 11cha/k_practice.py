try:
    with open("noname.txt") as handle:
        for line in handle:
            print(line.strip())
except Exception as err:
    print(f"error: {err}")


try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("Value error")
except Exception as err:
    print(f"Error: {err}")

print("#END")


d_dic: dict[str:int] = {"aaa": 1, 3: "a"}
print(d_dic.keys())
