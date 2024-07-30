def add_all(a: int, b: int, c: int) -> int:
    """add three numbers

    Args:
        a (int): input number 1
        b (int): input number 2
        c (int): input number 3

    Returns:
        int: a+b+c

    Example:
        add_all(1,2,3) -> 6
        add_all(3,2,3) -> 8
        add_all(5,5,5) -> 15
    """
    return a + b + c


if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))
    print(add_all(a, b, c))
