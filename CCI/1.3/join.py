def solution(str):
    res = []
    for char in str:
        if char == " ":
            res.append("%20")
        else:
            res.append(char)
    return "".join(res)

string = "a bc"
print(string + " : " + solution(string))

string = "a b c"
print(string + " : " + solution(string))

string = "c"
print(string + " : " + solution(string))

string = " c"
print(string + " : " + solution(string))

string = "c "
print(string + " : " + solution(string))

string = " "
print(string + " : " + solution(string))

string = ""
print(string + " : " + solution(string))

string = "  "
print(string + " : " + solution(string))
