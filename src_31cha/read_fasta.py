from collections import defaultdict


class FastaReader:
    def __init__(self):
        pass

    def read_fasta(self, filepath):
        seq = ""
        with open(filepath) as handle:
            for line in handle:
                if line.startswith(">"):
                    continue

                seq += line.strip()
        return seq

    def count_seq(self, seq):
        data = defaultdict(int)
        for base in seq:
            data[base] += 1
        return data


fasta_reader = FastaReader()
seq = fasta_reader.read_fasta("test.fasta")
print(seq)
data = fasta_reader.count_seq(seq)
print(data)
