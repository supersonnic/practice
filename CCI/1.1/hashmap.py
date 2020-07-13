def is_unique(str):
    chars = {}
    for char in str:
        if char not in chars:
            chars[char] = 1
        else:
            return False
    return True




print("" + str(is_unique("")))
print("a" + str(is_unique("a")))
print("abcd" + str(is_unique("abcd")))
print("abcad" + str(is_unique("abcad")))
print("dddd" + str(is_unique("dddd")))
print("bbsdgw" + str(is_unique("bbsdgw")))
