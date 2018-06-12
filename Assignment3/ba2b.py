def medianString(dna,k):
    stringDist = k+1
    for i in range(0, (4**k)-1):
        pattern = numbertopattern(i,k)
        if stringDist > distance(pattern,dna):
            stringDist = distance(pattern,dna)
            median = pattern
    return median


def distance(pattern, dna):
    k = len(pattern)
    dist = 0
    for i in range(0, len(dna)):
        text = dna[i]
        hammdist = k+1
        for j in range(0, len(text)-k+1):
            textpattern = text[j:j+k]
            if hammdist > hamming_distance(pattern, textpattern):
                hammdist = hamming_distance(pattern, textpattern)
        dist += hammdist
    return dist


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)
    prefixindex = index // 4
    r = index % 4
    symbol = numbertosymbol(r)
    prefixpattern = numbertopattern(prefixindex, k-1)
    return prefixpattern + symbol


def numbertosymbol(s):
    if s == 0:
        return "A"
    elif s == 1:
        return "C"
    elif s == 2:
        return "G"
    elif s == 3:
        return "T"


k = 6
DNA = ("TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT",
       "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA",
       "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT",
       "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA",
       "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG",
       "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA",
       "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC",
       "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA",
       "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG",
       "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG")

print(medianString(DNA,k))