import re
def parse(s):
    pattern = re.compile(r"([A-Z]): '([a-z])', '([a-z])'")
    return pattern.findall(s)






input = "A: 'a', B: 'a', 'b', C: 'v', 'h'"
print(parse(input))
