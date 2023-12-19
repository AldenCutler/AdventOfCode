input = open("input.txt", "r")
lines = [line.split() for line in input.read().strip().split("\n\n")]
input.close()

rules, parts = lines[0], lines[1]

# find starting index
def find_rule(id):
    for rule in rules:
        if id in rule.split("{")[0]:
            return rules.index(rule)
    return -1
        
start = find_rule("in")

def check_criteria(criteria, x, m, a, s):
    category = criteria[0]   # category
    comparison = criteria[1]   # comparison to perform
    value = int(criteria.split(":")[0].split(comparison)[1])   # value to compare to
 
    #print("category=", category, " comparison=", comparison, " value=", value)
 
    if category == "x":
        if comparison == ">":
            return x > value
        elif comparison == "<":
            return x < value
    elif category == "m":
        if comparison == ">":
            return m > value
        elif comparison == "<":
            return m < value
    elif category == "a":
        if comparison == ">":
            return a > value
        elif comparison == "<":
            return a < value
    elif category == "s":
        if comparison == ">":
            return s > value
        elif comparison == "<":
            return s < value
    
    
def get_next_id(rule, part):
    
    # get part values
    x, m, a, s = part.split(",")
    x = int(x.split("=")[1])
    m = int(m.split("=")[1])
    a = int(a.split("=")[1])
    s = int(s.split("=")[1][:-1])
    #print("x=", x, " m=", m, " a=", a, " s=", s)
    
    # get rule values
    criteria = rule.split(",")
    criteria[0] = criteria[0].split("{")[1]
    criteria[-1] = criteria[-1][:-1]
    #print(criteria)

    # check each criteria
    for i in range(len(criteria) - 1):
        good = criteria[i].split(":")[1]
        if check_criteria(criteria[i], x, m, a, s):
            return good
    return criteria[-1]
        
        
total = 0
for part in parts:
    current = start
    result = get_next_id(rules[current], part)
    while result != "A" and result != "R":
        current = find_rule(result)
        result = get_next_id(rules[current], part)
        print(result)
    
    if result == "A":
        x, m, a, s = part.split(",")
        x = int(x.split("=")[1])
        m = int(m.split("=")[1])
        a = int(a.split("=")[1])
        s = int(s.split("=")[1][:-1])
        total += x + m + a + s
    print(total)