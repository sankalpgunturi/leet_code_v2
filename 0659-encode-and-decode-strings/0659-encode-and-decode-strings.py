def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i
        string = ""
        while str[j] != "#":
            string += str[j]
            j += 1
        length = int(string)
        i += 1 + len(string)
        res.append(str[i:length+i])
        i += length
    
    return res
