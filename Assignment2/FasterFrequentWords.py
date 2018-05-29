import ba1k
import ba1m


def fasterfrequentwords(text,k):
    frequentpatterns = []
    frequencyarray = ba1k.computingfrequencies(text,k)
    maxcount = max(frequencyarray)
    for i in range(0, (4**k)-1):
        if frequencyarray[i] == maxcount:
            pattern = ba1m.numbertopattern(i,k)
            frequentpatterns.append(pattern)
    return frequentpatterns


# Input von Übungsaufgabe 1
print(fasterfrequentwords("CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATT"
                          "CATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGG"
                          "GCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCG"
                          "TGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAG"
                          "CATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCG"
                          "GGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGA"
                          "GGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCG"
                          "GGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGG"
                          "CGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG",12))
