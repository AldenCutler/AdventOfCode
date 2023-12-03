from collections import defaultdict

# Read in the input
ll = [x for x in open("C:/Users/alden/OneDrive - Worcester Polytechnic Institute (wpi.edu)/Documents/projects/AdventOfCode/Day 2/input.txt").read().strip().split("\n")]

def part1():
    idSum = 0

    for l in ll:
        game_id = int(l.split(":")[0].split(" ")[1])
        l = l.split(":")[1]

        possible = True

        for s in l.split(";"):
            counts = defaultdict(int)

            for rev in s.split(", "):
                rev = rev.strip()
                counts[rev.split(" ")[1]] += int(rev.split(" ")[0])

            if not (counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14):
                possible = False

        if possible:
            idSum += game_id
      
    print(idSum)
    return idSum

def part2():
    powerSum = 0
    
    for l in ll:
        l = l.split(":")[1]

        min_counts = defaultdict(int)

        for s in l.split(";"):
            counts = defaultdict(int)

            for rev in s.split(", "):
                rev = rev.strip()
                counts[rev.split(" ")[1]] += int(rev.split(" ")[0])

            for k, v in counts.items():
                min_counts[k] = max(min_counts[k], v)

        powerSum += min_counts["red"] * min_counts["green"] * min_counts["blue"]
      
    print(powerSum)
    return powerSum
        
part1()
part2()