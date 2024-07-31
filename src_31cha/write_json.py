import json

data = []
with open("test.csv") as handle:
    header = handle.readline().strip().split(",")
    for line in handle:
        row = line.strip().split(",")
        data.append(dict(zip(header, row)))

print(data)

with open("output.json", "w") as write_handle:

    json.dump(data, write_handle, indent=2)
