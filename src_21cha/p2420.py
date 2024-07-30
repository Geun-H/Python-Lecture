def chai(a, b):
    return abs(a - b)


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(chai(a, b))
