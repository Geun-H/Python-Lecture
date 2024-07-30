with open("123test.txt") as handle:
    for line in handle:
        print(line.strip())

# 터미널에서도 같은 위치여야한다.

"""
class TextFileReader:
    def __init__(self) -> None:
        pass

    def read_text(self, file_path):
        with open(file_path) as handle:
            return handle.readlines()

    def read_text_2(self, file_path):
        cnt = 0
        even, odd = list(), list()
        with open(file_path) as handle:
            for line in handle:
                if cnt % 2 == 0:
                    even.append(line.strip())
                else:
                    odd.append(line.strip())


read = TextFileReader()
read.read_text("test.txt")
"""
