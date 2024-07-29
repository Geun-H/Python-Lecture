with open("temp.fasta", "w") as handle:
    handle.write(">A_Strain\n")
    handle.write("ATGCFFAAG\n")
    handle.write("TCGGGATAG\n")

data = [">A_Strain", "CCGCCFAAG", "TCGGGATAG"]

with open("temp.fasta", "w") as fw:
    fw.write("\n".join(data))
