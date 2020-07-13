def solution(m):
    l = len(m)
    if l <= 1:
        return m
    for j in range(l // 2):
        for i in range(j, l - j - 1):
            m[j][i], m[i][l-j-1],m[l-i-1][j], m[l-j-1][l-i-1] = m[i][l-j-1], m[l-j-1][l-i-1], m[j][i], m[l-i-1][j]
    return m

m = []
print(str(m) + " : " + str(solution(m)))
print("\n")

m = ['a']
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b'],['c','d']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b','c'],['d','e','f'],['g','h','i']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
print(str(m) + " : " + str(solution(m)))
print("\n")
