def encode(string):
    res = []
    count, j = 0, 0
    if len(string) == 0:
        return string
    for i in range(len(string)):
        if string[i] != string[j]:
            res.append(string[j])
            res.append(str(count))
            count, j = 0, i
        count += 1
    res.append(string[-1])
    res.append(str(count))
    if len(res) >= len(string):
        return string
    return "".join(res)

string = "abc"
print(string + " : " + encode(string))

string = "aaab"
print(string + " : " + encode(string))

string = "aaaab"
print(string + " : " + encode(string))

string = "aaaabc"
print(string + " : " + encode(string))

string = "abbbccc"
print(string + " : " + encode(string))

string = "abbbc"
print(string + " : " + encode(string))

string = "abccc"
print(string + " : " + encode(string))

string = "a"
print(string + " : " + encode(string))

string = ""
print(string + " : " + encode(string))

string = "aaabbbccc"
print(string + " : " + encode(string))

string = "aaabbbcccdddeeefff"
print(string + " : " + encode(string))
