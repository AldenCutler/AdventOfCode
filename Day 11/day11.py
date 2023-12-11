universe = open("input.txt").read().splitlines()

#####################
###    PART 1     ###
#####################

# find the rows and columns with no galaxies
doubleRows = []
doubleColumns = []
for i in range (len(universe)):
    row = list(universe[i])
    if all(x == "." for x in row):
        doubleRows.append(i)
for i in range(len(universe[0])):
    column = []
    for j in range(len(universe)):
        column.append(universe[j][i])
    if all(x == "." for x in column):
        doubleColumns.append(i)

# find all the galaxies
def findGalaxies():
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append((i,j))
    return galaxies

# find the shortest path between two galaxies
def shortestPath(galaxy1, galaxy2, multiplier):
    # find the shortest path between two galaxies
    # we can do this summing the difference between the x and y coordinates
    # of the two galaxies
    distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


    # if there is a double row or column between the two galaxies
    # we need to add 1 to the distance
    if (galaxy1[0] > galaxy2[0]):
        for i in range(galaxy2[0]+1, galaxy1[0]):
            if i in doubleRows:
                distance += multiplier
    else:
        for i in range(galaxy1[0]+1, galaxy2[0]):
            if i in doubleRows:
                distance += multiplier

    if (galaxy1[1] > galaxy2[1]):
        for i in range(galaxy2[1]+1, galaxy1[1]):
            if i in doubleColumns:
                distance += multiplier
    else:
        for i in range(galaxy1[1]+1, galaxy2[1]):
            if i in doubleColumns:
                distance += multiplier

    return distance
    
# find the sum of the shortest path between every pair of galaxies
def part1():
    # find all the galaxies
    galaxies = findGalaxies()

    # generate pairs of galaxies
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[j]))

    # sum the shortest path between every pair of galaxies
    total = 0
    for pair in pairs:
        total += shortestPath(pair[0], pair[1], 1)
    print(total)

part1()

#####################
###    PART 2     ###
#####################

# Part 2 is the same as part 1, but with a multiplier of 1000000
def part2():
    # find all the galaxies
    galaxies = findGalaxies()

    # generate pairs of galaxies
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[j]))

    # sum the shortest path between every pair of galaxies
    total = 0
    for pair in pairs:
        total += shortestPath(pair[0], pair[1], 1000000 - 1)    # subtract 1 because we're the distance becomes 1000000 when we add 999999
    print(total)

part2()