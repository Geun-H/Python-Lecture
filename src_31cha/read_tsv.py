data = []
with open("test.tsv") as handle:
    header = handle.readline().strip().split("\t")
    for line in handle:
        row = line.strip().split("\t")
        data.append(dict(zip(header, row)))

print(data)
sorted_data = sorted(data, key=lambda x: float(x["VALUE"]), reverse=True)
print(sorted_data)
