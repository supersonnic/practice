def hanoi():

    s0 = [0, 1, 2, 3, 4, 5]
    s1 = []
    s2 = []

    def move(n, src, dst, buff):
        if n:
            print("calling move 1")
            move(n-1, src, buff, dst)
            print("moving shit")
            dst.append(src.pop())
            print("calling move 2")
            move(n-1, buff, dst, src)

    move(len(s0), s0, s2, s1)
    print(s0, s1, s2)
hanoi()
