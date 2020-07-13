def pal_perm(str):
    bitmap = 0
    for char in str:
        if char == " ":
            continue
        bitmap = flip(ord(char), bitmap)
    bitmap_mod = bitmap - 1
    if bitmap_mod & bitmap == 0:
        return True
    return False

def flip(bit, bitmap):
    mask = 1 << bit
    return bitmap ^ mask

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
