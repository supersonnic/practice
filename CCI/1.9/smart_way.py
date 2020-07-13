def isRotation(str1, str2):
    l = len(str1)
    if l != len(str2):
        return False
    if l == 0:
        return True
    return isSubstring(str1, str2 + str2)

def isSubstring(s1, s2):
    if s1 in s2:
        return True
    return False

str1 = ""
str2 = ""
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "abc"
str2 = "a"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "a"
str2 = "a"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "ab"
str2 = "ba"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = ""
str2 = ""
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "waterbottle"
str2 = "erbottlewat"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "waterbottle"
str2 = "aterbottlew"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))

str1 = "Waterbottle"
str2 = "aterbottlew"
print(str1 + " and " + str2 + "  " + str(isRotation(str1,str2)))
