def part_one():
    ans = 0

    with open("input.txt") as f:
        for line in f:
            nums = list(map(int, line.strip().split(" ")))
            differences = set([nums[i]-nums[i+1] for i in range(len(nums)-1)])
            if differences.issubset(set([1,2,3])) or differences.issubset(set([-1,-2,-3])):
                ans += 1
    
    print(ans)


def part_two():
    ans = 0

    def check_part_one(nums):
        differences = set([nums[i]-nums[i+1] for i in range(len(nums)-1)])
        return differences.issubset(set([1,2,3])) or differences.issubset(set([-1,-2,-3]))


    with open("input.txt") as f:
        for line in f:
            nums = list(map(int, line.strip().split(" ")))
            if check_part_one(nums):
                ans += 1
            else:
                # part two; deal with one bad level
                differences = [nums[i]-nums[i+1] for i in range(len(nums)-1)]
                pos = sum([1 if d > 0 else 0 if d == 0 else -1 for d in differences])
                if pos == 0:
                    continue
                is_decreasing = pos / abs(pos) == 1

                for i in range(len(nums)-1):
                    if (is_decreasing and nums[i]-nums[i+1] <= 0) or (not is_decreasing and nums[i]-nums[i+1] >= 0) or abs(nums[i]-nums[i+1]) > 3:
                        if check_part_one(nums[:i] + nums[i+1:]):
                            ans += 1
                            break
                        if i+2 < len(nums):
                            if check_part_one(nums[:i+1] + nums[i+2:]):
                                ans += 1
                                break
                        else:
                            if check_part_one(nums[:i+1]):
                                ans += 1
                                break
                
    print(ans)

part_two()
