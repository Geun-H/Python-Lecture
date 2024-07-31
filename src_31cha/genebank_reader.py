from Bio import SeqIO
import pandas as pd

record = SeqIO.parse("NC_045512.gb", "genbank")
print(record.id)
print(record.seq)
print(record.description)
print(record.annotations)


for k, v in record.annotations.items():
    print(k, "::", v)

print(record.seq.reverse_complement()[::-1])
print(record.seq.translate())


data = {
    "A":record.seq.count{"A"},
    "C":record.seq.count{"C"},
    "G":record.seq.count{"G"},
    "T":record.seq.count{"T"},
}
df_data = {"base":data.keys(), "count":data.values()}
df = pd.DataFrame(df_data)
print(df)

df.plot(kind="bar", x="base", y="count", title = "base count", xlabel = "Base", ylabel = "Count")

"--------------------------------------"

from Bio import Entrez

Entrez.email = "gjrms365@gmail.com"
handle = Entrez.efetch(db="nucleotide", rettype="gb", id=ncbi_id, retmode="text")
with open (f"{ncbi_id}.gb", "w") as fw:
    for line in handle:
        fw.write(line)
    print(f"##Done: {ncbi_id}.gb")

