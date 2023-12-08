import math

lines = [line for line in open("input.txt", "r").read().strip().split("\n\n")]
instructions = list(lines[0])
connections = {}

def part1():    

    # Parse the lines and add the connections
    for line in lines[1].split("\n"):
        a = line.split(" ")[0]
        b = line.split("(")[1].split(",")[0]
        c = line.split(" ")[3].split(")")[0]
        connections[a] = (b, c)

    # Follow the connections
    position = "AAA"
    index = 0
    while position != "ZZZ":
        direction = instructions[index % len(instructions)]
        position = connections[position][0 if direction == "L" else 1]
        index += 1

    print("Part 1:", index)

def part2():

    # Add the recursive connections
    def solve_steps(start):
        position = start
        index = 0
        while not position.endswith("Z"):
            direction = instructions[index % len(instructions)]
            position = connections[position][0 if direction == "L" else 1]
            index += 1
        return index
    
    # Find the least common multiple of all the steps
    ret = 1
    for start in connections:
        if start.endswith("A"):
            ret = math.lcm(ret, solve_steps(start))

    print("Part 2:", ret)

part1()
part2()