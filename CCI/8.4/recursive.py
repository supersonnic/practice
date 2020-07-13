def superset(l, output):
    output.append(l)
    if len(l) > 1:
        superset(l[:-1], output)
        superset(l[1:], output)
    return output

output = []
l = [i for i in range(3)]
sol1 = superset(l, output)
sol1.append([])
print(sol1)
