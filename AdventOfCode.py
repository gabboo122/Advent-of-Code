## Advent of Code
def d1one():
    n = 50  # Starting position
    c = 0   # Count of times at 0 after rotations
    
    with open("inputd1.txt") as f:
        lines = f.readlines()
    
    for line in lines:
        direction, steps = line.strip()[0], int(line.strip()[1:])
        
        if direction == 'R':
            n = (n + steps) % 100
        elif direction == 'L':
            n = (n - steps + 100) % 100
        
        if n == 0:
            c += 1
    
    return c

def d1two():
    n = 50
    c = 0
    
    with open("inputd1.txt") as f:
        lines = f.readlines()
    
    for line in lines:
        direction, steps = line.strip()[0], int(line.strip()[1:])
        
        if direction == 'R':
            # Count how many times we pass 0 moving right
            for _ in range(steps):
                n = (n + 1) % 100
                if n == 0:
                    c += 1
        elif direction == 'L':
            # Count how many times we pass 0 moving left  
            for _ in range(steps):
                n = (n - 1 + 100) % 100
                if n == 0:
                    c += 1
    
    return c

def d2one():
    n = 0
    t = 0
    l = 0
    with open("inputd2.txt") as f:
        linesr = f.readlines()
    ranges = linesr[0]
    rangesl = []
    while "," in ranges:
        first, _, rest = ranges.partition(",")
        rangesl.append(first)
        ranges = rest

    for rangen in rangesl:
        first, _, second = rangen.partition("-")
        fID = int(first)
        sID = int(second)
        
        for i in range(fID, sID + 1):
            if len(str(i)) % 2 == 0:
                l = len(str(i)) // 2
                first_half = str(i)[:l]
                second_half = str(i)[l:]
                if first_half == second_half:
                    n += 1
                    t += i
    return t

def d2two():
    t = 0
    l = []
    n = 0
    with open("inputd2.txt") as f:
        linesr = f.readlines()
    ranges = linesr[0]
    rangesl = []

    rangesc = ranges.count(",")
    if rangesc == 0:
        rangesl.append(ranges)
    elif not rangesc == 0:
        while "," in ranges:
            first, _, rest = ranges.partition(",")
            rangesl.append(first)
            ranges = rest
        rangesl.append(ranges)

    for rangen in rangesl:
        first, _, second = rangen.partition("-")
        fID = int(first)
        sID = int(second)
        
        for i in range(fID, sID + 1):
            if len(str(i)) == 2:
                first_half = str(i)[:1]
                second_half = str(i)[1:]
                if first_half == second_half:
                    t += i
            
            else:
                for r in range(2, len(str(i)) + 1):
                    if len(str(i)) % r == 0:
                        l = len(str(i)) // r
                        rep = str(i)[:l]
                        if str(i) == str(rep * r):
                            t += i
                            break

    return t

def d3one():
    with open("inputd3.txt") as f:
        powerbanks = f.readlines()
    
    total = 0

    for bank in powerbanks:
        fd = 0
        sd = 0
        fi = 0
        power = 0
        bankl = []
        for i in range(len(str(bank))):
            bankl.append(str(bank[i]))
        print(bankl)
        bankl.pop()

        for i in range(len(bankl)):
            bankl[i] = int(bankl[i])

        for i in range(len(bankl)):
            if bankl[i] > fd and not i == len(bankl):
                fd = bankl[i]
                fi = i
        
        for i in range(len(bankl)):
            if bankl[i] > sd and not i <= fi:
                sd = bankl[i]
        if sd == 0:
            sd = fd
            fd = 0
            for i in range(len(bankl) -1):
                if bankl[i] > fd and not i == len(bankl):
                    fd = bankl[i]
        power = 10*fd + sd
        total += power
        print(power)
    return total

def best_k_digits(bank_str: str, k: int = 12) -> int:
    digits = [int(ch) for ch in bank_str.strip() if ch.isdigit()]
    n = len(digits)
    to_remove = n - k
    stack = []

    for d in digits:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    stack = stack[:k]
    return int(''.join(str(d) for d in stack))

def d3two():
    total = 0
    with open("inputd3.txt") as f:
        for line in f:
            total += best_k_digits(line, 12)
    return total

def d4one():
    DIRS = [(-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)]
    with open("inputd4.txt") as f:
        grid = [line.rstrip('\n') for line in f]

    rows, cols = len(grid), len(grid[0])
    total = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            neighbors = 0
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    neighbors += 1
            if neighbors < 4:
                total += 1

    return total

def d4two():
    DIRS = [(-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)]
    with open("inputd4.txt") as f:
        grid = [list(line.rstrip('\n')) for line in f]

    rows, cols = len(grid), len(grid[0])
    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                neighbors = 0
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbors += 1
                if neighbors < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break 

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed

def d5one():
    with open("inputd5.txt") as f:
        lines = [line.strip() for line in f]

    blank_idx = lines.index("")
    range_lines = lines[:blank_idx]
    id_lines = lines[blank_idx+1:]

    ranges = []
    for line in range_lines:
        a, b = line.split("-")
        ranges.append((int(a), int(b)))

    ranges.sort()

    fresh_count = 0
    for line in id_lines:
        if not line:
            continue
        x = int(line)
        for lo, hi in ranges:
            if lo <= x <= hi:
                fresh_count += 1
                break

    return fresh_count

def d5two():
    with open("inputd5.txt") as f:
        lines = [line.strip() for line in f]

    ranges = []
    for line in lines:
        if line == "":
            break
        a, b = line.split("-")
        ranges.append((int(a), int(b)))

    ranges.sort()

    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    total = 0
    for s, e in merged:
        total += e - s + 1

    return total


def d7one():
    with open("inputd7.txt") as f:
        pathlines = f.readlines()
    
    l = 0
    lv = 0
    for i in range(len(pathlines)-1):
        line = pathlines[i].strip()
        if i == 0:
            l = len(line)
            lv = len(line)
        else:
            l = len(line)
            if l != lv:
                return i
    tlist = []
    tcount = 0
    for l in range(len(pathlines)-1):
        pathlines[l] = pathlines[l].strip()

    for i in range(len(pathlines)-1):
        pathlines[i] = list(pathlines[i])
        if i == 0:
            for k in range(len(pathlines[i])-1):
                if pathlines[i][k] == "S":
                    pathlines[i][k] = "t"
        else:
            for j in range(len(pathlines[i])-1):
                if pathlines[i][j] == "." and pathlines[i-1][j] == "t":
                    pathlines[i][j] = "t"
                elif pathlines[i][j] == "^" and pathlines[i-1][j] == "t":
                    if not j == 0:
                        pathlines[i][j-1] = "t"
                    if not j == len(pathlines[i])-1:
                        pathlines[i][j+1] = "t"
                    tcount += 1


    return(tcount)

def d9one():
    with open("inputd9.txt") as f:
        tilines = f.readlines()
    
    for i in range(len(tilines)-1):
        tilines[i] = tilines[i].strip()
        first, _, second = tilines[i].partition(",")
        tilines[i] = (first, second)