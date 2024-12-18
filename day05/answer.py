def part_one():
    rules = {}
    lines = []
    ans = 0

    with open("input.txt") as f:
        is_rule = True
        for line in f:
            if line == "\n":
                is_rule = False
            elif is_rule:
                before, after = list(map(int, line.strip().split("|")))
                if before not in rules:
                    rules[before] = set()
                rules[before].add(after)
            else:
                lines.append(list(map(int, line.strip().split(","))))
    
    for line in lines:
        prev = set()
        bad = False
        # if y=prev is in rules[x], then it is wrong
        for x in line:
            if prev and x in rules and prev.intersection(rules[x]):
                bad = True
                break
            prev.add(x)
        if not bad:
            ans += line[len(line)//2]

    print(ans)


def part_two():
    rules = {}
    backwards_rules = {}
    lines = []
    ans = 0

    with open("input.txt") as f:
        is_rule = True
        for line in f:
            if line == "\n":
                is_rule = False
            elif is_rule:
                before, after = list(map(int, line.strip().split("|")))
                if before not in rules:
                    rules[before] = set()
                if after not in backwards_rules:
                    backwards_rules[after] = set()
                rules[before].add(after)
                backwards_rules[after].add(before)
            else:
                lines.append(list(map(int, line.strip().split(","))))

    for line in lines:
        prev = set()
        bad = False
        # if y=prev is in rules[x], then it is wrong
        for x in line:
            if prev and x in rules and prev.intersection(rules[x]):
                bad = True
                break
            prev.add(x)
        if bad:
            still_need_added = set(line)
            new_line = []

            while len(still_need_added) > 0:
                for x in still_need_added:
                    if (x not in backwards_rules) or (backwards_rules[x].intersection(still_need_added) == set()):
                        new_line.append(x)
                        still_need_added.remove(x)
                        break
            ans += new_line[len(new_line)//2]
    print(ans)

part_two()


