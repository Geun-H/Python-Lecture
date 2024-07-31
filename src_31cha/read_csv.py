"""
with open("test.csv") as file_csv:
    l_head = file_csv.readline().strip().split(",")
    for line in file_csv:
        l_row = line.strip().split(",")
        print(
            f"{l_head[0]}: {l_row[0]}, {l_head[1]}: {l_row[1]}, {l_head[2]}: {l_row[2]}"
        )
"""

data = []
with open("test.csv") as handle:
    header = handle.readline().strip().split(",")
    for line in handle:
        row = line.strip().split(",")
        data.append({header[0]: row[0], header[1]: row[1], header[2]: row[2]})

for elem in data:
    print(elem)
