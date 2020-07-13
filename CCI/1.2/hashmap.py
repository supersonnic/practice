def is_perm(str1, str2):
    chars = {}
    for char in str1:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    for char in str2:
        if char not in chars:
            return False
        chars[char] -= 1
        if chars[char] == 0:
            del chars[char]

    if len(chars) == 0:
        return True
    return False

str1 = "abc"
str2 = "bca"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = "a"
str2 = "a"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = ""
str2 = ""
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = "bbb"
str2 = "bbb"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = "abcdfrr"
str2 = "bca"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = "sdf"
str2 = "dsfsdfe3"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))

str1 = "abbc"
str2 = "abc"
print(str1 + " and " + str2 + "  " + str(is_perm(str1,str2)))
