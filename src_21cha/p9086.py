def pick_fl(word: str) -> str:
    """get first and last character

    Args:
        word (str): input only alphabet

    Returns:
        str: first ans last character of the word

    Example:
        >>> pick_fl("AAADSDSDSFE")
        "AE"
    """
    return word[0] + word[-1]


if __name__ == "__main__":
    word = input()
    print(pick_fl(word))
