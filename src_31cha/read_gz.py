import gzip

with gzip.open("test.txt.gz", "rt") as handle:
    for line in handle:
        print(line.strip(), type(line))
        print(len(line), "e" in line)
