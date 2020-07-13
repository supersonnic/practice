def pal_perm(str):
    chars = {}
    str.lower()
    for char in str:
        if char == " ":
            continue
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    middle = 0
    for v in chars.values():
        if v % 2 != 0:
            middle += 1
        if middle > 1:
            return False
    return True

string = "tact coa"
print(string + " : " + str(pal_perm(string)))

string = "a"
print(string + " : " + str(pal_perm(string)))

string = "aa"
print(string + " : " + str(pal_perm(string)))

string = "a a"
print(string + " : " + str(pal_perm(string)))

string = "a  a"
print(string + " : " + str(pal_perm(string)))

string = "abccaa"
print(string + " : " + str(pal_perm(string)))

string = "aabbcd "
print(string + " : " + str(pal_perm(string)))

string = ""
print(string + " : " + str(pal_perm(string)))

string = " "
print(string + " : " + str(pal_perm(string)))
