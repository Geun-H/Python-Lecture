def operate(a, b):

    if int(a) > int(b):
        return ">"
    elif int(a) < int(b):
        return "<"
    elif int(a) == int(b):
        return "=="


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(operate(a, b))
