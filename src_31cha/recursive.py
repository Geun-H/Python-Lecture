def make_kmer(l1, l2, n):
    if n == 1:
        return l2
    ltmp = []
    for b1 in l1:
        for b2 in l2:
            ltmp.append(b1 + b2)

    return make_kmer(l1, ltmp, n - 1)


def check_palindrome(s):
    return s == s[::-1]


l1 = ["A", "C", "G", "T"]
l2 = ["A", "C", "G", "T"]
kmers = make_kmer(l1, l2, 5)
cnt = 0
for kmer in kmers:
    if check_palindrome(kmer):
        print(kmer)
        cnt += 1
print(cnt)
