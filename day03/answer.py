import re

def part_one():
    ans = 0

    with open("input.txt") as f:
        for line in f:
            all_mul = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line.strip())
            for mul in all_mul:
                first_num, second_num = list(map(int, mul[4:-1].split(",")))
                ans += first_num * second_num

    print(ans)

def part_two():
    ans = 0

    do = True
    with open("input.txt") as f:
        for line in f:
            all_mul = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line.strip())
            for mul in all_mul:
                if mul == "don't()":
                    do = False
                elif mul == "do()":
                    do = True
                else:
                    first_num, second_num = list(map(int, mul[4:-1].split(",")))
                    if do:
                        ans += first_num * second_num

    print(ans)

part_two()


