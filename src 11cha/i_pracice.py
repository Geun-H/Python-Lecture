with open("sample.txt") as handle:
    for line in handle:
        print(line.strip())

fo = open("sample.txt", "r")
# print(fo.readlines())
for row in fo:
    print(row.strip())

fo.close()
