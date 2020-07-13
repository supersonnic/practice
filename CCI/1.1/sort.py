def is_unique(str):
    sorted_str = sorted(str)
    for i in range(1, len(sorted_str)):
        if sorted_str[i - 1] == sorted_str[i]:
            return False
    return True




print("" + str(is_unique("")))
print("a" + str(is_unique("a")))
print("abcd" + str(is_unique("abcd")))
print("abcad" + str(is_unique("abcad")))
print("dddd" + str(is_unique("dddd")))
print("bbsdgw" + str(is_unique("bbsdgw")))
