def add_two(a: int, b: int):
    return a + b


if __name__ == "__main__":
    res = add_two(2, 3)
    exp = 5
    assert exp == res
    print("done")
