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

#print(numbertopattern(5353,7))