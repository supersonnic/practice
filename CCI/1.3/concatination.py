def solution(str):
    res = ""
    for char in str:
        if char == " ":
            res = res + "%20"
        else:
            res = res + char
    return res

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
