def patternToNumber(text):
    if not text:
        return 0
    symbol = text[-1]
    prefix = text[:-1]
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)


def symbolToNumber(s):
    if s == "A":
        return 0
    elif s == "C":
        return 1
    elif s == "G":
        return 2
    elif s == "T":
        return 3


print(patternToNumber("CTTCTCACGTACAACAAAATC"))
