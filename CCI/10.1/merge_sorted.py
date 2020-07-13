def merge_sorted(a, b):
    a_pointer = (len(a) - len(b)) - 1
    b_pointer = len(b) - 1
    next_pointer = len(a) - 1
    while a_pointer >= 0 and b_pointer >= 0:
        if a[a_pointer] < b[b_pointer]:
            a[next_pointer] = b[b_pointer]
            b_pointer -= 1
        else:
            a[next_pointer] = a[a_pointer]
            a_pointer -= 1
        next_pointer -= 1
    if b_pointer != -1:
        while b_pointer >= 0:
            a[next_pointer] = b[b_pointer]
            b_pointer -= 1
            next_pointer -=1

a = [0, 5, 7, 77, None, None, None, None, None]
b = [1, 2, 5, 6, 99]
merge_sorted(a, b)
print(a)
