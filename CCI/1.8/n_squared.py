def solution(m):
    if len(m) <= 1:
        return m
    row_len = len(m)
    col_len = len(m[0])
    row = set({})
    col = set({})
    for i in range(row_len):
        for j in range(col_len):
            if m[i][j] == 0:
                row.add(i)
                col.add(j)
                break
    for i in row:
        for j in range(col_len):
            m[i][j] = 0
    for j in col:
        for i in range(row_len):
            m[i][j] = 0
    return m

m = []
print(str(m) + " : " + str(solution(m)))
print("\n")

m = ['a']
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [0]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b'],['c',0],[0,0]]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b','c'],['d',0,'f']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [[0,'b','c'],['d',0,'f'],['g','h','i']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [['a','b','c','d'],['e','f','g',0],['i','j','k','l']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [[0,'b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
print(str(m) + " : " + str(solution(m)))
print("\n")

m = [[0,'b','c','d','e'],['f',0,'h','i','j'],['k','l',0,'n','o'],['p','q','r',0,'t'],['u','v','w','x',0]]
print(str(m) + " : " + str(solution(m)))
print("\n")
