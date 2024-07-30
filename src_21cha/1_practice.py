seq = "AGTTTATAG"
for i in range(len(seq)):
    if seq[i : i + 2] == "AG":
        print(i)
