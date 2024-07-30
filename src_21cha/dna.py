class DNA:
    def __init__(self, seq, sam_id):
        self.seq: str = seq
        self.sample_id: int = sam_id

    def __str__(self):
        return f"sample_id: {self.sample_id}\nsequence: {self.seq}"

    def __add__(self, other):
        return self.seq + other.seq

    def get_length(self):
        return len(self.seq)

    def get_reverse_seq(self):
        return self.seq[::-1]

    def count_base(self, base):
        return self.seq.count(base)


if __name__ == "__main__":
    dna = DNA("ATGTTATAG", 123)
    length = dna.get_length()
    print(length)
    rev_seq = dna.get_reverse_seq()
    print(rev_seq)
    print(dna.count_base("A"))
    print(dna)
    dna2 = DNA("TTTT", 200)
    print(dna + dna2)
