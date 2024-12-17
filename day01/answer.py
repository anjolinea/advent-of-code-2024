def part_one():
    left_list = []
    right_list = []

    with open("input.txt") as f:
        for line in f:
            ln, rn = line.strip().split("   ")
            left_list.append(int(ln))
            right_list.append(int(rn))

    left_list.sort()
    right_list.sort()
    ans = sum([abs(left_list[i]-right_list[i]) for i in range(len(left_list))])
    print(ans)

def part_two():
    left_dict = {}
    right_dict = {}

    with open("input.txt") as f:
        for line in f:
            ln, rn = list(map(int,line.strip().split("   ")))
            left_dict[ln] = left_dict.get(ln, 0) + 1
            right_dict[rn] = right_dict.get(rn, 0) + 1
            
    ans = sum([k * v * right_dict[k] if k in right_dict else 0 for k,v in left_dict.items()])
    print(ans)

part_two()