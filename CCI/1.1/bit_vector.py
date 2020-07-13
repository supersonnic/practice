def is_unique(str):
    bitmap = 0
    for char in str:
        character = ord(char) - 97
        if not is_set(bitmap, character):
            bitmap = set(bitmap, character)
        else:
            return False
    return True

def is_set(bitmap, bit):
    mask = 1 << bit
    if (bitmap & mask):
        return True
    return False

def set(bitmap, bit):
    mask = 1 << bit
    return bitmap | mask


print("abc" + str(is_unique("abc")))
print("abcdez" + str(is_unique("abcdez")))
print("a" + str(is_unique("a")))
print("z" + str(is_unique("z")))
print("zabcz" + str(is_unique("zabcz")))
print("bbbb" + str(is_unique("bbbb")))
