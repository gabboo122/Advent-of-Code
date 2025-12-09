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
                    t += i
            ## pour un nombre n de répétitions
            else:
                for r in range(1, len(str(i))):
                    if len(str(i)) % r == 0:
                        rep = str(i)[:r]
                        if str(i) == rep * (len(str(i)) // r):
                            t += i

    return t




def d7one():
    with open("inputd7.txt") as f:
        pathlines = f.readlines()
    
    l = 0
    lv = 0
    for i in range(len(pathlines-1)):
        line = pathlines[i].strip()
        if i == 0:
            l = len(line)
            lv = len(line)
        else:
            l = len(line)
            if l != lv:
                return i
    return("True")