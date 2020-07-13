def solution(str1, str2):

    if str1 == str2:
        return True
    len1, len2 = len(str1), len(str2)
    if abs(len1 - len2) > 1:
        return False
    if len1 > len2:
        str1, str2 = str2, str1
        len1, len2 = len2, len1
    edited = False
    i, j = 0, 0
    if len1 == len2:
        while i < len1:
            if str1[i] != str2[j]:
                if edited:
                    return False
                edited = True
                if len1 == len2:
                    j += 1
                i += 1
                j += 1
    return True

str1 = "ple"
str2 = "pale"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "pale"
str2 = "ple"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "a"
str2 = "a"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = ""
str2 = ""
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "bbb"
str2 = "bbb"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "abcdfrr"
str2 = "bca"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "sdf"
str2 = "dsfsdfe3"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "abbc"
str2 = "abc"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "abcd"
str2 = "abcde"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))

str1 = "bcde"
str2 = "abcde"
print(str1 + " and " + str2 + "  " + str(solution(str1,str2)))
