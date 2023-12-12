input = open("input.txt", "r")
lines = [line.split() for line in input.read().strip().split("\n")]

# I found this cache bit on reddit, which makes it run in a few seconds instead of a few minutes
from functools import cache

@cache
def num_solutions(s, sizes, num_done_in_group=0):

    # If we are at the end of the string, we are done if we are not in a group and all groups are closed
    if not s:
        return not sizes and not num_done_in_group
    
    num_sols = 0
    
    # If next letter is a "?" we can replace it with either "." or "#" so we try both
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            # Extend current group if the spring is damaged
            num_sols += num_solutions(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                # If we were in a group that can be closed, close it
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += num_solutions(s[1:], sizes[1:])
            else:
                # If we are not in a group, move on to next symbol
                num_sols += num_solutions(s[1:], sizes)
    
    return num_sols

# Parse rows
rows = [(left, tuple(map(int, right.split(",")))) for left, right in lines]

# Part 1
def part1():
    sum = 0
    for group, sizes in rows:
        sum += num_solutions(group + ".", sizes)
    print(sum)

# Part 2
def part2():
    sum = 0
    for group, sizes in rows:
        group = "?".join([group] * 5) + "."     # "unfold" the pattern 5 times
        sizes *= 5

        sum += num_solutions(group, sizes)      # and solve
    print(sum)

part1()
part2()