def cellCompete(states, days):
    if not states:
        return states
    states.insert(0, 0)
    states.append(0)
    length = len(states)
    out = []
    for i in range(days):
        if out:
            print("replacing")
            states = out
            out.clear()
        print(states)
        out.append(0)
        for j in range(1, length - 1):
            out.append(states[j-1]^states[j+1])
        out.append(0)
    return out[1:length-1]
