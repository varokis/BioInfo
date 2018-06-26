from random import randint


def rms(dna, k, times):
# Diese Funktion führt randomized_motif_search times mal aus und gibt am Ende
# das beste gefundene Ergebnis aus.
    best = randomized_motif_search(dna, k)
    for i in range(1, times):
        x = randomized_motif_search(dna, k)
        if x < best:
            best = x
    return best

def randomized_motif_search(dna, k):
    motifs = []
    for i in range(0, len(dna)):
        randmotif = randint(0, len(dna[i])-k)
        motifs.append(dna[i][randmotif:randmotif+k])
    bestmotifs = motifs
    bestscore = score(motifs, consensusfromprofile(make_profile(motifs)))
    #print(bestscore)
    while True:
        profile = make_profile(motifs)
        #print(profile)
        motifs = make_motifs(profile, dna)
        cons = consensusfromprofile(profile)
        #print(cons)
        if score(motifs, cons) < bestscore:
            #print("SCHLEIFE")
            bestscore = score(motifs, cons)
            #print(bestscore)
            bestmotifs = motifs
            #print(bestmotifs)
        else:
            return bestscore, bestmotifs


def make_profile(motifs):
    # Erstelle für jede Position im Motiv ein 4-Tupel wobei die Stellen für
    # (A,C,G,T) stehen. Für jedes 4-Tupel wird dann die entsprechende Stelle
    # in den Motiven durchgegangen und die jeweilige Stelle inkrementiert,
    # bevor am Ende durch die Gesamtanzahl verwendeter Motive geteilt wird um
    # "Wahrscheinlichkeiten" zu erhalten. Es werden Pseudocounts benutzt,
    # da mit einem (1,1,1,1) Profil begonnen wird.
    profile = []
    for i in range(0, len(motifs[0])):
        profile.append([1.0, 1.0, 1.0, 1.0])
        for j in range(0, len(motifs)):
            if motifs[j][i] == "A":
                profile[i][0] += 1.0
            elif motifs[j][i] == "C":
                profile[i][1] += 1.0
            elif motifs[j][i] == "G":
                profile[i][2] += 1.0
            elif motifs[j][i] == "T":
                profile[i][3] += 1.0
        profile[i][0] = (profile[i][0]) / (len(motifs)+4)
        profile[i][1] = (profile[i][1]) / (len(motifs)+4)
        profile[i][2] = (profile[i][2]) / (len(motifs)+4)
        profile[i][3] = (profile[i][3]) / (len(motifs)+4)
    return profile


def make_motifs(profile, dna):
    # len(profile) entspricht dem ursprünglichen k.
    #print("make motifs")
    k = len(profile)
    motifs = []
    for i in range(0, len(dna)):
        #print("i: ", i)
        mostprob = 0
        bestfit = 0
        for j in range(0, len(dna[i])-k):
           # print("J: ",j)
            prob = 1
            for h in range(0, k):
                prob *= profile[h][symboltonumber(dna[i][j+h])]
            if prob > mostprob:
                bestfit = j
                mostprob = prob
            #print("PROB:", prob)
           #print("MOSTPROB:", mostprob)
            #print("Bestfit", bestfit)
        motifs.append(dna[i][bestfit:bestfit+k])
    #print(motifs)
    return motifs


def consensusfromprofile(profile):
    # Es ist einfacher und weniger rechenaufwändig den Consensusstring aus dem
    # Profil zu berechnen als aus den einzelnen Motiven.
    cons = []
    for i in range(0, len(profile)):
        cons.append(numbertosymbol(profile[i].index(max(profile[i]))))
    return cons


def score(motifs, cons):
    score = 0
    for i in range(0, len(motifs)):
        score += hamming_distance(motifs[i], cons)
    return score


# Aus den vergangenen Übungen

def symboltonumber(s):
    if s == "A":
        return 0
    elif s == "C":
        return 1
    elif s == "G":
        return 2
    elif s == "T":
        return 3


def numbertosymbol(s):
    if s == 0:
        return "A"
    elif s == 1:
        return "C"
    elif s == 2:
        return "G"
    elif s == 3:
        return "T"


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


K1 = 8
DNA1 = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
       "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
       "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
       "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

K2 = 15
DNA2 = [
"ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT",
"AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT",
"CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA",
"ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG",
"TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT",
"ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA",
"CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT",
"ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT",
"CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA",
"GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT",
"AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG",
"ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA",
"AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA",
"GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT",
"TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA",
"TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA",
"TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA",
"GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT",
"TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG",
"TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT",
]

MOTIFS = ["TCTCGGGG","CCAAGGTG","TACAGGCG","TTCAGGTG","TCCACGTG"]



print(rms(DNA2,K2,1000))