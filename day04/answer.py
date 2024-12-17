def part_one():
    ans = 0
    grid = []

    n = 0
    m = 0

    # needs grid[x][y] to be "X"
    def find_xmas(x, y):
        def is_xmas(l):
            return l == ["X", "M", "A", "S"]
        
        part_ans = 0
        # left <-- SAMX
        if y-3 >= 0:
            if is_xmas(grid[x][y-3:y+1][::-1]):
                part_ans += 1
        # right --> XMAS
        if y+3 < m:
            if is_xmas(grid[x][y:y+4]):
                part_ans += 1
        # up
        if x-3 >= 0:
            if is_xmas([grid[z][y] for z in range(x-3,x+1)][::-1]):
                part_ans += 1
        # down
        if x+3 < n:
            if is_xmas([grid[z][y] for z in range(x,x+4)]):
                part_ans += 1
        # diagonal LU
        if x-3 >= 0 and y-3 >= 0:
            if is_xmas([grid[x-z][y-z] for z in range(0,4)]):
                part_ans += 1
        # diagonal RU
        if x-3 >= 0 and y+3 < m:
            if is_xmas([grid[x-z][y+z] for z in range(0,4)]):
                part_ans += 1
        # diagonal LD
        if x+3 < n and y-3 >= 0:
            if is_xmas([grid[x+z][y-z] for z in range(0,4)]):
                part_ans += 1
        # diagonal RD
        if x+3 < n and y+3 < m:
            if is_xmas([grid[x+z][y+z] for z in range(0,4)]):
                part_ans += 1
        
        return part_ans

    with open("input.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
        n = len(grid)
        m = len(grid[0])
    
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "X":
                ans += find_xmas(x, y)
    print(ans)

def part_two():
    ans = 0
    grid = []

    n = 0
    m = 0

    with open("input.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
        n = len(grid)
        m = len(grid[0])

    # needs grid[x][y] to be "A"
    def find_xmas(x, y):
        # needs a square of space of unit 1
        if x == 0 or y == 0 or x == n-1 or y == m-1:
            return 0
        LU = grid[x-1][y-1]
        RU = grid[x-1][y+1]
        LD = grid[x+1][y-1]
        RD = grid[x+1][y+1]
        all_dict = {x:[LU, RU, LD, RD].count(x) for x in [LU, RU, LD, RD]}
        if (set(["M", "S"]) == set(all_dict.keys())) and ([2,2] == list(all_dict.values())) and (LU == LD or LU == RU):
            return 1
        return 0
    
    for x in range(n):
        for y in range(m):
            if grid[x][y] == "A":
                ans += find_xmas(x, y)
    print(ans)

part_two()

            